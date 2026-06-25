import { Matrix } from '../matrix';
import { Quantizer, QuantizedPayload } from '../quantization';

export interface GradientPayload {
  weights_ih: Matrix;
  weights_ho: Matrix;
  bias_h: Matrix;
  bias_o: Matrix;
}

export interface QuantizedGradientPayload {
  qWeightsIH: QuantizedPayload;
  qWeightsHO: QuantizedPayload;
  qBiasH: QuantizedPayload;
  qBiasO: QuantizedPayload;
}

/**
 * Enterprise Layer: Hierarchical Pod Aggregator
 * 
 * Instead of 1,000 substations DDoSing the Central Master server,
 * regional "Pods" (e.g., a server in Howrah) collect updates from 50 local substations.
 * It performs a mathematical Federated Average locally, and sends ONE compressed payload
 * to the Master. This reduces network ingress on the Master by 98%.
 */
export class PodAggregator {
  public podId: string;
  private pendingUpdates: GradientPayload[] = [];
  private aggregationThreshold: number; // How many updates to wait for before aggregating

  constructor(podId: string, aggregationThreshold: number = 5) {
    this.podId = podId;
    this.aggregationThreshold = aggregationThreshold;
  }

  /**
   * Receives a quantized gradient payload from a Substation Daemon.
   */
  public receiveSubstationUpdate(payload: QuantizedGradientPayload): void {
    // 1. De-quantize the payload for mathematical averaging
    const weights_ih = Quantizer.dequantize(payload.qWeightsIH);
    const weights_ho = Quantizer.dequantize(payload.qWeightsHO);
    const bias_h = Quantizer.dequantize(payload.qBiasH);
    const bias_o = Quantizer.dequantize(payload.qBiasO);

    this.pendingUpdates.push({ weights_ih, weights_ho, bias_h, bias_o });
  }

  /**
   * Mathematically averages all local substation updates.
   * Returns a single quantized payload to send to the Master Coordinator.
   * If threshold is not met, returns null.
   */
  public aggregateAndCompress(): QuantizedGradientPayload | null {
    if (this.pendingUpdates.length < this.aggregationThreshold) {
      return null; // Waiting for more nodes to finish
    }

    const numClients = this.pendingUpdates.length;
    
    // Grab dimensions from the first update
    const first = this.pendingUpdates[0];
    const avg_weights_ih = new Matrix(first.weights_ih.rows, first.weights_ih.cols);
    const avg_weights_ho = new Matrix(first.weights_ho.rows, first.weights_ho.cols);
    const avg_bias_h = new Matrix(first.bias_h.rows, first.bias_h.cols);
    const avg_bias_o = new Matrix(first.bias_o.rows, first.bias_o.cols);

    // Sum all matrices
    for (const update of this.pendingUpdates) {
      avg_weights_ih.add(update.weights_ih);
      avg_weights_ho.add(update.weights_ho);
      avg_bias_h.add(update.bias_h);
      avg_bias_o.add(update.bias_o);
    }

    // Divide by N (Average)
    avg_weights_ih.multiply(1 / numClients);
    avg_weights_ho.multiply(1 / numClients);
    avg_bias_h.multiply(1 / numClients);
    avg_bias_o.multiply(1 / numClients);

    // Clear local memory pool
    this.pendingUpdates = [];

    // Re-quantize for high-speed transmission to the Master
    return {
      qWeightsIH: Quantizer.quantize(avg_weights_ih),
      qWeightsHO: Quantizer.quantize(avg_weights_ho),
      qBiasH: Quantizer.quantize(avg_bias_h),
      qBiasO: Quantizer.quantize(avg_bias_o)
    };
  }

  public getPendingCount(): number {
    return this.pendingUpdates.length;
  }
}
