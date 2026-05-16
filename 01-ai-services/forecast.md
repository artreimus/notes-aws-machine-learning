---
title: "Amazon Forecast"
exam: "MLA-C01"
status: "legacy"
domain:
  - "2.1"
service:
  - "Amazon Forecast"
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "legacy"
  - "forecasting"
aliases:
  - "Amazon Forecast"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Forecast

## Exam Relevance

Legacy forecasting service note. Amazon Forecast is no longer available to new customers and is absent from the current MLA-C01 in-scope ML service list.

## When To Use

- Use only for historical context or existing customers.
- For current forecasting study, prefer SageMaker built-in algorithms such as DeepAR or custom time-series models.

## Core Concepts

- Forecast was a managed time-series forecasting service.
- New customers should use current alternatives.
- SageMaker DeepAR remains a key exam-relevant forecasting algorithm.

## AWS Services And Features

- Amazon Forecast
- Amazon SageMaker AI
- DeepAR

## Implementation Patterns

- Historical: time-series dataset -> Forecast predictor -> forecast.
- Current: time-series data -> DeepAR/SageMaker training or custom model -> endpoint/batch forecast.

## Tradeoffs And Pitfalls

- No new customers; avoid as a preferred current answer.
- Still useful to recognize old service wording.

## Exam Triggers

- Forecast service wording should trigger lifecycle caveat.
- DeepAR points to SageMaker built-in forecasting.

## Related Notes

- [[deep-ar]]
- [[model-selection-decision-guide]]


## Sources

- https://docs.aws.amazon.com/forecast/latest/dg/API_ListForecasts.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
