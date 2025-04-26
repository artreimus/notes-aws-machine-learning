The purpose of **convolution** in a Convolutional Neural Network (CNN) is to automatically extract and learn **features** from input data, typically images.

Here's what it does:

1. **Feature Extraction**: Convolution layers apply filters (also called kernels) that slide over the input image. These filters detect local patterns like edges, textures, shapes, etc.

2. **Spatial Hierarchy**: Early layers capture low-level features (like edges), while deeper layers learn high-level patterns (like eyes, wheels, or full objects) by combining lower-level features.

3. **Parameter Efficiency**: Convolution uses shared weights (the same filter across the image), reducing the number of parameters compared to fully connected layers. This makes the network more efficient and less prone to overfitting.

4. **Preserves Spatial Relationships**: Unlike flattening or dense layers, convolutions maintain the spatial structure of the image, which is important for tasks like object detection or segmentation.
