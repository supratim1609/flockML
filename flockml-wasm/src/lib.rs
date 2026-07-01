use wasm_bindgen::prelude::*;
use getrandom::getrandom;
use std::f64;

// Use `wee_alloc` as the global allocator if needed in the future for smaller binary size, 
// but standard allocator is fine for now.

#[wasm_bindgen]
pub struct WasmMatrix {
    rows: usize,
    cols: usize,
    // Flat array for better memory locality and cache hits compared to Vec<Vec<f64>>
    data: Vec<f64>,
}

#[wasm_bindgen]
impl WasmMatrix {
    /// Creates a new matrix filled with zeros
    #[wasm_bindgen(constructor)]
    pub fn new(rows: usize, cols: usize) -> WasmMatrix {
        WasmMatrix {
            rows,
            cols,
            data: vec![0.0; rows * cols],
        }
    }

    /// Expose getters for Javascript
    #[wasm_bindgen(getter)]
    pub fn rows(&self) -> usize {
        self.rows
    }

    #[wasm_bindgen(getter)]
    pub fn cols(&self) -> usize {
        self.cols
    }

    /// Load from a flat JS Float64Array
    pub fn from_array(rows: usize, cols: usize, array: &[f64]) -> WasmMatrix {
        WasmMatrix {
            rows,
            cols,
            data: array.to_vec(),
        }
    }

    /// Export back to JS Float64Array
    pub fn to_array(&self) -> Vec<f64> {
        self.data.clone()
    }

    /// O(n^3) Dot Product (Matrix Multiplication)
    /// This is where Rust WebAssembly destroys JS V8 performance.
    pub fn dot(&self, other: &WasmMatrix) -> Result<WasmMatrix, JsValue> {
        if self.cols != other.rows {
            return Err(JsValue::from_str(&format!(
                "Incompatible matrices for dot product: {} !== {}",
                self.cols, other.rows
            )));
        }

        let mut result = WasmMatrix::new(self.rows, other.cols);
        
        // Cache friendly iteration (i, k, j loop ordering is significantly faster for flat arrays)
        for i in 0..self.rows {
            for k in 0..self.cols {
                let a_ik = self.data[i * self.cols + k];
                for j in 0..other.cols {
                    result.data[i * other.cols + j] += a_ik * other.data[k * other.cols + j];
                }
            }
        }

        Ok(result)
    }

    /// Matrix Transpose
    pub fn transpose(&self) -> WasmMatrix {
        let mut result = WasmMatrix::new(self.cols, self.rows);
        for i in 0..self.rows {
            for j in 0..self.cols {
                result.data[j * self.rows + i] = self.data[i * self.cols + j];
            }
        }
        result
    }

    /// Element-wise addition of another matrix
    pub fn add(&mut self, other: &WasmMatrix) -> Result<(), JsValue> {
        if self.rows != other.rows || self.cols != other.cols {
            return Err(JsValue::from_str("Incompatible matrices for addition"));
        }
        for i in 0..self.data.len() {
            self.data[i] += other.data[i];
        }
        Ok(())
    }
    
    /// Element-wise subtraction (A - B)
    pub fn subtract(&self, other: &WasmMatrix) -> Result<WasmMatrix, JsValue> {
        if self.rows != other.rows || self.cols != other.cols {
            return Err(JsValue::from_str("Incompatible matrices for subtraction"));
        }
        let mut result = WasmMatrix::new(self.rows, self.cols);
        for i in 0..self.data.len() {
            result.data[i] = self.data[i] - other.data[i];
        }
        Ok(result)
    }

    /// Applies Differential Privacy (Laplacian Noise) to the matrix in-place
    pub fn apply_noise(&mut self, epsilon: f64, sensitivity: f64) {
        let scale = sensitivity / epsilon;
        let mut buf = [0u8; 8];
        
        for i in 0..self.data.len() {
            // Generate a secure uniform random u in [-0.5, 0.5] using getrandom
            let _ = getrandom(&mut buf);
            let bytes = u64::from_ne_bytes(buf);
            let mut u = (bytes as f64) / (u64::MAX as f64);
            u -= 0.5;

            let sign = if u < 0.0 { -1.0 } else { 1.0 };
            let noise = -scale * sign * (1.0 - 2.0 * u.abs()).ln();
            
            self.data[i] += noise;
        }
    }
}

// --------------------------------------------------------
// ACTIVATIONS
// --------------------------------------------------------

