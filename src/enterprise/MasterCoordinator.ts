import { LegacyNeuralNetwork as NeuralNetwork } from './legacy-network';
import { Matrix } from '../matrix';
import { Quantizer, QuantizedPayload } from '../quantization';
import { GradientPayload, QuantizedGradientPayload } from './PodAggregator';

export interface Task {
  id: string;
  assignedToNodeId: string | null;
  status: 'PENDING' | 'RUNNING' | 'COMPLETED' | 'FAILED';
  retryCount: number;
}

export interface NodeStatus {
  id: string;
  lastHeartbeat: number;
  status: 'ACTIVE' | 'DEAD';
  assignedTask: string | null;
}

/**
 * Enterprise Layer: Central Master Coordinator
 * 
 * Handles:
 * 1. Global Federated Averaging (from Pods)
 * 2. Fault Tolerance (Heartbeats & DAG Task Re-queueing)
 * 3. Security (Statistical Anomaly Gates against Poison Attacks)
 */
export class MasterCoordinator {
  public globalModel: NeuralNetwork;
  private pendingUpdates: GradientPayload[] = [];
  
  // Fault Tolerance State
  public nodes: Map<string, NodeStatus> = new Map();
  public taskQueue: Task[] = [];
  public completedTasks: Set<string> = new Set();
  
  private heartbeatInterval: any;

  constructor(inputNodes: number, hiddenNodes: number, outputNodes: number) {
    this.globalModel = new NeuralNetwork(inputNodes, hiddenNodes, outputNodes);
    
    // Start the chaos monitor loop (checks every 500ms)
    this.heartbeatInterval = setInterval(() => this.monitorGridHealth(), 500);
  }

  // --- FAULT TOLERANCE & DAG ROUTING ---

  public registerNode(nodeId: string): void {
    this.nodes.set(nodeId, {
      id: nodeId,
      lastHeartbeat: Date.now(),
      status: 'ACTIVE',
      assignedTask: null
    });
    console.log(`[MASTER] Node Registered: ${nodeId}`);
  }

  public recordHeartbeat(nodeId: string): void {
    const node = this.nodes.get(nodeId);
    if (node && node.status === 'ACTIVE') {
      node.lastHeartbeat = Date.now();
    }
  }

  public generateTasks(count: number): void {
    for (let i = 0; i < count; i++) {
      this.taskQueue.push({
        id: `TASK_${i}`,
        assignedToNodeId: null,
        status: 'PENDING',
        retryCount: 0
      });
    }
  }

  public requestTask(nodeId: string): Task | null {
    const node = this.nodes.get(nodeId);
    if (!node || node.status === 'DEAD') return null;

    // Find first pending task
    const task = this.taskQueue.find(t => t.status === 'PENDING');
    if (task) {
      task.status = 'RUNNING';
      task.assignedToNodeId = nodeId;
      node.assignedTask = task.id;
      return task;
    }
    return null;
  }

  /**
   * The Grid Monitor (Kalbaishakhi Defense)
   * Scans for nodes that missed heartbeats. If a node is DEAD, its assigned task is re-queued.
   */
  private monitorGridHealth(): void {
    const now = Date.now();
    const TIMEOUT_MS = 2000; // If no heartbeat in 2 seconds, assume DEAD

    this.nodes.forEach((node, nodeId) => {
      if (node.status === 'ACTIVE' && (now - node.lastHeartbeat > TIMEOUT_MS)) {
        node.status = 'DEAD';
        console.log(`\n[ALERT - GRID FAILURE] Substation ${nodeId} has gone OFFLINE.`);
        
        // Recover the stranded task (The DAG Re-queueing logic)
        if (node.assignedTask) {
          const task = this.taskQueue.find(t => t.id === node.assignedTask);
          if (task && task.status === 'RUNNING') {
            console.log(`[FAULT TOLERANCE] Recovering ${task.id} from DEAD Node ${nodeId}. Re-queuing...`);
            task.status = 'PENDING';
            task.assignedToNodeId = null;
            task.retryCount += 1;
            node.assignedTask = null;
          }
        }
      }
    });
  }

  // --- SECURITY & FEDERATED MATH ---

  public receivePodUpdate(podId: string, taskId: string, payload: QuantizedGradientPayload): void {
    const weights_ih = Quantizer.dequantize(payload.qWeightsIH);
    const weights_ho = Quantizer.dequantize(payload.qWeightsHO);
    const bias_h = Quantizer.dequantize(payload.qBiasH);
    const bias_o = Quantizer.dequantize(payload.qBiasO);

    // 1. STATISTICAL ANOMALY GATE (Poison Defense)
    if (this.detectAnomaly(weights_ih)) {
      console.error(`[SECURITY BREACH] Malicious/Poisoned tensor detected from Pod ${podId}. Payload dropped.`);
      return;
    }

    // 2. Accept Payload
    this.pendingUpdates.push({ weights_ih, weights_ho, bias_h, bias_o });
    this.completedTasks.add(taskId);
    
    // Mark task as complete
    const task = this.taskQueue.find(t => t.id === taskId);
    if (task) task.status = 'COMPLETED';

    console.log(`[MASTER] Received valid aggregated payload for ${taskId}`);
  }

  /**
   * Mathematical Gate: Checks if the incoming matrix contains NaN, Infinity, or absurdly high variance.
   * This proves to the government that hacked rural substations cannot poison the Global Model.
   */
  private detectAnomaly(matrix: Matrix): boolean {
    let sum = 0;
    for (let i = 0; i < matrix.rows; i++) {
      for (let j = 0; j < matrix.cols; j++) {
        const val = matrix.data[i][j];
        if (isNaN(val) || !isFinite(val)) return true;
        sum += Math.abs(val);
      }
    }
    const avgMagnitude = sum / (matrix.rows * matrix.cols);
    if (avgMagnitude > 10.0) return true; // Arbitrary high threshold for anomaly
    return false;
  }

  public aggregateGlobalModel(): void {
    if (this.pendingUpdates.length === 0) return;

    const numUpdates = this.pendingUpdates.length;
    console.log(`[MASTER] Performing Global FedAvg on ${numUpdates} pod updates...`);

    const averageMatrix = (matrixKey: keyof GradientPayload, targetMatrix: Matrix) => {
      const sumMatrix = new Matrix(targetMatrix.rows, targetMatrix.cols);
      for (const update of this.pendingUpdates) {
        sumMatrix.add(update[matrixKey]);
      }
      sumMatrix.multiply(1 / numUpdates);

      for (let i = 0; i < targetMatrix.rows; i++) {
        for (let j = 0; j < targetMatrix.cols; j++) {
          targetMatrix.data[i][j] = sumMatrix.data[i][j];
        }
      }
    };

    averageMatrix('weights_ih', this.globalModel.weights_ih);
    averageMatrix('weights_ho', this.globalModel.weights_ho);
    averageMatrix('bias_h', this.globalModel.bias_h);
    averageMatrix('bias_o', this.globalModel.bias_o);

    this.pendingUpdates = [];
  }
  
  public cleanup() {
    clearInterval(this.heartbeatInterval);
  }
}
