import { Matrix } from '../matrix';
import { sigmoid, dsigmoid } from '../activations';

export class LegacyNeuralNetwork {
  inputNodes: number;
  hiddenNodes: number;
  outputNodes: number;
  
  weights_ih: Matrix;
  weights_ho: Matrix;
  bias_h: Matrix;
  bias_o: Matrix;
  
  learningRate: number;
  
  activationFunc: (x: number) => number;
  dActivationFunc: (y: number) => number;

  constructor(inputNodes: number, hiddenNodes: number, outputNodes: number) {
    this.inputNodes = inputNodes;
    this.hiddenNodes = hiddenNodes;
    this.outputNodes = outputNodes;

    this.weights_ih = new Matrix(this.hiddenNodes, this.inputNodes);
    this.weights_ho = new Matrix(this.outputNodes, this.hiddenNodes);
    this.weights_ih.randomize();
    this.weights_ho.randomize();

    this.bias_h = new Matrix(this.hiddenNodes, 1);
    this.bias_o = new Matrix(this.outputNodes, 1);
    this.bias_h.randomize();
    this.bias_o.randomize();

    this.learningRate = 0.1;
    this.activationFunc = sigmoid;
    this.dActivationFunc = dsigmoid;
  }

  predict(inputArray: number[]): number[] {
    const inputs = Matrix.from1DArray(inputArray);
    const hidden = Matrix.dot(this.weights_ih, inputs);
    hidden.add(this.bias_h);
    hidden.map(this.activationFunc);
    const outputs = Matrix.dot(this.weights_ho, hidden);
    outputs.add(this.bias_o);
    outputs.map(this.activationFunc);
    return outputs.toArray();
  }

  train(inputArray: number[], targetArray: number[]): void {
    const inputs = Matrix.from1DArray(inputArray);
    const hidden = Matrix.dot(this.weights_ih, inputs);
    hidden.add(this.bias_h);
    hidden.map(this.activationFunc);
    const outputs = Matrix.dot(this.weights_ho, hidden);
    outputs.add(this.bias_o);
    outputs.map(this.activationFunc);

    const targets = Matrix.from1DArray(targetArray);
    const outputErrors = Matrix.subtract(targets, outputs);
    const weights_ho_t = Matrix.transpose(this.weights_ho);
    const hiddenErrors = Matrix.dot(weights_ho_t, outputErrors);

    const gradients = Matrix.map(outputs, this.dActivationFunc);
    const gradientsMult = Matrix.multiply(gradients, outputErrors);
    gradientsMult.multiply(this.learningRate);

    const hidden_T = Matrix.transpose(hidden);
    const weight_ho_deltas = Matrix.dot(gradientsMult, hidden_T);

    this.weights_ho.add(weight_ho_deltas);
    this.bias_o.add(gradientsMult);

    const hiddenGradients = Matrix.map(hidden, this.dActivationFunc);
    const hiddenGradientsMult = Matrix.multiply(hiddenGradients, hiddenErrors);
    hiddenGradientsMult.multiply(this.learningRate);

    const inputs_T = Matrix.transpose(inputs);
    const weight_ih_deltas = Matrix.dot(hiddenGradientsMult, inputs_T);

    this.weights_ih.add(weight_ih_deltas);
    this.bias_h.add(hiddenGradientsMult);
  }
}