fn sigmoid(x: f64) -> f64 {
    1.0 / (1.0 + (-x).exp())
}

fn dsigmoid(y: f64) -> f64 {
    // Note: y is already the output of the sigmoid function
    y * (1.0 - y)
}

// --------------------------------------------------------
// FULL NEURAL NETWORK ENGINE
// --------------------------------------------------------

#[wasm_bindgen]
pub struct WasmNeuralNetwork {
    input_nodes: usize,
    hidden_nodes: usize,
    output_nodes: usize,
    learning_rate: f64,

    weights_ih: WasmMatrix,
    weights_ho: WasmMatrix,
    bias_h: WasmMatrix,
    bias_o: WasmMatrix,
}

#[wasm_bindgen]
impl WasmNeuralNetwork {
    #[wasm_bindgen(constructor)]
    pub fn new(input_nodes: usize, hidden_nodes: usize, output_nodes: usize) -> WasmNeuralNetwork {
        let mut weights_ih = WasmMatrix::new(hidden_nodes, input_nodes);
        let mut weights_ho = WasmMatrix::new(output_nodes, hidden_nodes);
        let mut bias_h = WasmMatrix::new(hidden_nodes, 1);
        let mut bias_o = WasmMatrix::new(output_nodes, 1);

        // Simple random initialization between -1 and 1
        let mut buf = [0u8; 8];
        let mut randomize = |m: &mut WasmMatrix| {
            for i in 0..m.data.len() {
                let _ = getrandom(&mut buf);
                let bytes = u64::from_ne_bytes(buf);
                let u = (bytes as f64) / (u64::MAX as f64);
                m.data[i] = (u * 2.0) - 1.0;
            }
        };

        randomize(&mut weights_ih);
        randomize(&mut weights_ho);
        randomize(&mut bias_h);
        randomize(&mut bias_o);

        WasmNeuralNetwork {
            input_nodes,
            hidden_nodes,
            output_nodes,
            learning_rate: 0.1,
            weights_ih,
            weights_ho,
            bias_h,
            bias_o,
        }
    }

    pub fn set_learning_rate(&mut self, lr: f64) {
        self.learning_rate = lr;
    }

    /// Feedforward Pass
    pub fn predict(&self, inputs_array: &[f64]) -> Result<Vec<f64>, JsValue> {
        let inputs = WasmMatrix::from_array(self.input_nodes, 1, inputs_array);

        let mut hidden = self.weights_ih.dot(&inputs)?;
        hidden.add(&self.bias_h)?;
        for x in &mut hidden.data { *x = sigmoid(*x); }

        let mut outputs = self.weights_ho.dot(&hidden)?;
        outputs.add(&self.bias_o)?;
        for x in &mut outputs.data { *x = sigmoid(*x); }

        Ok(outputs.data)
    }

    /// Backpropagation Training
    pub fn train(&mut self, inputs_array: &[f64], targets_array: &[f64]) -> Result<(), JsValue> {
        // --- FORWARD PASS ---
        let inputs = WasmMatrix::from_array(self.input_nodes, 1, inputs_array);

        let mut hidden = self.weights_ih.dot(&inputs)?;
        hidden.add(&self.bias_h)?;
        for x in &mut hidden.data { *x = sigmoid(*x); }

        let mut outputs = self.weights_ho.dot(&hidden)?;
        outputs.add(&self.bias_o)?;
        for x in &mut outputs.data { *x = sigmoid(*x); }

        // --- ERROR CALCULATION ---
        let targets = WasmMatrix::from_array(self.output_nodes, 1, targets_array);
        let output_errors = targets.subtract(&outputs)?;

        let weights_ho_t = self.weights_ho.transpose();
        let hidden_errors = weights_ho_t.dot(&output_errors)?;

        // --- CALCULATE OUTPUT GRADIENTS ---
        let mut gradients = WasmMatrix::new(outputs.rows, outputs.cols);
        for i in 0..outputs.data.len() {
            gradients.data[i] = dsigmoid(outputs.data[i]) * output_errors.data[i] * self.learning_rate;
        }

        let hidden_t = hidden.transpose();
        let weight_ho_deltas = gradients.dot(&hidden_t)?;

        self.weights_ho.add(&weight_ho_deltas)?;
        self.bias_o.add(&gradients)?;

        // --- CALCULATE HIDDEN GRADIENTS ---
        let mut hidden_gradients = WasmMatrix::new(hidden.rows, hidden.cols);
        for i in 0..hidden.data.len() {
            hidden_gradients.data[i] = dsigmoid(hidden.data[i]) * hidden_errors.data[i] * self.learning_rate;
        }

        let inputs_t = inputs.transpose();
        let weight_ih_deltas = hidden_gradients.dot(&inputs_t)?;

        self.weights_ih.add(&weight_ih_deltas)?;
        self.bias_h.add(&hidden_gradients)?;

        Ok(())
    }

