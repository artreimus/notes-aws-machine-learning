---
title: "AutoGluon-Tabular"
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
  - "built-in-algorithm"
aliases:
  - "AutoGluon-Tabular"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AutoGluon-Tabular

## Exam Relevance

SageMaker AI built-in tabular AutoML algorithm for classification, regression, and ranking.

## When To Use

- Use when the data/task matches the algorithm family and a managed SageMaker built-in container is preferred.
- Use to avoid maintaining custom training code when built-in input formats and hyperparameters fit.

## Core Concepts

- AutoGluon-Tabular ensembles and stacks multiple model types, handles varied data types, supports CSV, and expects target values in the first column for CSV training.
- Check required input channels, content types, and instance recommendations before training.
- Compare against XGBoost/LightGBM/Linear Learner or custom training depending on task and constraints.

## AWS Services And Features

- Amazon SageMaker AI built-in algorithms
- SageMaker Training
- SageMaker Automatic Model Tuning

## Implementation Patterns

- S3 training data -> built-in algorithm container -> training job -> model artifact -> endpoint or batch transform.

## Tradeoffs And Pitfalls

- Built-in algorithms still require correct input format and feature engineering.
- Use the algorithm cheat sheet to avoid choosing image/text/tabular algorithms interchangeably.
- Not every algorithm is parallelizable or GPU-appropriate.

## Exam Triggers

- Managed built-in algorithm with matching data type points to SageMaker AI.
- Need full architecture control points to custom training.

## Related Notes

- [[sagemaker-built-in-algorithms-cheat-sheet]]
- [[model-selection-decision-guide]]


## Sources

- https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-tabular.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/InputOutput-AutoGluon-Tabular.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
