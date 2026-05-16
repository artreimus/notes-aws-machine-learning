---
title: "SageMaker Built-In Algorithms Cheat Sheet"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "2.1"
  - "2.2"
service:
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "domain-2"
  - "sagemaker"
  - "built-in-algorithms"
aliases:
  - "SageMaker Built-In Algorithms Cheat Sheet"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SageMaker Built-In Algorithms Cheat Sheet

## Exam Relevance

Use this as the first-stop decision table for SageMaker AI built-in algorithm questions.

## Algorithm Decision Table

| Data/problem type | Strong candidates | Notes |
| --- | --- | --- |
| Tabular classification/regression | [[xgboost]], [[light-gbm]], [[catboost]], [[autogluon-tabular]], [[tabtransformer]], [[linear-learner]] | Tree/boosting models are common defaults; AutoGluon is AutoML/ensembling; TabTransformer targets tabular categorical interactions |
| High-dimensional sparse features | [[factorization-machines]], [[linear-learner]] | Common for recommendation-like or sparse encoded features |
| Clustering | [[k-means]] | Unsupervised grouping |
| Anomaly detection | [[random-cut-forest]] | Streaming/time-series anomaly detection patterns |
| Dimensionality reduction | [[principal-component-analysis]] | Reduce feature dimensions before downstream modeling |
| Topic modeling | [[latent-dirichlet-allocation]], [[neural-topic-model]] | Organize documents into latent topics |
| Text classification | [[blazing-text]], [[text-classification-tensorflow]] | BlazingText is classic supervised/Word2Vec; TensorFlow version supports transfer learning |
| Time-series forecasting | [[deep-ar]] | Current exam-relevant replacement for old Forecast service emphasis |
| Image classification | [[image-classification]], [[image-classification-tensorflow]] | TensorFlow version supports transfer learning with pretrained models |
| Object detection | [[object-detection]], [[object-detection-tensorflow]] | MXNet and TensorFlow variants appear in SageMaker docs |
| Semantic segmentation | [[semantic-segmentation]] | Pixel-level image classification |
| Recommendation/embedding-like use cases | [[object2vec]], [[factorization-machines]] | Map inputs to dense embeddings or interaction scores |
| IP/entity behavior | [[ip-insights]] | Learn usage patterns for IPv4 addresses |

## Current Gaps Closed

- [[autogluon-tabular]]
- [[catboost]]
- [[tabtransformer]]
- [[text-classification-tensorflow]]
- [[image-classification-tensorflow]]
- [[object-detection-tensorflow]]

## Exam Triggers

- If the question says tabular classification/regression, compare XGBoost, LightGBM, CatBoost, AutoGluon, TabTransformer, and Linear Learner.
- If the question says text transfer learning, consider Text Classification - TensorFlow.
- If the question says image transfer learning, consider Image Classification - TensorFlow or Object Detection - TensorFlow.
- If the question says no labels and grouping, choose K-Means.
- If the question says time-series forecast in current SageMaker context, choose DeepAR rather than Amazon Forecast.

## Sources

- https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-tabular.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-tensorflow.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification-tensorflow.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tensorflow.html