    /// Extractor for Differential Privacy Payload Export
    pub fn export_weights(&mut self, epsilon: f64, sensitivity: f64) -> JsValue {
        // Apply Laplacian Noise
        self.weights_ih.apply_noise(epsilon, sensitivity);
        self.weights_ho.apply_noise(epsilon, sensitivity);
        self.bias_h.apply_noise(epsilon, sensitivity);
        self.bias_o.apply_noise(epsilon, sensitivity);

        // Serialize into JS Object (We could serialize into a typed Int8 array directly in the future)
        let payload = js_sys::Object::new();
        js_sys::Reflect::set(&payload, &"weights_ih".into(), &js_sys::Float64Array::from(self.weights_ih.data.as_slice()).into()).unwrap();
        js_sys::Reflect::set(&payload, &"weights_ho".into(), &js_sys::Float64Array::from(self.weights_ho.data.as_slice()).into()).unwrap();
        js_sys::Reflect::set(&payload, &"bias_h".into(), &js_sys::Float64Array::from(self.bias_h.data.as_slice()).into()).unwrap();
        js_sys::Reflect::set(&payload, &"bias_o".into(), &js_sys::Float64Array::from(self.bias_o.data.as_slice()).into()).unwrap();
        
        payload.into()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_matrix_creation() {
        let m = WasmMatrix::new(2, 3);
        assert_eq!(m.rows(), 2);
        assert_eq!(m.cols(), 3);
        assert_eq!(m.data.len(), 6);
    }

    #[test]
    fn test_dot_product() {
        let a = WasmMatrix::from_array(2, 2, &[1.0, 2.0, 3.0, 4.0]);
        let b = WasmMatrix::from_array(2, 2, &[5.0, 6.0, 7.0, 8.0]);
        let c = a.dot(&b).unwrap();
        
        assert_eq!(c.data, vec![19.0, 22.0, 43.0, 50.0]);
    }

    #[test]
    fn test_transpose() {
        let a = WasmMatrix::from_array(2, 3, &[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]);
        let b = a.transpose();
        
        assert_eq!(b.rows(), 3);
        assert_eq!(b.cols(), 2);
        assert_eq!(b.data, vec![1.0, 4.0, 2.0, 5.0, 3.0, 6.0]);
    }

    #[test]
    fn test_apply_noise() {
        let mut a = WasmMatrix::new(10, 10);
        a.apply_noise(1.0, 1.0);
        // Ensure noise actually mutated the zeros
        assert!(a.data.iter().any(|&x| x != 0.0));
    }

    #[test]
    fn test_extreme_stress_dot_product() {
        // "Test till it breaks"
        // Multiplying two 1000x1000 matrices requires 1,000,000,000 operations
        let a = WasmMatrix::new(1000, 1000);
        let b = WasmMatrix::new(1000, 1000);
        
        // This will panic/OOM if memory allocation fails, otherwise it will execute rapidly in Rust
        let c = a.dot(&b);
        assert!(c.is_ok());
    }

    #[test]
    fn test_god_tier_allocation() {
        // Testing memory allocation limits (5000 x 5000 = 25 million f64s = ~200 MB of RAM)
        let mut a = WasmMatrix::new(5000, 5000);
        let b = WasmMatrix::new(5000, 5000);
        
        // Element-wise addition of 200MB chunks
        let res = a.add(&b);
        assert!(res.is_ok());
    }

    #[test]
    fn test_insane_dot_product() {
        // Pushing the CPU to its absolute limit: 1500 x 1500 matrix dot product
        // Requires 3.375 BILLION floating point operations.
        // We initialize with a tiny number to avoid f64 Infinity overflow.
        let a = WasmMatrix::from_array(1500, 1500, &vec![0.0001; 2_250_000]);
        let b = WasmMatrix::from_array(1500, 1500, &vec![0.0001; 2_250_000]);
        
        let c = a.dot(&b);
        assert!(c.is_ok());
    }
}
