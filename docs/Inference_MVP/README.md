# FlockML: Decentralized Inference Cloud MVP

FlockML turns consumer and enterprise hardware on a local network (LAN) into a unified, high-speed AI inference cluster.

Developers make standard OpenAI-compatible API calls (`POST /v1/chat/completions`), while FlockML automatically discovers nodes, shards transformer layers, routes requests, and provides sub-5ms failover resilience.

---

## 5-Minute Quickstart

### 1. Start the FlockML Control Plane
```bash
cd coordinator
npm install
npm run build
npx tsx src/inference_server.ts
```
*Control Plane is now active on `http://localhost:8080` (or your LAN IP `http://192.168.1.X:8080`).*

---

### 2. Join Compute Nodes to the Cluster

On any machine on your Wi-Fi/Ethernet network:
```bash
# Terminal on Machine 1 (e.g. MacBook Pro M2)
npx tsx src/node_agent.ts --id=node-01-apple-m2 --control-plane=http://<CONTROL_PLANE_IP>:8080

# Terminal on Machine 2 (e.g. Workstation RTX GPU)
npx tsx src/node_agent.ts --id=node-02-nvidia-gpu --control-plane=http://<CONTROL_PLANE_IP>:8080

# Terminal on Machine 3 (e.g. Set-Top Box / Linux Server)
npx tsx src/node_agent.ts --id=node-03-telecom-hub --control-plane=http://<CONTROL_PLANE_IP>:8080
```

---

### 3. Send Inference Requests (OpenAI SDK Drop-In)

```python
from openai import OpenAI

# Point client to your local FlockML Control Plane
client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="flockml-lan-token"
)

stream = client.chat.completions.create(
    model="llama-3-70b-flock",
    messages=[{"role": "user", "content": "Explain decentralized inference in one sentence."}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 1-Click Automated Investor Demo

To run the complete automated 13-step demonstration:
```bash
NODE_PATH=./coordinator/node_modules npx tsx ./scripts/run_investor_lan_demo.ts
```
