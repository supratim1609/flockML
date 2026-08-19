import WebSocket from 'ws';

console.log(`========================================================================`);
console.log(` 🚀 MEITY 50-NODE DUAL-REGION SIMULATION LOAD TEST`);
console.log(` Target: 25 NIC Delhi Nodes + 25 NIC Kolkata Nodes`);
console.log(`========================================================================`);

const SERVER_URL = 'ws://localhost:8080';
const TOTAL_NODES = 50;
const sockets: WebSocket[] = [];

let connectedCount = 0;
let weightsBroadcastsReceived = 0;

function createVirtualNode(id: number) {
  const isDelhi = id <= 25;
  const region = isDelhi ? 'meity-delhi' : 'nic-kolkata';
  const nodeId = `node-${region}-${id.toString().padStart(2, '0')}`;

  const ws = new WebSocket(SERVER_URL);

  ws.on('open', () => {
    connectedCount++;
    // 1. Send JOIN_SWARM
    ws.send(JSON.stringify({
      type: 'JOIN_SWARM',
      nodeId,
      payload: {
        tenantId: region,
        hardwareConfig: {
          deviceType: isDelhi ? 'NIC Delhi Workstation (i7 WebGPU)' : 'NIC Kolkata Terminal (i5 WASM SIMD)',
          hasWebGPU: isDelhi,
          hasWasmSimd: true
        }
      }
    }));

    if (connectedCount === TOTAL_NODES) {
      console.log(`\n✅ ALL 50 VIRTUAL NODES CONNECTED (25 Delhi + 25 Kolkata)!`);
      startGradientSubmissions();
    }
  });

  ws.on('message', (data: string) => {
    const msg = JSON.parse(data);
    if (msg.type === 'WEIGHTS_BROADCAST') {
      weightsBroadcastsReceived++;
    }
  });

  ws.on('error', (err) => {
    console.error(`[Node ${nodeId}] WebSocket Error:`, err);
  });

  sockets.push(ws);
}

function startGradientSubmissions() {
  console.log(`\n[Simulating Gradients] Submitting 50 BitNet quantized gradient updates...`);
  
  sockets.forEach((ws, idx) => {
    const nodeId = `node-${idx < 25 ? 'meity-delhi' : 'nic-kolkata'}-${(idx + 1).toString().padStart(2, '0')}`;
    
    // Send GRADIENT_SUBMIT
    ws.send(JSON.stringify({
      type: 'GRADIENT_SUBMIT',
      nodeId,
      payload: {
        clientNodeId: nodeId,
        samplesCount: 64,
        roundId: 1,
        weights_ih: {
          rows: 2,
          cols: 4,
          data: [0.01, -0.02, 0.03, -0.01, 0.05, -0.04, 0.02, 0.01]
        },
        weights_ho: {
          rows: 4,
          cols: 1,
          data: [0.1, -0.2, 0.3, -0.1]
        }
      }
    }));
  });

  setTimeout(() => {
    console.log(`\n========================================================================`);
    console.log(` 📊 50-NODE SIMULATION SUMMARY RESULTS:`);
    console.log(`   • Connected Virtual Nodes: ${connectedCount} / 50`);
    console.log(`   • Global Weight Broadcasts Received: ${weightsBroadcastsReceived}`);
    console.log(`========================================================================`);
    
    // Close all connections cleanly
    sockets.forEach(ws => ws.close());
    process.exit(0);
  }, 4000);
}

// Spawn 50 virtual nodes
for (let i = 1; i <= TOTAL_NODES; i++) {
  createVirtualNode(i);
}
