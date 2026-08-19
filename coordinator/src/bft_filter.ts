import { QuantizedPayload, ClientGradientUpdate } from './types';
import { Quantizer } from './quantization';

export class ByzantineFaultFilter {
  private minSimilarityThreshold: number;

  constructor(minSimilarityThreshold: number = 0.20) {
    this.minSimilarityThreshold = minSimilarityThreshold;
  }

  /**
   * Flatten 2D Float matrix to 1D vector for fast vector math.
   */
  private flatten(matrix: number[][]): number[] {
    const vec: number[] = [];
    for (let r = 0; r < matrix.length; r++) {
      for (let c = 0; c < matrix[r].length; c++) {
        vec.push(matrix[r][c]);
      }
    }
    return vec;
  }

  /**
   * Extract full flat gradient vector from an update.
   */
  public extractGradientVector(update: ClientGradientUpdate): number[] {
    const wIH = this.flatten(Quantizer.dequantize(update.weights_ih));
    const wHO = this.flatten(Quantizer.dequantize(update.weights_ho));
    const bH = this.flatten(Quantizer.dequantize(update.bias_h));
    const bO = this.flatten(Quantizer.dequantize(update.bias_o));
    return [...wIH, ...wHO, ...bH, ...bO];
  }

  /**
   * Compute Cosine Similarity between two 1D Float vectors.
   * CosineSim(A, B) = (A . B) / (||A|| * ||B||)
   */
  public cosineSimilarity(v1: number[], v2: number[]): number {
    if (v1.length !== v2.length || v1.length === 0) return 0;

    let dot = 0;
    let norm1 = 0;
    let norm2 = 0;

    for (let i = 0; i < v1.length; i++) {
      const a = v1[i];
      const b = v2[i];
      if (isNaN(a) || !isFinite(a) || isNaN(b) || !isFinite(b)) return -1; // Poisoned numeric anomaly
      dot += a * b;
      norm1 += a * a;
      norm2 += b * b;
    }

    const mag = Math.sqrt(norm1) * Math.sqrt(norm2);
    if (mag === 0) return 0;
    return dot / mag;
  }

  /**
   * Compute the element-wise Median Vector across a batch of vectors.
   */
  public computeMedianVector(vectors: number[][]): number[] {
    if (vectors.length === 0) return [];
    const len = vectors[0].length;
    const medianVec: number[] = new Array(len);

    for (let i = 0; i < len; i++) {
      const colValues = vectors.map(v => v[i]).sort((a, b) => a - b);
      const mid = Math.floor(colValues.length / 2);
      medianVec[i] = colValues.length % 2 !== 0 
        ? colValues[mid] 
        : (colValues[mid - 1] + colValues[mid]) / 2;
    }
    return medianVec;
  }

  /**
   * Filters out Byzantine/Poisoned gradient updates from a batch.
   * Returns valid updates and counts rejected poisoned payloads.
   */
  public filterBatch(updates: ClientGradientUpdate[]): { validUpdates: ClientGradientUpdate[]; rejectedCount: number } {
    if (updates.length <= 2) {
      // Single/dual update check for basic NaN/Infinity/Extreme Magnitude check
      const valid: ClientGradientUpdate[] = [];
      let rejected = 0;

      for (const update of updates) {
        const vec = this.extractGradientVector(update);
        const hasAnomaly = vec.some(val => isNaN(val) || !isFinite(val) || Math.abs(val) > 20.0);
        if (hasAnomaly) {
          rejected++;
          console.warn(`[BFT Security Gate] Rejected payload from ${update.nodeId}: Numeric anomaly detected.`);
        } else {
          valid.push(update);
        }
      }
      return { validUpdates: valid, rejectedCount: rejected };
    }

    // Extract all vectors
    const vectors = updates.map(u => this.extractGradientVector(u));
    const medianVec = this.computeMedianVector(vectors);

    const validUpdates: ClientGradientUpdate[] = [];
    let rejectedCount = 0;

    for (let i = 0; i < updates.length; i++) {
      const update = updates[i];
      const vec = vectors[i];

      // Check numeric bounds
      const hasAnomaly = vec.some(val => isNaN(val) || !isFinite(val) || Math.abs(val) > 20.0);
      if (hasAnomaly) {
        rejectedCount++;
        console.warn(`[BFT Security Gate] Rejected payload from ${update.nodeId}: Numeric anomaly.`);
        continue;
      }

      // Compute Cosine Distance to the Median Vector
      const sim = this.cosineSimilarity(vec, medianVec);
      if (sim < this.minSimilarityThreshold) {
        rejectedCount++;
        console.warn(`[BFT Security Gate] Rejected Byzantine/Poisoned payload from node ${update.nodeId} (Cosine similarity: ${sim.toFixed(4)} < threshold ${this.minSimilarityThreshold}).`);
      } else {
        validUpdates.push(update);
      }
    }

    return { validUpdates, rejectedCount };
  }
}
