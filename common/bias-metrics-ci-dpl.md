---
title: "Bias Metrics: CI And DPL"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "1.3"
  - "4.1"
service:
  - "Amazon SageMaker Clarify"
tags:
  - "aws"
  - "mla-c01"
  - "bias"
  - "clarify"
aliases:
  - "Bias Metrics: CI And DPL"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Bias Metrics: CI And DPL

## Exam Relevance

Focused note on SageMaker Clarify Class Imbalance (CI) and Difference in Proportions of Labels (DPL) metrics.

## When To Use

- Use CI to measure imbalance in member counts between facet values.
- Use DPL to measure imbalance of positive outcome proportions across facets.
- Use before training to detect raw data bias.

## Core Concepts

- Facet is a column/attribute used for bias measurement.
- CI asks whether one facet has more samples than another.
- DPL asks whether one facet has a higher positive label proportion.

## AWS Services And Features

- Amazon SageMaker Clarify

## Implementation Patterns

- Select facet and label -> run Clarify pre-training bias analysis -> review CI/DPL -> mitigate before training.

## Tradeoffs And Pitfalls

- Metrics are model-agnostic before training; they do not prove legal fairness.
- Interpretation depends on the application and definition of positive outcome.
- Bias mitigation should involve product, policy, legal, and domain stakeholders.

## Exam Triggers

- CI means class/facet imbalance.
- DPL means difference in positive label proportions.
- Pre-training bias metric wording points to Clarify.

## Related Notes

- [[sagemaker-clarify]]
- [[class-imbalance-and-resampling]]
- [[conditional-demographic-disparity]]


## Sources

- https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-data-bias.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-data-bias.html
