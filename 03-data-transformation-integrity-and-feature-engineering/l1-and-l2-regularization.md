---
title: "L1 and L2 Regularization: Quick Reference & Practical Guide"
exam: "MLA-C01"
status: "draft"
domain:
  - "1.2"
  - "1.3"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "03_data_transformation_integrity_and_feature_engineering"
aliases:
  - "L1 and L2 Regularization: Quick Reference & Practical Guide"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# L1 and L2 Regularization: Quick Reference & Practical Guide

---

## Quick Reference Summary

- **L1 Regularization (LASSO):** Drives some weights to zero (feature selection, sparse models)
- **L2 Regularization (Ridge):** Shrinks all weights smoothly (no weights exactly zero, dense models)
- **AWS Context:** Both are available in SageMaker built-in algorithms (e.g., Linear Learner, XGBoost)
- **When to Use:**
  - L1: When you want feature selection or have high-dimensional, sparse data
  - L2: When you want stability, handle multicollinearity, or keep all features

---

## 1. Overview

L1 and L2 regularization are techniques to prevent overfitting by adding a penalty to the loss function, discouraging overly complex models. They help improve generalization by constraining model weights.

- **L1 Regularization (LASSO):** Adds the sum of the absolute values of weights to the loss function.
- **L2 Regularization (Ridge):** Adds the sum of the squared values of weights to the loss function.

Both methods are widely used in machine learning, including AWS ML services.

---

## 2. Key Differences

| Aspect              | L1 (LASSO)                    | L2 (Ridge)                    |
| ------------------- | ----------------------------- | ----------------------------- | --- | ----- |
| Penalty Term        | λ∑                            | wᵢ                            |     | λ∑wᵢ² |
| Effect on Weights   | Many weights go to zero       | All weights shrink, none zero |
| Feature Selection   | Yes (sparse models)           | No (dense models)             |
| Solution Uniqueness | May have multiple solutions   | Unique solution               |
| Use Cases           | High-dimensional, sparse data | Multicollinearity, stability  |
| Computational Cost  | Slightly higher               | Lower                         |
| Geometric View      | Diamond constraint (corners)  | Circular constraint (smooth)  |

---

## 3. Practical Application

- **L1 Regularization:**
  - Useful when you want automatic feature selection (irrelevant features get zeroed out)
  - Good for high-dimensional, sparse datasets (e.g., text data, one-hot encoded features)
  - Example: Reducing the number of predictors in a regression model
- **L2 Regularization:**
  - Useful when you want to keep all features but reduce their impact
  - Helps with multicollinearity (correlated features)
  - Example: Ridge regression for stable, interpretable coefficients

---

## 4. AWS Services & Features

- **Amazon SageMaker Linear Learner:** Supports both L1 and L2 regularization. You can tune the regularization parameter (λ) as a hyperparameter.
- **Amazon SageMaker XGBoost:** Supports L1 ("alpha") and L2 ("lambda") regularization for tree-based models.
- **Other AWS ML Services:** Many built-in algorithms and frameworks (e.g., TensorFlow, PyTorch) allow you to configure regularization.

**Typical Use Cases in AWS:**

- Preventing overfitting in tabular data with SageMaker Linear Learner
- Feature selection in high-dimensional datasets
- Improving model generalization in production ML pipelines

---

## 5. Challenges & Best Practices

**Challenges:**

- Setting the regularization strength (λ) too high can underfit the model
- L1 can be unstable when features are highly correlated
- L2 does not perform feature selection (all features remain)

**Best Practices:**

- Use cross-validation to tune λ (regularization strength)
- Use L1 when you want a simpler, more interpretable model
- Use L2 for stability and when you want to keep all features
- In AWS SageMaker, leverage built-in hyperparameter tuning jobs to find the best regularization settings

---

## 6. Additional Resources

- [AWS SageMaker Linear Learner Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html)
- [AWS SageMaker XGBoost Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html)
- [Regularization in Machine Learning (GeeksforGeeks)](https://www.geeksforgeeks.org/regularization-in-machine-learning/)
- [L1 vs L2 Regularization (Neptune.ai)](https://neptune.ai/blog/fighting-overfitting-with-l1-or-l2-regularization)
- [AWS Certified Machine Learning – Associate Exam Guide](https://aws.amazon.com/certification/certified-machine-learning-specialty/)

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
