**Subsampling**, also known as **pooling**, is a technique used in CNNs to reduce the spatial dimensions (width and height) of feature maps after convolution. The most common type is **max pooling**, but **average pooling** is also used.

### Purpose of Subsampling:

1. **Reduce Computation**: Smaller feature maps mean fewer computations in later layers.
2. **Prevent Overfitting**: By simplifying the features, the model becomes less sensitive to small variations and noise.
3. **Capture Dominant Features**: In max pooling, for instance, only the strongest feature (maximum value) in a region is kept, helping highlight the most important patterns.

### How It Works:

For example, in **2×2 max pooling**:

- A 2×2 window slides over the feature map.
- In each window, it picks the maximum value.
- The output is a smaller feature map.
