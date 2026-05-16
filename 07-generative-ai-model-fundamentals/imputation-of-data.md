---
title: "Imputation Of Data"
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
  - "07_generative_ai_model_fundamentals"
aliases:
  - "Imputation Of Data"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Imputation Of Data

Imputing missing data means **filling in the blanks** in a dataset where some values are missing.

Instead of deleting incomplete rows or columns, imputation replaces missing values with _estimated_ ones, based on the rest of the data. This helps keep as much information as possible and improves the accuracy of models.

### Common imputation methods:

1. **Mean/Median/Mode Imputation**: Fill missing values with the column’s average (mean), middle value (median), or most common value (mode).
2. **Forward/Backward Fill**: Use the previous or next value to fill in the missing one (often used with time series).
3. **K-Nearest Neighbors (KNN)**: Estimate the missing value based on similar (nearest) data points.
4. **Regression Imputation**: Predict the missing value using a regression model built from the other variables.
5. **Multivariate Imputation (e.g. MICE)**: Iteratively predict missing values using multiple models.

Want a quick code example in Python or help choosing the right method for your data?


## Sources

- https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
