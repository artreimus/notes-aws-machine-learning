# Recurrent Neural Networks (RNNs)\*\*

## 1. What Are RNNs For?

- **Time-series prediction**: modeling sequential data where past inputs influence future outputs.
  - Stock prices, sensor logs, web traffic, self-driving car trajectories.
- **Variable-length sequences**: handling inputs and/or outputs of arbitrary length.
  - Machine translation, text generation, image captioning, music composition.

## 2. RNN Fundamentals

### 2.1. Recurrent Neuron (Memory Cell)

- A single RNN neuron maintains a hidden state that is updated at each time step:
  \[ h*t = f(W*{xh} x*t + W*{hh} h\_{t-1} + b) \]
- It “remembers” information by feeding its previous state back into itself.
- **Unrolled view**: shows the same neuron at each time step, passing state forward.

### 2.2. Layers of Recurrent Neurons

- Multiple neurons in a layer share the same recurrence but have distinct weights and biases.
- Outputs at each time step can be taken from each neuron or only at the final step, depending on the task.

## 3. RNN Topologies

- **Sequence → Sequence**: produces an output at every time step (e.g., sequence of predicted stock prices).
- **Sequence → Vector**: encodes an entire input sequence into a single vector (e.g., sentence → sentiment).
- **Vector → Sequence**: generates a sequence from a fixed-length vector (e.g., image embedding → captions).
- **Encoder–Decoder**:
  - Encoder RNN compresses input sequence into a context vector.
  - Decoder RNN expands context into an output sequence (e.g., neural machine translation).

## 4. Training RNNs

- **Backpropagation Through Time (BPTT)**:
  - Unrolls the network across time and applies standard backprop to the unrolled graph.
  - Computationally expensive as sequence length grows.
- **Truncated BPTT**: limits the number of time steps for gradient propagation to reduce cost.
- **Challenges**:
  - **Vanishing/exploding gradients**: long-range dependencies can be lost or gradients can blow up.
  - **State dilution**: information from early steps weakens over time.

## 5. Gated RNN Architectures

### 5.1. LSTM (Long Short-Term Memory)

- Introduces **gates** to control information flow:
  - **Forget gate (fₜ)**: decides what information to discard.
  - **Input gate (iₜ)**: decides what new information to store.
  - **Output gate (oₜ)**: decides what to output from the cell.
- Maintains separate **cell state (Cₜ)** and **hidden state (hₜ)** for long-term and short-term memory.

### 5.2. GRU (Gated Recurrent Unit)

- Simplifies LSTM by combining forget and input gates into an **update gate**.
- Merges cell and hidden states into a single state.
- Often performs on par with LSTM with fewer parameters.

## 6. Practical Considerations & Challenges

- **Hyperparameter sensitivity**: topology (layers, units), learning rate, sequence length.
- **Resource intensity**: training can be slow and memory-heavy for long sequences.
- **Convergence issues**: improper configuration may prevent training from converging.
