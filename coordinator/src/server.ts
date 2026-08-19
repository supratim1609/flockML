import express from 'express';
import http from 'http';
import fs from 'fs';
import path from 'path';
import { WebSocketServer, WebSocket } from 'ws';
import { FedAvgAggregator } from './aggregator';
import { WsMessage, ClientGradientUpdate, SwarmStats, WebRtcSignalPacket } from './types';
import { CertInAuditLogger } from './audit_logger';

const PORT = process.env.PORT ? parseInt(process.env.PORT) : 8080;
const AGGREGATION_INTERVAL_MS = process.env.AGGREGATION_INTERVAL_MS ? parseInt(process.env.AGGREGATION_INTERVAL_MS) : 3000;
const MIN_CLIENTS_FOR_AGGREGATION = 1;
const MAX_WEBSOCKET_PAYLOAD_BYTES = 5 * 1024 * 1024; // 5 MB max payload limit (DoS mitigation)
const MAX_SUBMISSIONS_PER_MINUTE = 30;

// Local SSD Storage Directory (Zero AWS S3 Cost)
const LOCAL_STORAGE_DIR = path.join(__dirname, '../storage');
if (!fs.existsSync(LOCAL_STORAGE_DIR)) {
  fs.mkdirSync(LOCAL_STORAGE_DIR, { recursive: true });
}

const app = express();
app.use(express.json({ limit: '50mb' }));
app.use('/models/download', express.static(LOCAL_STORAGE_DIR));

const server = http.createServer(app);
const wss = new WebSocketServer({ server, maxPayload: MAX_WEBSOCKET_PAYLOAD_BYTES });

const aggregator = new FedAvgAggregator(2, 4, 1);

interface ClientSession {
  nodeId: string;
  ws: WebSocket;
  ipAddress: string;
  connectedAt: Date;
  submissionTimestamps: number[];
  hardwareConfig?: {
    deviceType: string;
    hasWebGPU: boolean;
    hasWasmSimd: boolean;
  };
}

const activeClients = new Map<string, ClientSession>();
let totalGradientsReceived = 0;
let lastAggregationTime: string | null = null;

// CERT-In & MeitY Mandated HTTP Security Headers middleware
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  res.header('X-Frame-Options', 'SAMEORIGIN');
  res.header('X-Content-Type-Options', 'nosniff');
  res.header('X-XSS-Protection', '1; mode=block');
  res.header('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  next();
});

// REST Endpoint: Local SSD Model Upload (Zero-Cost S3 Replacement)
app.post('/models/upload', (req, res) => {
  try {
    const { modelName, payloadBase64 } = req.body;
    if (!modelName || !payloadBase64) {
      return res.status(400).json({ error: 'Missing modelName or payloadBase64' });
    }

    const safeName = path.basename(modelName).replace(/[^a-zA-Z0-9_\-\.]/g, '_');
    const filePath = path.join(LOCAL_STORAGE_DIR, safeName);
    const buffer = Buffer.from(payloadBase64, 'base64');
    
    fs.writeFileSync(filePath, buffer);
    CertInAuditLogger.log('SECURITY_GRADIENT_ACCEPTED', 'ADMIN', `Saved model checkpoint to local SSD: ${safeName} (${buffer.length} bytes)`);

    res.json({
      status: 'success',
      modelName: safeName,
      sizeBytes: buffer.length,
      downloadUrl: `/models/download/${safeName}`
    });
  } catch (err) {
    res.status(500).json({ error: `Upload failed: ${err}` });
  }
});

// REST Endpoint: Health Check
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    uptimeSeconds: Math.floor(process.uptime()),
    timestamp: new Date().toISOString()
  });
});

// REST Endpoint: Live Telemetry Metrics with BFT Security Metrics
app.get('/metrics', (req, res) => {
  const nodeTypes: { [key: string]: number } = {};
  activeClients.forEach((session) => {
    const dtype = session.hardwareConfig?.deviceType || 'Standard Device';
    nodeTypes[dtype] = (nodeTypes[dtype] || 0) + 1;
  });

  const totalProc = aggregator.totalProcessedUpdatesCount;
  const rejected = aggregator.totalRejectedPoisonCount;
  const passRate = totalProc > 0 ? parseFloat(((totalProc - rejected) / totalProc * 100).toFixed(2)) : 100.0;

  const stats: SwarmStats = {
    activeNodes: activeClients.size,
    totalRoundsCompleted: aggregator.currentRound,
    totalGradientsAggregated: totalGradientsReceived,
    poisonedPayloadsRejected: rejected,
    bftFilterPassRate: passRate,
    globalEpsilonPrivacy: 0.8,
    nodeTypes,
    lastAggregationTimestamp: lastAggregationTime
  };
  res.json(stats);
});

