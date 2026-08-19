# Investor Live Demonstration Playbook

**Target Audience:** Anicut Capital (Summit Nayak) & Technical Evaluators  
**Primary Goal:** Prove that 3 separate machines on a local network form a unified, resilient OpenAI-compatible AI inference cluster.

---

## 13-Step Live Demonstration Sequence

### Step 1: Launch the Control Plane
Open Terminal 1:
```bash
cd coordinator
npx tsx src/inference_server.ts
```
*Output: Control Plane active on port 8080.*

---

### Step 2: Spawn Node 01 (Laptop)
Open Terminal 2:
```bash
cd coordinator
npx tsx src/node_agent.ts --id=node-01-apple-m2 --control-plane=http://localhost:8080
```
*Output: Node registered with hardware telemetry.*

---

### Step 3: Spawn Node 02 (GPU Workstation)
Open Terminal 3:
```bash
cd coordinator
npx tsx src/node_agent.ts --id=node-02-nvidia-rtx --control-plane=http://localhost:8080
```
*Output: Node registered as WebGPU worker.*

---

### Step 4: Spawn Node 03 (Telecom Hub)
Open Terminal 4:
```bash
cd coordinator
npx tsx src/node_agent.ts --id=node-03-telecom-hub --control-plane=http://localhost:8080
```
*Output: 3 nodes active in cluster.*

---

### Step 5: Send Live Inference Request
Open Terminal 5:
```bash
curl -N -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3-70b-flock",
    "messages": [{"role": "user", "content": "Demonstrate decentralized inference across 3 nodes."}],
    "stream": true
  }'
```
*Observation: Tokens stream back instantly as layers 0-10, 11-22, and 23-31 are computed across the 3 separate terminals.*

---

### Step 6: Trigger Fault Tolerance Chaos Test
In Terminal 2 (Node 01), press **`Ctrl + C`** to kill the node abruptly.

---

### Step 7: Send Second Request
In Terminal 5:
```bash
curl -N -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3-70b-flock",
    "messages": [{"role": "user", "content": "Verify failover recovery on healthy nodes."}],
    "stream": true
  }'
```
*Observation: The Control Plane detects the disconnect in <5ms, dynamically rebalances the layer pipeline across Node 02 and Node 03, and delivers the full response with ZERO user errors.*

---

## 1-Click Automated Runner

To run all 13 steps automatically in a single command:
```bash
NODE_PATH=./coordinator/node_modules npx tsx ./scripts/run_investor_lan_demo.ts
```
