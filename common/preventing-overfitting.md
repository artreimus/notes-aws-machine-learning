# Preventing Overfitting

Overfitting occurs when a model learns the noise in the training data rather than the underlying pattern, resulting in poor generalization to new data. Common strategies to prevent overfitting include:

## Early Stopping

- Pause training before the model starts to learn noise.
- Helps avoid over-training, but requires careful timing.

## Pruning / Feature Selection

- Remove irrelevant or less important features from the dataset.
- Focus on features that have the most impact on predictions.

## Regularization

- Apply penalties to model complexity during training (e.g., L1, L2 regularization).
- Penalizes features with minimal impact to reduce overfitting.

## Ensembling

- Combine predictions from multiple models (e.g., bagging, boosting).
- Reduces variance and improves accuracy by leveraging diverse models.

## Data Augmentation

- Increase training data diversity by applying transformations (e.g., flipping, rotation, scaling) to input data.
- Especially useful in image and text data to improve model robustness.

---

**Best Practices:**

- Use cross-validation to monitor model performance.
- Regularly evaluate models on validation/test sets.
- Prefer simpler models when possible to reduce the risk of overfitting.