// REST Endpoint: List Connected Nodes
app.get('/nodes', (req, res) => {
  const nodes = Array.from(activeClients.values()).map(s => ({
    nodeId: s.nodeId,
    connectedAt: s.connectedAt,
    hardwareConfig: s.hardwareConfig
  }));
  res.json({ count: nodes.length, nodes });
});

// WebSocket Protocol Handlers with CERT-In Security Enforcement
wss.on('connection', (ws: WebSocket, req: http.IncomingMessage) => {
  let clientNodeId: string | null = null;
  const clientIp = (req.headers['x-forwarded-for'] as string || req.socket.remoteAddress || '127.0.0.1').split(',')[0].trim();

  ws.on('error', (err: Error) => {
    CertInAuditLogger.log('SECURITY_OVERSIZED_PAYLOAD_DROP', clientNodeId || 'UNKNOWN', `WebSocket socket error caught safely: ${err.message}`, { ipAddress: clientIp });
  });

  ws.on('message', (data: string) => {
    try {
      // 1. Oversized payload protection check
      if (typeof data === 'string' && data.length > MAX_WEBSOCKET_PAYLOAD_BYTES) {
        CertInAuditLogger.log('SECURITY_OVERSIZED_PAYLOAD_DROP', clientNodeId || 'UNKNOWN', `Payload length ${data.length} bytes exceeded 5MB limit. Closing socket.`, { ipAddress: clientIp });
        ws.close(1009, 'Payload Too Large');
        return;
      }

      const msg: WsMessage = JSON.parse(data);

      switch (msg.type) {
        case 'JOIN_SWARM': {
          clientNodeId = String(msg.nodeId || 'node_anon').replace(/[^a-zA-Z0-9_\-\.]/g, '_');
          if (clientNodeId === '__proto__' || clientNodeId === 'constructor' || clientNodeId === 'prototype') {
            clientNodeId = `safe_node_${Date.now()}`;
          }
          activeClients.set(clientNodeId, {
            nodeId: clientNodeId,
            ws,
            ipAddress: clientIp,
            connectedAt: new Date(),
            submissionTimestamps: [],
            hardwareConfig: msg.payload?.hardwareConfig
          });

          CertInAuditLogger.log('SECURITY_NODE_JOIN', clientNodeId, `Swarm node joined from IP ${clientIp} (${msg.payload?.hardwareConfig?.deviceType || 'Device'})`, { ipAddress: clientIp });

          // Send current global weights to the newly connected node
          const weightsPayload = aggregator.getQuantizedGlobalWeights();
          ws.send(JSON.stringify({
            type: 'WEIGHTS_BROADCAST',
            payload: weightsPayload
          }));
          break;
        }

        case 'GRADIENT_SUBMIT': {
          if (!clientNodeId) return;
          const session = activeClients.get(clientNodeId);
          if (!session) return;

          // 2. Node Rate Limiting Check
          const now = Date.now();
          session.submissionTimestamps = session.submissionTimestamps.filter(t => now - t < 60000);
          if (session.submissionTimestamps.length >= MAX_SUBMISSIONS_PER_MINUTE) {
            CertInAuditLogger.log('SECURITY_RATE_LIMIT_EXCEEDED', clientNodeId, `Rate limit exceeded (${session.submissionTimestamps.length} submissions/min). Dropping payload.`, { ipAddress: clientIp });
            return;
          }
          session.submissionTimestamps.push(now);

          const update: ClientGradientUpdate = msg.payload;

          // 3. Schema & Bound Validation (OOB Protection)
          if (
            !update || !update.weights_ih || !update.weights_ho ||
            update.weights_ih.rows > 10000 || update.weights_ih.cols > 10000 ||
            update.weights_ho.rows > 10000 || update.weights_ho.cols > 10000
          ) {
            CertInAuditLogger.log('SECURITY_OOB_PAYLOAD_DROP', clientNodeId, `OOB Payload matrix boundary violation detected. Dropping update.`, { ipAddress: clientIp });
            return;
          }

          aggregator.addUpdate(update);
          totalGradientsReceived++;
          CertInAuditLogger.log('SECURITY_GRADIENT_ACCEPTED', clientNodeId, `Gradient update queued for round #${update.roundId || 0}`, { ipAddress: clientIp });
          break;
        }

        case 'WEBRTC_SIGNAL': {
          const signal: WebRtcSignalPacket = msg.payload;
          const targetSession = activeClients.get(signal.targetNodeId);
          if (targetSession && targetSession.ws.readyState === WebSocket.OPEN) {
            targetSession.ws.send(JSON.stringify({
              type: 'WEBRTC_SIGNAL',
              payload: signal
            }));
          } else {
            console.warn(`[P2P Signaling] Target node ${signal.targetNodeId} not reachable for WebRTC signal.`);
          }
          break;
        }

        case 'REQUEST_WEIGHTS': {
          const weightsPayload = aggregator.getQuantizedGlobalWeights();
          ws.send(JSON.stringify({
            type: 'WEIGHTS_BROADCAST',
            payload: weightsPayload
          }));
          break;
        }

        case 'HEARTBEAT': {
          ws.send(JSON.stringify({ type: 'PONG', timestamp: new Date().toISOString() }));
          break;
        }
      }
    } catch (err) {
      CertInAuditLogger.log('SECURITY_OOB_PAYLOAD_DROP', clientNodeId || 'UNKNOWN', `JSON parse or schema validation crash: ${err}`, { ipAddress: clientIp });
    }
  });

  ws.on('close', () => {
    let removedId = clientNodeId;
    if (clientNodeId && activeClients.has(clientNodeId)) {
      activeClients.delete(clientNodeId);
    } else {
      activeClients.forEach((session, key) => {
        if (session.ws === ws) {
          activeClients.delete(key);
          removedId = key;
        }
      });
    }
    if (removedId) {
      CertInAuditLogger.log('SECURITY_NODE_DISCONNECT', removedId, `Node disconnected cleanly. Active remaining: ${activeClients.size}`, { ipAddress: clientIp });
    }
  });
});

