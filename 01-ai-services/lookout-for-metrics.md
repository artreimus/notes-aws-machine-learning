---
title: "Amazon Lookout For Metrics"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "legacy"
domain:
  - "2.1"
  - "4.1"
service:
  - "Amazon Lookout for Metrics"
tags:
  - "aws"
  - "mla-c01"
  - "ai-services"
  - "legacy"
aliases:
  - "Amazon Lookout For Metrics"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Lookout For Metrics

## Knowledge Relevance

Lifecycle-aware note: AWS General Reference lists Amazon Lookout for Metrics in full shutdown as of October 10, 2025.

## When To Use

- Use only to understand historical exam/service references.
- For current anomaly detection, prefer CloudWatch anomaly detection, SageMaker AI, or custom time-series models.

## Core Concepts

- Was an ML service for detecting anomalies in business and operational metrics.
- No longer available or supported in any capacity after full shutdown.

## AWS Services And Features

- Amazon Lookout for Metrics
- Amazon CloudWatch
- Amazon SageMaker AI

## Implementation Patterns

- Historical: metrics source -> detector -> anomaly alerts.
- Current: CloudWatch metric math/anomaly detection or SageMaker model for custom time-series monitoring.

## Tradeoffs And Pitfalls

- Full shutdown means it should not be selected as a current implementation choice.
- If an exam item uses it, read for legacy context and choose current alternatives when offered.

## Decision Triggers

- Metric anomaly detection with no-current-service caveat points away from Lookout for Metrics.
- CloudWatch anomaly detection or custom SageMaker time-series model is the current direction.

## Related Notes

- [[cloudwatch]]
- [[random-cut-forest]]
- [[concept-drift]]


## Sources

- https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html
- https://docs.aws.amazon.com/lookoutmetrics/latest/api/Welcome.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
