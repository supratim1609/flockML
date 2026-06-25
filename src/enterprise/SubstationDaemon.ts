import { NeuralNetwork } from '../network';
import { Quantizer, QuantizedPayload } from '../quantization';
import { QuantizedGradientPayload } from './PodAggregator';
import { MasterCoordinator, Task } from './MasterCoordinator';
import { DifferentialPrivacy } from '../privacy';

/**
 * Enterprise Layer: Substation Worker Daemon
 * 
 * This code runs on the physical micro-racks inside a CESC Substation.
 * It constantly pings the Master to prove it is alive.
 * It pulls batches, runs the mathematical Forward/Backward pass locally,
 * and pushes the quantized results to its regional PodAggregator.
 */
export class SubstationDaemon {
  public id: string;
  private localModel: NeuralNetwork;
  private master: MasterCoordinator;
  
  private heartbeatInterval: any = null;
  public isPowerOn: boolean = true;

  constructor(id: string, master: MasterCoordinator, inputNodes: number, hiddenNodes: number, outputNodes: number) {
    this.id = id;
    this.master = master;
    this.localModel = new NeuralNetwork(inputNodes, hiddenNodes, outputNodes);
  }

  public bootUp(): void {
    this.isPowerOn = true;
    this.master.registerNode(this.id);
    
    // Ping heartbeat every 300ms
    this.heartbeatInterval = setInterval(() => {
      if (this.isPowerOn) {
        this.master.recordHeartbeat(this.id);
      }
    }, 300);
  }

  /**
   * Simulates a Kalbaishakhi power cut or a worker accidentally unplugging the machine.
   * Stops sending heartbeats immediately.
   */
  public simulatePowerFailure(): void {
    console.log(`\n[HARDWARE ALERT] Substation ${this.id} experienced a catastrophic power failure!`);
    this.isPowerOn = false;
    if (this.heartbeatInterval) {
      clearInterval(this.heartbeatInterval);
      this.heartbeatInterval = null;
    }
  }

  /**
   * Pulls a task, runs the Neural Network training math, and returns the Quantized Gradients.
   * Simulates async latency (like a GPU processing a batch).
   */
  public async processTask(task: Task): Promise<QuantizedGradientPayload | null> {
    if (!this.isPowerOn) return null;

    console.log(`[WORKER ${this.id}] Pulled ${task.id}. Beginning local matrix operations...`);
    
    // Simulate 1 second of heavy GPU processing latency
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // If power failed mid-processing, abort
    if (!this.isPowerOn) {
      console.log(`[WORKER ${this.id}] Died while processing ${task.id}. Gradients lost.`);
      return null;
    }

    // --- The Core Math (Forward & Backward Pass) ---
    // We train on a dummy XOR dataset to generate valid mathematical gradients
    const dummyInputs = [ [0,0], [0,1], [1,0], [1,1] ];
    const dummyTargets = [ [0], [1], [1], [0] ];
    
    // Train for 5 epochs locally
    for (let i=0; i<5; i++) {
      for (let j=0; j<dummyInputs.length; j++) {
        this.localModel.train(dummyInputs[j], dummyTargets[j]);
      }
    }

    console.log(`[WORKER ${this.id}] Mathematical processing complete for ${task.id}.`);
    console.log(`[DPDP COMPLIANCE] Injecting Laplacian Noise into weights for Substation ${this.id}...`);

    // DPDP Act Compliance: Inject mathematical noise before it leaves the local hardware
    DifferentialPrivacy.applyNoise(this.localModel.weights_ih, 0.5);
    DifferentialPrivacy.applyNoise(this.localModel.weights_ho, 0.5);
    DifferentialPrivacy.applyNoise(this.localModel.bias_h, 0.5);
    DifferentialPrivacy.applyNoise(this.localModel.bias_o, 0.5);

    console.log(`[WORKER ${this.id}] Anonymization complete. Quantizing payload...`);

    // Quantize the result for transmission
    return {
      qWeightsIH: Quantizer.quantize(this.localModel.weights_ih),
      qWeightsHO: Quantizer.quantize(this.localModel.weights_ho),
      qBiasH: Quantizer.quantize(this.localModel.bias_h),
      qBiasO: Quantizer.quantize(this.localModel.bias_o)
    };
  }

  public shutdown() {
    this.isPowerOn = false;
    if (this.heartbeatInterval) clearInterval(this.heartbeatInterval);
  }
}
