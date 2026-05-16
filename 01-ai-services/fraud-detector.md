---
title: "Amazon Fraud Detector"
exam: "MLA-C01"
status: "legacy"
domain:
  - "2.1"
service:
  - "Amazon Fraud Detector"
tags:
  - "aws"
  - "mla-c01"
  - "ai-services"
  - "legacy"
aliases:
  - "Amazon Fraud Detector"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Fraud Detector

## Exam Relevance

Lifecycle-aware service note: Amazon Fraud Detector appears in MLA-C01 service scope, but AWS says it is no longer open to new customers and is in sunset status.

## When To Use

- Use only for existing Fraud Detector environments.
- For new fraud detection designs, prefer SageMaker AI, AutoGluon, feature engineering, and AWS WAF depending on the pattern.
- Study as a historical high-level AI service, not as a preferred current build path.

## Core Concepts

- Managed fraud detection service using ML plus rules/outcomes.
- Evaluates online fraud scenarios such as payment fraud and fake account creation.
- Sunset status means migration planning matters.

## AWS Services And Features

- Amazon Fraud Detector
- Amazon SageMaker AI
- AutoGluon
- AWS WAF

## Implementation Patterns

- Existing Fraud Detector detector -> fraud score -> decision logic -> outcome.
- Replacement path: feature store/training data -> SageMaker model -> real-time endpoint -> application rule layer.

## Tradeoffs And Pitfalls

- No new customers as of November 7, 2025.
- AWS General Reference lists an end-of-support date of October 7, 2026.
- Avoid selecting it as a greenfield answer when a current alternative fits.

## Exam Triggers

- Fraud detection managed service with lifecycle caveat points to Fraud Detector.
- Greenfield custom fraud model points to SageMaker AI or AutoGluon.

## Related Notes

- [[sagemaker-feature-store]]
- [[autogluon-tabular]]
- [[xgboost]]


## Sources

- https://docs.aws.amazon.com/frauddetector/latest/ug/what-is-frauddetector.html
- https://docs.aws.amazon.com/general/latest/gr/sunset_services.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
