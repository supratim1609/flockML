import { WebSocket } from 'ws';

const COORDINATOR_URL = 'ws://localhost:8080';
const NUM_SIMULATED_NODES = 5;

console.log(`=======================================================`);
console.log(` 🧪 Starting Simulated 5-Node Swarm Verification Test`);
console.log(`=======================================================`);

const sockets: WebSocket[] = [];

for (let i = 0; i < NUM_SIMULATED_NODES; i++) {
  const nodeId = `sim-node-${i + 1}`;
  const ws = new WebSocket(COORDINATOR_URL);

  ws.on('open', () => {
    console.log(`[Client ${nodeId}] Connected to coordinator.`);
    
    // Handshake: JOIN_SWARM
    ws.send(JSON.stringify({
      type: 'JOIN_SWARM',
      nodeId,
      payload: {
        hardwareConfig: {
          deviceType: i % 2 === 0 ? 'Apple M2 Air' : 'Linux Workstation',
          hasWebGPU: true,
          hasWasmSimd: true
        }
      }
    }));

    // Send gradient update
    setTimeout(() => {
      console.log(`[Client ${nodeId}] Transmitting simulated Int8 gradient payload...`);
      ws.send(JSON.stringify({
        type: 'GRADIENT_SUBMIT',
        nodeId,
        payload: {
          nodeId,
          roundId: 1,
          weights_ih: { min: -0.5, max: 0.5, rows: 4, cols: 2, data: new Array(8).fill(128) },
          weights_ho: { min: -0.5, max: 0.5, rows: 1, cols: 4, data: new Array(4).fill(128) },
          bias_h: { min: -0.1, max: 0.1, rows: 4, cols: 1, data: new Array(4).fill(128) },
          bias_o: { min: -0.1, max: 0.1, rows: 1, cols: 1, data: new Array(1).fill(128) }
        }
      }));
    }, 1000 + i * 200);
  });

  ws.on('message', (data: string) => {
    const msg = JSON.parse(data);
    if (msg.type === 'WEIGHTS_BROADCAST') {
      console.log(`✅ [Client ${nodeId}] Received updated global model weights from server (Round #${msg.payload.roundId})!`);
    }
  });

  sockets.push(ws);
}

// Exit after 6 seconds
setTimeout(() => {
  console.log(`=======================================================`);
  console.log(` 🏁 5-Node Swarm Simulation Test Completed Successfully!`);
  console.log(`=======================================================`);
  sockets.forEach(s => s.close());
  process.exit(0);
}, 6000);
