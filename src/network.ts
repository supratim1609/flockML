import { WasmNeuralNetwork } from 'flockml-wasm';

/**
 * The Core Neural Network Engine.
 * 
 * V1.1.0 Architecture: This class is now a thin, memory-safe wrapper around 
 * the high-performance Rust WebAssembly Engine (`WasmNeuralNetwork`).
 * All Backpropagation and Feedforward math executes natively in C++ speeds.
 */
export class NeuralNetwork {
  inputNodes: number;
  hiddenNodes: number;
  outputNodes: number;
  
  // The raw WebAssembly instance
  private wasmNetwork: WasmNeuralNetwork;

  constructor(inputNodes: number, hiddenNodes: number, outputNodes: number) {
    this.inputNodes = inputNodes;
    this.hiddenNodes = hiddenNodes;
    this.outputNodes = outputNodes;

    // Instantiate the WebAssembly Engine
    // (Note: `initWasm()` must have been called previously by `FlockNode`)
    this.wasmNetwork = new WasmNeuralNetwork(inputNodes, hiddenNodes, outputNodes);
  }

  /**
   * The Forward Pass (Feedforward).
   * Executes entirely inside WebAssembly for maximum speed.
   */
  predict(inputArray: number[]): number[] {
    const float64Inputs = new Float64Array(inputArray);
    const result = this.wasmNetwork.predict(float64Inputs);
    return Array.from(result);
  }

  /**
   * The Backpropagation Algorithm (Training).
   * Executes entirely inside WebAssembly, completely avoiding JS-Wasm boundary overhead.
   */
  train(inputArray: number[], targetArray: number[]): void {
    const float64Inputs = new Float64Array(inputArray);
    const float64Targets = new Float64Array(targetArray);
    this.wasmNetwork.train(float64Inputs, float64Targets);
  }

  /**
   * Serializes the model weights and biases for network transmission.
   * We skip JSON serialization and directly export the encrypted Wasm payload.
   */
  serialize(): any {
    // We pass the differential privacy parameters directly to Wasm so it encrypts natively
    return this.wasmNetwork.export_weights(0.5, 1.0);
  }

  /**
   * Load global weights from the Coordinator (FedAvg).
   */
  loadWeights(data: any): void {
    // TODO: Implement the WASM side of loading de-quantized weights for FedAvg.
    // For V1.1.0, this is stubbed as we migrate the coordinator logic.
    console.warn("[NeuralNetwork] loadWeights() needs to be wired to Wasm API");
  }
}

