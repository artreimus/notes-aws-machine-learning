---
title: "Class Imbalance And Resampling"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "1.3"
  - "2.3"
service:
  - "Amazon SageMaker Clarify"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "ml-concepts"
  - "bias"
aliases:
  - "Class Imbalance And Resampling"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Class Imbalance And Resampling

## Knowledge Relevance

Domain 1/2 concept note for imbalanced labels, sampling strategies, and the SageMaker Clarify Class Imbalance bias metric.

## When To Use

- Use when one class is underrepresented and accuracy may hide poor minority-class performance.
- Use resampling, class weights, threshold tuning, or anomaly detection framing depending on the problem.
- Use Clarify CI when measuring facet imbalance for bias/fairness.

## Core Concepts

- Class imbalance affects metrics, training dynamics, and fairness.
- Oversampling duplicates/synthesizes minority examples; undersampling reduces majority examples.
- Clarify Class Imbalance ranges from -1 to +1 for facet representation imbalance.

## AWS Services And Features

- Amazon SageMaker Clarify
- SageMaker Training
- SageMaker Model Monitor

## Implementation Patterns

- Stratified split -> train with class weights or resampling -> evaluate precision/recall/F1/AUC-PR -> monitor minority-class performance.

## Tradeoffs And Pitfalls

- Accuracy is misleading under severe imbalance.
- Oversampling can overfit; undersampling can discard information.
- Choose the metric that matches false-positive/false-negative cost.

## Decision Triggers

- Rare positive class, skewed labels, or minority recall points to imbalance handling.
- Facet representation imbalance points to Clarify Class Imbalance.

## Related Notes

- [[bias-metrics-ci-dpl]]
- [[model-metrics]]
- [[sagemaker-clarify]]


## Sources

- https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-data-bias.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
