---
title: "K Nearest Neighbor"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "draft"
domain:
  - "2.1"
  - "2.2"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-2"
  - "06_sagemaker_built_in_algorithms"
aliases:
  - "K Nearest Neighbor"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# K Nearest Neighbor

**K-Nearest Neighbors (k-NN): Overview and Applications**

Amazon SageMaker's k-NN is a simple yet powerful algorithm for both classification and regression tasks. It operates on the principle that similar data points tend to have similar outcomes, making predictions based on the characteristics of the k closest points in the feature space.

**Key Characteristics:**

- Non-parametric, instance-based learning algorithm
- Supports both classification and regression tasks
- Classification: Returns most frequent label among k nearest neighbors
- Regression: Returns average value of k nearest neighbors
- Particularly effective for irregular decision boundaries

**Training Input Requirements:**

- **Train Channel:** Required, contains training data
- **Test Channel:** Optional, emits accuracy (classification) or MSE (regression)
- **Input Formats:**
  - recordIO-protobuf
  - CSV format (first column must be the label)
- **Mode Support:** Both file and pipe modes supported

**Usage and Applications:**

- **Classification Tasks:**
  - Customer review sentiment analysis
  - Image classification
  - Document categorization
- **Regression Tasks:**
  - Price prediction
  - Value estimation
  - Anomaly detection

**Important Hyperparameters:**

- **k:** Number of nearest neighbors to consider
  - Critical parameter affecting model performance
  - Smaller values: More sensitive to noise
  - Larger values: More robust but may smooth out important patterns
- **sample_size:** Controls the size of the training data sample
  - Helps manage computational complexity
  - Affects model accuracy and training time

**Model Processing Pipeline:**

1. Data sampling and dimensionality reduction
   - Uses "sign" or "fjlt" methods
   - Helps avoid the "curse of dimensionality"
   - May introduce some noise but improves efficiency
2. Index building for neighbor lookup
3. Model serialization
4. Query processing for specified k value

**Instance Type Recommendations:**

- Supports both CPU and GPU instances
- GPU instances recommended for larger datasets
- Memory requirements depend on dataset size and k value

**Model Evaluation:**

- Classification: Accuracy metrics
- Regression: Mean Squared Error (MSE)
- Cross-validation recommended for optimal k selection

**Common Challenges + Best Practices:**

- **Feature Scaling:** Essential due to distance-based nature
- **Computational Efficiency:**
  - Uses FAISS library for efficient neighbor searches
  - Dimensionality reduction helps manage large datasets
- **Curse of Dimensionality:**
  - High-dimensional data can reduce effectiveness
  - Dimensionality reduction techniques help mitigate this


## Sources

- https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
