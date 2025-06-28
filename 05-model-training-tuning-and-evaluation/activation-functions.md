## Activation Functions

Activation functions are crucial in neural networks as they introduce non-linearity, allowing the model to learn complex patterns. They determine how the weighted sum of inputs is transformed into an output signal for each neuron.

- **Linear**: $f(x) = x$. Provides identity mapping; commonly used in output layers for regression tasks since it does not squash values.
- **Binary Step**: $f(x)=\begin{cases}1,&x>0\\0,&x\le0\end{cases}$. Introduces thresholding behavior but is non-differentiable at 0, hindering gradient-based training.
- **Sigmoid / Logistic**: $f(x) = \dfrac{1}{1 + e^{-x}}$. Squashes inputs to the $(0,1)$ range; historically popular but prone to vanishing gradients for large $|x|$.
- **Tanh**: $f(x) = \tanh(x)$. Squashes to $(-1,1)$ and is zero-centered, but can still suffer from vanishing gradients at the tails.
- **ReLU (Rectified Linear Unit)**: $f(x) = \max(0, x)$. Simple and efficient; mitigates vanishing gradients for positive inputs but can lead to "dying ReLU" when neurons output 0 permanently.
- **Leaky ReLU**: $f(x) = \max(\alpha x, x)$ with a small $\alpha$ (e.g., 0.01). Allows a small gradient when $x<0$, reducing the risk of inactive neurons.
- **PReLU (Parametric ReLU)**: $f(x) = \max(\alpha x, x)$ where $\alpha$ is learned during training, offering more flexibility per neuron or channel.
- **ELU (Exponential Linear Unit)**: $f(x) = \begin{cases}x,&x>0\\ \alpha (e^{x}-1),&x\le0\end{cases}$. Smooths negative activations and can converge faster than ReLU variants.
- **Maxout**: $f(x) = \max_{i}(w_{i}^{T}x + b_{i})$ over multiple linear functions. Learns both activation shape and weights but increases parameter count.
- $1
- **Softmax**: f_i(x) = exp(x_i) / Σ_j exp(x_j). Converts a vector of raw scores into a probability distribution; commonly used in the output layer for multi-class classification.

### When to Use Activation Functions

| Activation         | When to Use                                  | Notes                                             |
| ------------------ | -------------------------------------------- | ------------------------------------------------- |
| Linear             | Output layer for regression                  | Keeps values unbounded                            |
| Binary Step        | Simple binary classification thresholding    | Non-differentiable; not used in hidden layers     |
| Sigmoid            | Output layer for binary classification       | Squashes to (0,1); risk of vanishing gradients    |
| Tanh               | Hidden layers requiring zero-centered output | Better gradient flow; still vanishing at extremes |
| ReLU               | Hidden layers in deep networks               | Efficient; risk of dead neurons                   |
| Leaky ReLU / PReLU | Hidden layers to mitigate dead neurons       | PReLU learns leak parameter                       |
| ELU                | Hidden layers needing smoother negatives     | May speed convergence; extra computation          |
| Maxout             | Hidden layers requiring flexible activations | High parameter count; learns activation shape     |
| Swish              | Deep models seeking slight accuracy gains    | Smooth, non-monotonic; can outperform ReLU        |
| Softmax            | Output layer for multi-class classification  | Converts logits to probabilities                  |
