### Semantic Segmentation in Amazon SageMaker

**What’s it for?**

- **Pixel-level object classification**: Assigns a class to each individual pixel in an image, generating a segmentation mask.
- **Differs from image classification**: Image classification outputs a single label per image.
- **Differs from object detection**: Object detection assigns bounding boxes around detected objects.
- **Common Use Cases**:
  - Self-driving vehicles (e.g., road lane detection)
  - Medical imaging diagnostics (e.g., tumor segmentation)
  - Robotics (e.g., environmental understanding via scene segmentation)

---

**Training Input Requirements:**

- **Images**: JPG format for training and validation.
- **Annotations**: PNG format segmentation masks, where each pixel value corresponds to a class label.
- **Label Maps**: JSON or text files mapping pixel values in annotations to class labels.
- **Augmented Manifest**: Supported in **Pipe mode** to efficiently stream large datasets.
- **Inference**: Accepts JPG images for predictions.

---

**How is it used?**

- **Framework**: Built on **MXNet Gluon** and **GluonCV** libraries.
- **Available Algorithms**:
  - **Fully Convolutional Network (FCN)**
  - **Pyramid Scene Parsing (PSPNet)**
  - **DeepLabV3**
- **Backbone Network Choices**:
  - **ResNet50**
  - **ResNet101**
  - Both networks can be initialized with **ImageNet pre-trained weights** or trained from scratch.
- **Training Modes**:
  - **Full training**
  - **Incremental training** (transfer learning) supported.

---

**Important Hyperparameters:**

- **Algorithm**: Choose between `fcn`, `psp`, or `deeplab`.
- **Backbone**: Choose between `resnet50` or `resnet101`.
- **Epochs**: Number of times the training data is passed through the model.
- **Learning rate**: Controls the step size during optimization.
- **Batch size**: Number of images processed in each training iteration.
- **Optimizer**: Options such as SGD, Adam, etc.

---

**Instance Types (from your image):**

- **Training**:
  - Only **GPU-supported** instances.
  - Recommended: `P2`, `P3`, `G4dn`, or `G5` on a **single machine** only.
- **Inference**:
  - Can be done on **CPU instances** (`C5`, `M5`) or **GPU instances** (`P3`, `G4dn`).

---

**Key Notes**:

- Semantic segmentation is computationally heavy due to the per-pixel classification requirement.
- Multi-GPU training within a single machine is supported, but **multi-node (multi-machine) training is not**.
