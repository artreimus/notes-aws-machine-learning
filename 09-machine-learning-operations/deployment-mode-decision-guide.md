---
title: "Deployment Mode Decision Guide"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.1"
service:
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "deployment"
aliases:
  - "Deployment Mode Decision Guide"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Deployment Mode Decision Guide

## Knowledge Relevance

Decision guide for choosing real-time, async, batch, serverless, multi-model, and multi-container SageMaker deployment modes.

## When To Use

- Use real-time endpoints for low-latency synchronous inference.
- Use async inference for large payloads or longer processing with queued responses.
- Use batch transform for offline batch inference.
- Use serverless inference for intermittent traffic.
- Use multi-model endpoints for many related models with shared serving infrastructure.

## Core Concepts

- Deployment mode depends on latency, throughput, payload size, traffic shape, cost, and response pattern.
- Application Auto Scaling supports endpoint variants and inference components.
- CloudWatch metrics and Model Monitor support operations after deployment.

## AWS Services And Features

- SageMaker real-time endpoints
- SageMaker asynchronous inference
- SageMaker batch transform
- SageMaker serverless inference
- SageMaker multi-model endpoints

## Implementation Patterns

- Request/response API -> real-time endpoint.
- Large request with callback/polling -> async endpoint.
- Nightly scoring job -> batch transform.
- Low intermittent usage -> serverless inference.

## Tradeoffs And Pitfalls

- Keeping idle real-time endpoints can be expensive.
- Serverless cold starts may affect latency.
- Batch transform is not interactive.
- MLOps needs rollback, monitoring, and automation regardless of mode.

## Decision Triggers

- Low latency synchronous inference points to real-time endpoint.
- Large payload or long-running inference points to async inference.
- Offline scoring points to batch transform.

## Related Notes

- [[sagemaker-deployment-modes]]
- [[sagemaker-model-endpoints]]
- [[endpoint-autoscaling-metrics]]


## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html
