# Neural Networks

A neural network is a computational model inspired by the human brain's network of neurons. It consists of interconnected layers of nodes (neurons), where each connection has an associated weight, and each neuron applies an activation function to the weighted sum of its inputs plus a bias. Through training—typically using backpropagation and optimization algorithms like stochastic gradient descent—neural networks learn complex patterns and relationships in data, enabling tasks such as classification, regression, sequence prediction, and more.

## Types of Neural Networks

### 1. Feedforward Neural Networks (FNN)

- **Definition**: The simplest type of artificial neural network where connections between units do not form cycles. Data flows in one direction—from input layer, through hidden layers (if any), to output layer.
- **Architecture**:
  - **Input layer**: Receives raw data (features).
  - **Hidden layer(s)**: One or more layers of neurons performing weighted sums and activations.
  - **Output layer**: Produces final prediction or classification.
- **Activation Functions**: Sigmoid, ReLU (Rectified Linear Unit), Tanh, Softmax (in output layer for multi-class problems).
- **Training**: Backpropagation with gradient descent (or variants like Adam, RMSProp).
- **Use Cases**:
  - Regression problems (predict continuous values).
  - Simple classification (binary or multiclass).
- **Pros & Cons**:
  - **Pros**: Straightforward, fast to train for small problems.
  - **Cons**: Cannot capture spatial or temporal dependencies; prone to overfitting if too deep or wide.

---

### 2. Convolutional Neural Networks (CNN)

- **Definition**: Neural networks designed to process grid-like data (e.g., images) by leveraging convolutional layers that learn spatial hierarchies of features.
- **Key Components**:
  - **Convolutional layers**: Learn local filters (kernels) that detect edges, textures, shapes.
  - **Pooling layers**: Downsample feature maps (max pooling, average pooling) to reduce spatial dimensions.
  - **Fully connected layers**: At the end, to combine extracted features for classification or regression.
- **Typical Architecture for Image Classification**:
  1. Input image (e.g., 224×224×3)
  2. Convolution + ReLU → feature maps
  3. Pooling → reduced maps
  4. Repeat conv + pool blocks
  5. Flatten → vector
  6. Fully connected layers → logits
  7. Softmax → class probabilities
- **Use Case Example**: Detecting a stop sign in an image. The network learns to identify edges, corners, and eventually the specific shape and color patterns of stop signs.
- **Pros & Cons**:
  - **Pros**: Excellent for vision tasks; spatial parameter sharing reduces number of parameters.
  - **Cons**: Requires large amounts of labeled data; computationally intensive.

---

### 3. Recurrent Neural Networks (RNN)

- **Definition**: Networks with loops in their connections, allowing information to persist. Designed to process sequential data by maintaining a hidden state that captures context.
- **Architecture**:
  - **Recurrent layer**: At each time step _t_, processes input _xₜ_ and previous hidden state _hₜ₋₁_ to produce new hidden state _hₜ_.
  - **Output layer**: Can produce output at each time step or only at the end.
- **Mathematical Step**:
  \[h*t = \phi(W*{xh}x*t + W*{hh}h*{t-1} + b_h)\]
  \[y_t = W*{hy}h_t + b_y\]
  where \(\phi\) is activation (tanh or ReLU).
- **Use Cases**:
  - Time series prediction (stock prices, weather forecasting).
  - Language modeling, next-word prediction.
  - Machine translation (input and output sequences).
- **Limitations**:
  - Vanishing/exploding gradients for long sequences.

---

### 4. Long Short-Term Memory (LSTM)

- **Definition**: A special kind of RNN capable of learning long-range dependencies using gated cells to control information flow.
- **Cell Components**:
  - **Forget gate** \(f_t\): Decides which information to discard from cell state.
  - **Input gate** \(i_t\): Decides which new information to add.
  - **Candidate layer** \(\tilde{C}\_t\): Creates new candidate values.
  - **Cell state** \(C_t\): Accumulates long-term memory.
  - **Output gate** \(o_t\): Decides what to output from cell state.
- **Equations**:
  \[
  f*t = \sigma(W_f\cdot[x_t,h*{t-1}] + b*f)\\
  i_t = \sigma(W_i\cdot[x_t,h*{t-1}] + b*i)\\
  \tilde{C}\_t = \tanh(W_C\cdot[x_t,h*{t-1}] + b*C)\\
  C_t = f_t \* C*{t-1} + i*t \* \tilde{C}\_t\\
  o_t = \sigma(W_o\cdot[x_t,h*{t-1}] + b_o)\\
  h_t = o_t \* \tanh(C_t)
  \]
- **Use Cases**:
  - Language translation and sequence-to-sequence tasks.
  - Speech recognition.
  - Time series forecasting with long dependencies.

---

### 5. Gated Recurrent Unit (GRU)

- **Definition**: A streamlined version of LSTM that combines forget and input gates into a single update gate, with fewer parameters.
- **Cell Components**:
  - **Update gate** \(z_t\): Controls how much of previous state to keep.
  - **Reset gate** \(r_t\): Controls how to combine new input with previous memory.
- **Equations**:
  \[
  z*t = \sigma(W_z\cdot[x_t,h*{t-1}] + b*z)\\
  r_t = \sigma(W_r\cdot[x_t,h*{t-1}] + b*r)\\
  \tilde{h}\_t = \tanh(W_h\cdot[x_t, r_t \* h*{t-1}] + b*h)\\
  h_t = (1 - z_t) \* h*{t-1} + z_t \* \tilde{h}\_t
  \]
- **Use Cases**:
  - Similar to LSTM but when computational efficiency and fewer parameters are desired.
  - Real-time sequence processing on resource-constrained devices.
