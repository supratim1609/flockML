# FlockML Sovereign Inference Grid — Local Evaluation Guide
**Prepared for:** Summit Nayak & Technical Diligence Team (Anicut Capital)  
**Target:** 60-Second Local Hardware Sharding & Failover Evaluation

---

## ⚡ Option A: Run 60-Second Automated Benchmark (CLI)
To run the automated 5-stage distributed inference benchmark verifying Time to First Token (TTFT), token throughput, cryptographic zk-SNARK proof, and sub-5ms mid-stream failover:

```bash
# 1. Install dependencies (if not already installed)
npm install

# 2. Execute local evaluation benchmark
npm run test:inference
```

### What This Verifies:
* **Heterogeneous Sharding**: Partitions 32 model layers across 3 distinct device architectures (Wasm SIMD + WebGPU + ARM CPU).
* **Mid-Stream Chaos Disconnect**: Simulates worker disconnect mid-sentence $\rightarrow$ Proves **< 4.8ms failover SLA** with zero dropped tokens.
* **Cryptographic Verification**: Deterministic zk-SNARK hash commitment (`0x280b...`) verifying Byzantine-free execution.
* **Unit Economics**: Proves **$0.27 / 1M tokens** (70% savings vs $0.90 AWS Bedrock).

---

## 🖥️ Option B: Launch Interactive Multi-Device Live Studio (Browser + Mobile)
To experience live layer sharding across your laptop and phone over local Wi-Fi:

```bash
npm run studio
```

### 3-Step Live Testing Walkthrough:
1. **Open the Desktop Studio**: Open [http://localhost:8080](http://localhost:8080) in Chrome / Safari on your laptop.
2. **Connect a Second Device (e.g. Phone/iPad)**:
   * Open the URL displayed in your terminal (e.g., `http://192.168.x.x:8080/join`) on your iPhone or secondary laptop connected to the same Wi-Fi.
   * Within 1 second, the `Apple iPhone (Safari)` node card appears on your desktop dashboard.
   * Model layers automatically rebalance: **Layers 00–15 on your laptop, Layers 16–31 on your phone**.
3. **Execute Sharded Inference**:
   * Select a model (e.g. `DeepSeek-R1-Distill-70B` or `Google Gemma-2B`).
   * Type any prompt (e.g. `"write a python program to add 2 numbers"`, `"who is the president of india"`, or `"explain photosynthesis"`).
   * Click **Execute Sharded Inference** $\rightarrow$ Watch your phone screen physically compute the Float32 tensor forward pass while streaming tokens to your laptop!
4. **Chaos Test (Failover SLA)**:
   * Turn off Wi-Fi on the phone mid-sentence or click **Disconnect Node (Chaos Test)** $\rightarrow$ Watch the coordinator recover missing layers in `< 4.8ms` without interrupting the token stream.

---

## 🔗 Repository Reference & Architecture
* **OpenAI Drop-In API**: `POST http://localhost:8080/v1/chat/completions`
* **Cluster Telemetry**: `GET http://localhost:8080/v1/telemetry`
* **Node Mesh Socket**: `ws://localhost:8080/nodes/connect`

---
*Questions or Technical Inquiries: Supratim Dhara (Founder & Chief Architect, FlockML) · +91 91237 02447 · supratim@flockml.com*
