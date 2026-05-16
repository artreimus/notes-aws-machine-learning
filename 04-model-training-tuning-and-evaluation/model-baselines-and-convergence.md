---
title: "Model Baselines And Convergence"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "2.2"
  - "2.3"
service:
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "domain-2"
  - "model-evaluation"
aliases:
  - "Model Baselines And Convergence"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Model Baselines And Convergence

## Knowledge Relevance

Model development concept note for comparing models to baselines and detecting convergence or non-convergence during training/tuning.

## When To Use

- Use a baseline to verify that a model beats simple heuristics or prior models.
- Use learning curves to identify underfitting, overfitting, or training instability.
- Use early stopping when validation metrics stop improving.

## Core Concepts

- Baseline can be naive rule, majority class, previous production model, or simple algorithm.
- Convergence means objective/metric changes become small or stable.
- Non-convergence can come from learning rate, data scaling, bad features, or insufficient training.

## AWS Services And Features

- Amazon SageMaker AI
- Automatic Model Tuning
- SageMaker Experiments

## Implementation Patterns

- Train baseline -> train candidate -> compare validation/test metric -> inspect learning curves -> tune or stop.

## Tradeoffs And Pitfalls

- A complex model that does not beat a baseline is not ready.
- Training loss improving while validation worsens suggests overfitting.
- Unstable loss can indicate learning-rate or data quality issues.

## Decision Triggers

- Baseline comparison and convergence detected point to Domain 2 performance analysis.
- Early stopping/tuning objective point to AMT.

## Related Notes

- [[model-metrics]]
- [[automatic-model-tuning-and-hyperparameter-tuning]]
- [[preventing-overfitting]]


## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html
