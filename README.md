# FlockML

> **Decentralized Edge AI. Turn your web traffic into a distributed GPU cluster.**

FlockML is a web-native federated learning infrastructure. It allows startups and developers to train AI models for $0 by crowdsourcing compute from their website visitors via non-blocking Web Workers, 8-bit Matrix Quantization, and Differential Privacy.

---

## ⚡ The Paradigm Shift

### The Problem (Centralized Cloud)
Currently, training Neural Networks requires renting astronomical A100 GPU clusters from AWS or GCP. Furthermore, user data must be shipped across the internet to these central servers, creating a massive privacy risk.

### The Fix (FlockML)
FlockML drops a silent, non-blocking Web Worker into your Next.js/React app. When a user visits your site, their local WebGPU processes tiny batches of training data. 
- **$0 Compute Costs:** 10,000 visitors = 10,000 active GPUs.
- **Cryptographic Privacy:** Data never leaves the browser. We inject Laplacian noise into the gradients before network transmission.
- **Infinite Scalability:** Your compute power scales linearly with your web traffic.

---

## ⚙️ Architecture Under the Hood

To make deep learning run natively in the browser without freezing the UI thread at 60fps, FlockML implements three core optimizations:

1. **8-Bit Quantization (`lib/federated/quantization.ts`)**
   Standard ML frameworks (PyTorch/TensorFlow) rely on heavy 32-bit floating point (`Float32`) numbers. FlockML mathematically compresses weight matrices down to `Int8` payloads. This reduces WebSocket payload sizes by 4x and dramatically speeds up local dot-products on mobile processors.

2. **Differential Privacy (`lib/federated/privacy.ts`)**
   FlockML utilizes Cryptographic Laplacian Noise to anonymize the gradients extracted from the user's local data. Because of the mathematics of Federated Averaging (FedAvg), when the central server aggregates thousands of these noisy gradients, the noise cancels out to 0, leaving only the pure, learned signal.

3. **Federated Averaging Coordinator (`lib/federated/coordinator.ts`)**
   The central backend server never trains. It simply orchestrates. It receives quantized, encrypted tensors from millions of browsers and mathematically averages them to update the Global Model.

---

## 🚀 Drop-in Integration

Get started in three lines of code in your existing React/Next.js layout:

```typescript
// 1. Import the node client
import { FlockNode } from 'flockml';

// 2. Connect to your central FedAvg Coordinator
FlockNode.connect('wss://api.yourdomain.com/flock');

// 3. Initialize background training
FlockNode.startTraining();
```

---

## 🛠 Project Structure
- `/src/matrix.ts` - Linear Algebra core (Dot products, transposition)
- `/src/activations.ts` - Calculus engine (Sigmoid, ReLU, derivatives)
- `/src/network.ts` - Neural Network logic (Forward Pass & Backpropagation)
- `/src/quantization.ts` - Float32 -> Int8 payload compression
- `/src/privacy.ts` - Differential Privacy via Laplacian Noise
- `/src/coordinator.ts` - FedAvg server aggregation
- `/src/client-node.ts` - Client API wrapper

---

## 📜 License
MIT License.
