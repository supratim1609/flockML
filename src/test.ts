import { Coordinator } from './coordinator';
import { SwarmNode } from './client-node';
import { Matrix } from './matrix';

console.log("=== SCATTER.JS END-TO-END TEST ===");

// 1. Initialize the Central Coordinator
// Expecting 2 inputs, 4 hidden nodes, 1 output node
const coordinator = new Coordinator(2, 4, 1);
console.log("\n[Server] Initialized FedAvg Coordinator.");

// 2. Initialize two Edge Clients (Browsers)
const clientA = new SwarmNode(2, 4, 1);
const clientB = new SwarmNode(2, 4, 1);
clientA.connect('wss://mock.network');
clientB.connect('wss://mock.network');

// Override weights to be identical at the start so we can see the effect of training
const startingWeights = coordinator.getGlobalWeightsForBroadcast();
clientA.syncGlobalWeights(startingWeights.weights_ih, startingWeights.weights_ho, startingWeights.bias_h, startingWeights.bias_o);
clientB.syncGlobalWeights(startingWeights.weights_ih, startingWeights.weights_ho, startingWeights.bias_h, startingWeights.bias_o);

// 3. Define some mock training data (XOR problem)
const inputs = [
  [0, 0],
  [0, 1],
  [1, 0],
  [1, 1]
];
const targets = [
  [0],
  [1],
  [1],
  [0]
];

// 4. Train the clients locally on the Edge
console.log("\n[Edge] Client A training local batch...");
clientA.trainLocalBatch(inputs, targets);

console.log("[Edge] Client B training local batch...");
clientB.trainLocalBatch(inputs, targets);

// 5. Secure & Quantize Gradients
console.log("\n[Edge] Applying Laplacian Noise & 8-Bit Quantization...");
clientA.privacyEpsilon = 1.5; // Moderate privacy
clientB.privacyEpsilon = 1.5;

const payloadA = clientA.exportSecureGradients();
const payloadB = clientB.exportSecureGradients();

console.log(`[Network] Payload A Size (Int8): ${payloadA.weights_ih.data.length} bytes`);
console.log(`[Network] Payload A Min/Max: ${payloadA.weights_ih.min.toFixed(2)} to ${payloadA.weights_ih.max.toFixed(2)}`);

// 6. Send to Coordinator for FedAvg
console.log("\n[Server] Receiving Encrypted Payloads...");
coordinator.receiveUpdate(payloadA.weights_ih, payloadA.weights_ho, payloadA.bias_h, payloadA.bias_o);
coordinator.receiveUpdate(payloadB.weights_ih, payloadB.weights_ho, payloadB.bias_h, payloadB.bias_o);

console.log("[Server] Running Federated Averaging (FedAvg)...");
// Snapshot original weight
const oldWeight = coordinator.globalModel.weights_ih.data[0][0];

coordinator.aggregate();

// Snapshot new weight
const newWeight = coordinator.globalModel.weights_ih.data[0][0];

console.log(`\n=== TEST RESULTS ===`);
console.log(`Global Weight Before FedAvg:  ${oldWeight.toFixed(4)}`);
console.log(`Global Weight After FedAvg:   ${newWeight.toFixed(4)}`);
console.log(`Weight Delta:                 ${(newWeight - oldWeight).toFixed(4)}`);
console.log("\n✅ SUCCESS: End-to-End Pipeline Executed (Edge Training -> Noise -> Quantization -> Aggregation)");
