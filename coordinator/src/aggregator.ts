import { ClientGradientUpdate, QuantizedPayload } from './types';
import { Quantizer } from './quantization';
import { ByzantineFaultFilter } from './bft_filter';
import { CertInAuditLogger } from './audit_logger';

export class FedAvgAggregator {
  public globalWeightsIH: number[][];
  public globalWeightsHO: number[][];
  public globalBiasH: number[][];
  public globalBiasO: number[][];

  // FedAvg-M Server Momentum state vectors
  private velocityIH: number[][];
  private velocityHO: number[][];
  private velocityBiasH: number[][];
  private velocityBiasO: number[][];
  private momentumBeta: number = 0.9;

  private pendingUpdates: ClientGradientUpdate[] = [];
  public currentRound: number = 1;
  public totalProcessedUpdatesCount: number = 0;
  public totalRejectedPoisonCount: number = 0;
  private bftFilter: ByzantineFaultFilter;

  constructor(
    public inputNodes: number = 2,
    public hiddenNodes: number = 4,
    public outputNodes: number = 1
  ) {
    this.globalWeightsIH = this.randomMatrix(hiddenNodes, inputNodes);
    this.globalWeightsHO = this.randomMatrix(outputNodes, hiddenNodes);
    this.globalBiasH = this.randomMatrix(hiddenNodes, 1);
    this.globalBiasO = this.randomMatrix(outputNodes, 1);

    this.velocityIH = this.zeroMatrix(hiddenNodes, inputNodes);
    this.velocityHO = this.zeroMatrix(outputNodes, hiddenNodes);
    this.velocityBiasH = this.zeroMatrix(hiddenNodes, 1);
    this.velocityBiasO = this.zeroMatrix(outputNodes, 1);

    this.bftFilter = new ByzantineFaultFilter(0.25);
  }

  private randomMatrix(rows: number, cols: number): number[][] {
    const mat: number[][] = [];
    for (let r = 0; r < rows; r++) {
      const row: number[] = [];
      for (let c = 0; c < cols; c++) {
        row.push((Math.random() * 2 - 1) * 0.5);
      }
      mat.push(row);
    }
    return mat;
  }

  private zeroMatrix(rows: number, cols: number): number[][] {
    return Array.from({ length: rows }, () => new Array(cols).fill(0));
  }

  public addUpdate(update: ClientGradientUpdate): void {
    this.pendingUpdates.push(update);
  }

  public getPendingCount(): number {
    return this.pendingUpdates.length;
  }

  public aggregate(): { success: boolean; round: number; validCount: number; rejectedCount: number } {
    if (this.pendingUpdates.length === 0) {
      return { success: false, round: this.currentRound, validCount: 0, rejectedCount: 0 };
    }

    const rawBatch = [...this.pendingUpdates];
    this.pendingUpdates = [];

    // 1. Run BFT Cosine Distance Filter on batch
    const filterResult = this.bftFilter.filterBatch(rawBatch);
    const validUpdates = filterResult.validUpdates;
    const rejectedCount = filterResult.rejectedCount;

    this.totalProcessedUpdatesCount += rawBatch.length;
    this.totalRejectedPoisonCount += rejectedCount;

    if (rejectedCount > 0) {
      CertInAuditLogger.log('SECURITY_OOB_PAYLOAD_DROP', 'BFT_FILTER', `Dropped ${rejectedCount} poisoned/outlier gradient updates.`);
    }

    if (validUpdates.length === 0) {
      console.warn(`[FedAvgAggregator] All ${rawBatch.length} updates rejected by BFT filter.`);
      return { success: false, round: this.currentRound, validCount: 0, rejectedCount };
    }

    // 2. Average valid dequantized matrices with FedAsync staleness attenuation
    const averageDequantized = (
      getKey: (u: ClientGradientUpdate) => QuantizedPayload,
      targetRows: number,
      targetCols: number
    ): number[][] => {
      const sum = this.zeroMatrix(targetRows, targetCols);
      let totalWeightSum = 0;

      for (const update of validUpdates) {
        // FedAsync Exponential Staleness Decay: S(staleness) = e^(-0.5 * staleness)
        const staleness = Math.max(0, this.currentRound - (update.roundId || this.currentRound));
        const stalenessWeight = Math.exp(-0.5 * staleness);
        totalWeightSum += stalenessWeight;

        const deq = Quantizer.dequantize(getKey(update));
        for (let r = 0; r < targetRows; r++) {
          for (let c = 0; c < targetCols; c++) {
            const val = deq[r] && deq[r][c] !== undefined ? deq[r][c] : 0;
            sum[r][c] += val * stalenessWeight;
          }
        }
      }

      for (let r = 0; r < targetRows; r++) {
        for (let c = 0; c < targetCols; c++) {
          sum[r][c] /= (totalWeightSum || 1);
        }
      }
      return sum;
    };

    const targetIHRows = this.globalWeightsIH.length;
    const targetIHCols = this.globalWeightsIH[0].length;
    const targetHORows = this.globalWeightsHO.length;
    const targetHOCols = this.globalWeightsHO[0].length;

    const avgWeightsIH = averageDequantized(u => u.weights_ih, targetIHRows, targetIHCols);
    const avgWeightsHO = averageDequantized(u => u.weights_ho, targetHORows, targetHOCols);
    const avgBiasH = averageDequantized(u => u.bias_h, targetIHRows, 1);
    const avgBiasO = averageDequantized(u => u.bias_o, targetHORows, 1);

    // 3. Apply Momentum FedAvg-M update: v_{t+1} = \beta v_t + (1 - \beta) avg
    const applyMomentum = (globalMat: number[][], velocityMat: number[][], avgMat: number[][]) => {
      for (let r = 0; r < globalMat.length; r++) {
        for (let c = 0; c < globalMat[0].length; c++) {
          velocityMat[r][c] = this.momentumBeta * velocityMat[r][c] + (1 - this.momentumBeta) * avgMat[r][c];
          globalMat[r][c] = avgMat[r][c];
        }
      }
    };

    applyMomentum(this.globalWeightsIH, this.velocityIH, avgWeightsIH);
    applyMomentum(this.globalWeightsHO, this.velocityHO, avgWeightsHO);
    applyMomentum(this.globalBiasH, this.velocityBiasH, avgBiasH);
    applyMomentum(this.globalBiasO, this.velocityBiasO, avgBiasO);

    const completedRound = this.currentRound;
    this.currentRound++;

    return {
      success: true,
      round: completedRound,
      validCount: validUpdates.length,
      rejectedCount
    };
  }

  public getQuantizedGlobalWeights() {
    return {
      weights_ih: Quantizer.quantize(this.globalWeightsIH),
      weights_ho: Quantizer.quantize(this.globalWeightsHO),
      bias_h: Quantizer.quantize(this.globalBiasH),
      bias_o: Quantizer.quantize(this.globalBiasO),
      roundId: this.currentRound
    };
  }
}
