# FlockML Architecture: Decentralized Edge Inference Cloud

## 1. System Topology

```
+-------------------------------------------------------------------------+
|                              DEVELOPER LAYER                            |
|        (Python OpenAI SDK / LangChain / LiteLLM / cURL HTTP Calls)      |
+-------------------------------------------------------------------------+
                                     |
                                     | POST /v1/chat/completions (SSE Stream)
                                     v
+-------------------------------------------------------------------------+
|                     FLOCKML CONTROL PLANE (Port 8080)                   |
|  - REST & WebSocket Gateway: Accepts requests, parses prompts           |
|  - Dynamic Scheduler: Slices 32-layer 70B model into layer shards       |
|  - Cluster Topology Manager: Discovers nodes & monitors 50ms heartbeats |
|  - Sub-5ms Work-Stealing Coordinator: Detects drops & rebalances DAG    |
+-------------------------------------------------------------------------+
                                     |
               +---------------------+---------------------+
               |                     |                     |
               | WebSocket Tensors   | WebSocket Tensors   | WebSocket Tensors
               v                     v                     v
+--------------------+ +--------------------+ +--------------------+
|  NODE 01 (Laptop)  | |   NODE 02 (GPU)    | |  NODE 03 (Set-Top) |
|  Layers 00 - 10    | |   Layers 11 - 22   | |   Layers 23 - 31   |
|  Embedding/Attn    | |   BitNet MatMul    | |   Dequantization   |
+--------------------+ +--------------------+ +--------------------+
               |                     |                     |
               +---------------------+---------------------+
                                     |
                                     v
                 Streaming Output Tokens -> Developer Client
```

---

## 2. Core Components

### A. Control Plane (`coordinator/src/inference_server.ts`)
- **HTTP Engine:** Serves `/v1/chat/completions`, `/v1/models`, `/v1/telemetry`.
- **WebSocket Hub:** Listens on `/nodes/connect` for node join/leave events.
- **Dynamic Sharding:** Calculates memory-proportional layer assignments across connected nodes.

### B. Node Agent (`coordinator/src/node_agent.ts`)
- Discovers CPU cores, RAM, and GPU capabilities on startup.
- Dispatches periodic heartbeats to maintain cluster liveness.
- Receives forward activation tensors, executes WebGPU / BitNet matrix multiplications, and streams activations to the next layer node.

### C. Fault Tolerance & Work Stealing
- If a node drops or disconnects mid-token, the Control Plane's DAG scheduler catches the disconnect in under 5ms and re-routes the pending layer shard to a healthy neighbor.
- Zero error codes or partial tokens are returned to the developer.
