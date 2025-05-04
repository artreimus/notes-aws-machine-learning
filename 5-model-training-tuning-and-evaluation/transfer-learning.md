# Transfer Learning

## 1. What Is Transfer Learning?

- **Definition**: leveraging knowledge gained in one domain or task to improve performance on a different but related task.
- **Why use it?**
  - Reduces data and compute requirements by starting from a pre-trained model.
  - Speeds up development and improves convergence when labeled data is scarce.
  - Enables re-use of models trained on massive datasets (e.g., ImageNet, language corpora) for specialized tasks.

## 2. Common Transfer Learning Approaches

### 2.1. Fine-Tuning (Continue Training)

- **Process**:
  1. Load a pre-trained model (all weights from source task).
  2. Continue training on your target dataset using a low learning rate.
- **Use case**: when your target data distribution is similar to the source and you have moderate labeled data.
- **Pros**: adapts full model representations; often highest accuracy.
- **Considerations**: risk of overfitting if target dataset is too small; requires careful learning-rate scheduling.

### 2.2. Feature Extraction (Add New Top Layers)

- **Process**:
  1. Freeze (or partially freeze) base layers of pre-trained model.
  2. Attach new trainable layers (e.g., dense or convolutional heads) for the target task.
  3. Train only the new layers, optionally fine-tune some base layers.
- **Use case**: when you have limited target data and want faster training.
- **Pros**: lower computational cost; reduces overfitting risk.

### 2.3. Retraining from Scratch

- **Process**: initialize model weights randomly and train entirely on the target dataset.
- **Use case**: when target task is fundamentally different or you have abundant data and compute.
- **Pros**: full control over architecture; no source bias.
- **Cons**: high data and computing requirements; longer training time.

### 2.4. Off-the-Shelf Use

- **Process**: use pre-trained model without any additional training.
- **Use case**: when source task aligns exactly with your requirements (e.g., use pre-trained BERT for sentiment analysis if its training data matches your domain).
- **Pros**: instant deployment; minimal effort.

## 3. Practical Steps

1. **Select a Pre-Trained Model**: choose architecture and source dataset (e.g., ResNet, BERT, GPT).
2. **Prepare Data**: ensure input format (image size, tokenization) matches pre-trained model requirements.
3. **Configure Training Strategy**: decide which layers to freeze, learning rates for each layer group.
4. **Train & Monitor**: use early stopping, learning-rate schedulers, and validation metrics to avoid over/under-fitting.
5. **Evaluate & Deploy**: benchmark on holdout data, optimize for inference (quantization, pruning) if needed.

## 4. Examples

- **Computer Vision**:
  - Starting from ImageNet-trained CNNs (ResNet, EfficientNet) to classify medical or satellite images.
- **Natural Language Processing**:
  - Fine-tuning BERT, RoBERTa, or GPT models for text classification, QA, summarization using Hugging Face Transformers.

## 5. Transfer Learning on AWS

- **SageMaker**:
  - Built-in support for pre-trained models in SageMaker JumpStart (vision, NLP, tabular).
  - Hugging Face DLCs (Deep Learning Containers) for seamless fine-tuning on managed infrastructure.
  - SageMaker Clarify, Debugger, and Model Monitor to ensure performance and bias controls post-transfer.

## 6. Best Practices & Tips

- **Start simple**: try feature extraction before full fine-tuning.
- **Layer-wise learning rates**: lower for pre-trained layers, higher for new layers.
- **Data augmentation**: especially in vision tasks to reduce overfitting.
- **Monitor for catastrophic forgetting**: ensure new task training does not erase useful pre-trained features.
