# Convolutional Neural Networks (CNNs)

## What Are CNNs For?

- Handle data that doesn’t align neatly into columns (e.g., images, sequential text).
- Common applications:
  - Image feature extraction and classification (detecting objects like a stop sign).
  - Machine translation, sentence classification, sentiment analysis in NLP.
- Feature-location invariance: filters detect patterns regardless of position in input.

## How CNNs Work

- **Biological inspiration**: modeled on visual cortex receptive fields that respond to local image patches.
- **Convolutional layers**:
  - Apply learnable filters (kernels) across input to produce feature maps.
  - Early filters detect edges (horizontal, vertical, diagonal).
- **Pooling/Subsampling layers**:
  - Downsample spatial dimensions (e.g., MaxPooling) to reduce resolution and computation.
- **Hierarchical feature learning**:
  - Lower layers capture basic features (edges, colors).
  - Intermediate layers combine into shapes.
  - Deeper layers recognize complex objects.
- **Color channels**:
  - RGB images use separate filters per channel, combined into multi-channel feature maps.

## How CNNs Work

1. **Low-level convolution** picks up strong red signals and octagonal edges.
2. **Higher-level filters** integrate edges into octagon shape and recognize letters “STOP.”
3. **Fully connected layers** match the composite pattern to the label "stop sign."

## Implementing CNNs with Keras / TensorFlow

- **Input**: tensor shape `(height, width, channels)`.
- **Key layers**:
  - `Conv2D(filters, kernel_size, activation)` for convolutions.
  - `MaxPooling2D(pool_size)` for spatial downsampling.
  - `Dropout(rate)` for regularization.
  - `Flatten()` to convert 2D maps to 1D vector.
  - `Dense(units, activation)` culminating in a `softmax` classifier.
- **Typical model flow**:
  ```
  Conv2D → MaxPooling2D → Dropout → Conv2D → MaxPooling2D → Dropout → Flatten → Dense → Softmax
  ```

## Challenges in CNNs

- **Resource intensity**: high CPU/GPU and memory usage for training and inference.
- **Hyperparameter tuning**: kernel sizes, number of filters, layers, pooling strategy, optimizer settings.
- **Data requirements**: large labeled datasets needed; data labeling and management often the hardest part.

## Specialized CNN Architectures

- **LeNet-5**: pioneering CNN for digit recognition.
- **AlexNet**: deeper network that popularized CNNs on ImageNet.
- **GoogLeNet (Inception)**: introduced inception modules (parallel convolution/filter paths).
- **ResNet (Residual Network)**: uses skip connections to train very deep networks without vanishing gradients.
