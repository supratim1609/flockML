import { QuantizedPayload } from './types';

export class Quantizer {
  /**
   * Dequantize Int8 (0-255) data back to 2D Float numbers.
   * Handles both quantized payloads and raw unquantized matrix objects safely.
   */
  static dequantize(q: QuantizedPayload | any): number[][] {
    if (!q) return [];
    
    // Check if q is a raw unquantized matrix format: { rows, cols, data: number[] }
    if (q.min === undefined || q.max === undefined) {
      const rows = q.rows || 1;
      const cols = q.cols || (q.data ? q.data.length : 0);
      const data: number[] = q.data || [];
      const result: number[][] = [];
      
      for (let r = 0; r < rows; r++) {
        const row: number[] = [];
        for (let c = 0; c < cols; c++) {
          row.push(data[r * cols + c] || 0);
        }
        result.push(row);
      }
      return result;
    }

    const { min, max, rows, cols, data } = q;
    const range = max - min;
    const result: number[][] = [];

    for (let r = 0; r < rows; r++) {
      const row: number[] = [];
      for (let c = 0; c < cols; c++) {
        const val = data[r * cols + c];
        // 0 -> min, 255 -> max
        const floatVal = range === 0 ? min : min + (val / 255.0) * range;
        row.push(floatVal);
      }
      result.push(row);
    }
    return result;
  }

  /**
   * Quantize 2D Float numbers to Int8 (0-255) array for broadcasting back to clients.
   */
  static quantize(matrixData: number[][]): QuantizedPayload {
    const rows = matrixData.length;
    const cols = matrixData[0].length;
    
    let min = Infinity;
    let max = -Infinity;

    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const val = matrixData[r][c];
        if (val < min) min = val;
        if (val > max) max = val;
      }
    }

    if (min === max) {
      return { min, max, rows, cols, data: new Array(rows * cols).fill(127) };
    }

    const range = max - min;
    const data: number[] = [];

    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const val = matrixData[r][c];
        const qVal = Math.round(((val - min) / range) * 255.0);
        data.push(qVal);
      }
    }

    return { min, max, rows, cols, data };
  }
}