// Periodically run BFT-filtered FedAvg-M aggregation and broadcast updated weights to all nodes
setInterval(() => {
  if (aggregator.getPendingCount() >= MIN_CLIENTS_FOR_AGGREGATION) {
    const result = aggregator.aggregate();
    if (result.success) {
      lastAggregationTime = new Date().toISOString();
      console.log(`[Swarm Coordinator] Executed BFT FedAvg-M Round #${aggregator.currentRound} (Accepted: ${result.validCount}, Poison Rejected: ${result.rejectedCount}). Broadcasting to ${activeClients.size} nodes.`);
      
      const updatedWeights = aggregator.getQuantizedGlobalWeights();
      const broadcastMsg = JSON.stringify({
        type: 'WEIGHTS_BROADCAST',
        payload: updatedWeights
      });

      activeClients.forEach((session) => {
        if (session.ws.readyState === WebSocket.OPEN) {
          session.ws.send(broadcastMsg);
        }
      });

      // Auto-save model checkpoint to local SSD every 10 aggregation rounds
      if (aggregator.currentRound % 10 === 0) {
        const checkpointPath = path.join(LOCAL_STORAGE_DIR, `checkpoint_round_${aggregator.currentRound}.json`);
        fs.writeFileSync(checkpointPath, JSON.stringify(updatedWeights, null, 2));
        CertInAuditLogger.log('SECURITY_GRADIENT_ACCEPTED', 'COORDINATOR', `Auto-saved model checkpoint to local SSD: checkpoint_round_${aggregator.currentRound}.json`);
      }
    }
  }
}, AGGREGATION_INTERVAL_MS);

server.listen(PORT, () => {
  console.log(`=======================================================`);
  console.log(` 🚀 FlockML Sovereign AI CERT-In Hardened Coordinator`);
  console.log(` 🏛️  Target: MeitY / NIC Node Network & Defense Swarms`);
  console.log(` 🛡️  CERT-In Audit Logging & DoS Defense: ONLINE`);
  console.log(` 📡 WebSocket Port: ${PORT}`);
  console.log(` 📊 Metrics API: http://localhost:${PORT}/metrics`);
  console.log(`=======================================================`);
});
