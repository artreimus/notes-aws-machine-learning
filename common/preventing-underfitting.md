---
title: "Preventing Underfitting"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "draft"
domain:
  - "2.1"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-2"
aliases:
  - "Preventing Underfitting"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Preventing Underfitting

Underfitting happens when your model is too simple to capture the underlying structure of the data, resulting in poor performance on both training and validation sets. Here's how to address it in practice:

## 1. Enrich and Prepare Your Data

- **Add More Features:** Engineer new features that capture important patterns (e.g., polynomial features, interaction terms, domain-specific variables).
- **Reduce Excessive Preprocessing:** Overly aggressive dimensionality reduction or feature selection can remove useful information—revisit your pipeline.
- **Improve Data Quality:** Clean noisy labels, fill missing values, and ensure your data is representative of the problem space.
- **Increase Training Data:** If possible, collect more data or use data augmentation (especially for images/text) to provide the model with more signal.

## 2. Adjust Model Complexity

- **Choose a More Expressive Model:** If using linear regression, try polynomial regression, decision trees, or neural networks. For tree-based models, increase `max_depth` or number of trees.
- **Add Layers/Units:** For neural networks, increase the number of layers or units per layer.
- **Reduce Regularization:** Lower L1/L2 penalties (`alpha`, `lambda`, or `reg_param`) to allow the model to fit the data more closely.

## 3. Tune Training Process

- **Train Longer:** Increase the number of epochs or iterations. Underfitting can occur if training is stopped too early.
- **Adjust Learning Rate:** Sometimes a higher learning rate helps the model escape shallow minima, but be careful not to overshoot.
- **Batch Size:** For deep learning, try smaller batch sizes to introduce more noise and help the model learn richer representations.

## 4. Hyperparameter Tuning: What to Try

- **Tree Models:**
  - Increase `max_depth`, `min_samples_split`, or number of estimators.
  - Reduce regularization parameters like `min_child_weight` (XGBoost) or `lambda`.
- **Neural Networks:**
  - Add more layers/neurons.
  - Reduce dropout rate.
  - Lower weight decay (L2 regularization).
- **Linear Models:**
  - Add polynomial or interaction features.
  - Reduce regularization strength.

## 5. Practical Diagnosis

- **Learning Curves:** If both training and validation errors are high and close together, your model is underfitting.
- **Validation:** Try increasing model complexity or relaxing regularization and observe if training error drops and validation error improves.

## Example (SageMaker/XGBoost):

- If your XGBoost model underfits, try increasing `max_depth`, reducing `lambda`, or adding more features. In SageMaker, these are exposed as hyperparameters in the training job configuration.

## Key Takeaways

- Underfitting is usually solved by making the model more flexible, providing richer data, or relaxing constraints.
- Always monitor both training and validation errors to distinguish underfitting from overfitting.
- Tuning is iterative: make one change at a time and observe the effect.

## AWS Services & Features

- **Amazon SageMaker**: Supports a wide range of algorithms and model architectures, allowing you to increase model complexity as needed. SageMaker Autopilot and built-in algorithms provide options to tune model parameters and select more expressive models.
- **SageMaker Automatic Model Tuning**: Helps optimize hyperparameters (e.g., number of layers, learning rate) to reduce underfitting.
- **SageMaker Data Wrangler**: Enables advanced feature engineering to enrich datasets and reduce underfitting.

## Practical Application

- **Increase Model Complexity**: Use more complex algorithms (e.g., deeper neural networks, ensemble methods) when simple models underperform.
- **Feature Engineering**: Add relevant features, polynomial terms, or interaction variables to help the model capture more information.
- **Train Longer**: Increase the number of training epochs or iterations, especially if the model is under-trained.
- **Reduce Regularization**: Lower regularization strength (L1/L2 penalties) if the model is too constrained.
- **Hyperparameter Tuning**: Use SageMaker's hyperparameter tuning jobs to find optimal settings that reduce bias.

**Example:**

- If a linear regression model underfits a nonlinear dataset, try switching to a decision tree, random forest, or neural network. In SageMaker, you can easily swap algorithms and tune hyperparameters using built-in tools.

## Challenges & Best Practices

**Challenges:**

- Identifying underfitting can be subtle; look for high error on both training and validation sets.
- Adding too much complexity can quickly lead to overfitting—monitor performance carefully.
- Insufficient or poor-quality data can cause underfitting regardless of model choice.

**Best Practices:**

- Start with simple models, but increase complexity if both training and validation errors are high.
- Use cross-validation to assess model performance and detect underfitting.
- Perform thorough feature engineering and data preprocessing.
- Monitor learning curves to ensure the model is learning from the data.
- Use SageMaker Experiments to track different model configurations and results.

## Additional Resources

- [AWS SageMaker: Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)
- [Bias-Variance Tradeoff (AWS ML Blog)](https://aws.amazon.com/blogs/machine-learning/understanding-the-bias-variance-tradeoff/)
- [SageMaker Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
- [Feature Engineering Best Practices (AWS)](https://aws.amazon.com/big-data/datalakes-and-analytics/feature-engineering/)
