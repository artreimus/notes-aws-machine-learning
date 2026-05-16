---
title: "AWS Auto Scaling For ML Workloads"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.1"
  - "4.2"
service:
  - "Application Auto Scaling"
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "domain-4"
  - "autoscaling"
aliases:
  - "AWS Auto Scaling For ML Workloads"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Auto Scaling For ML Workloads

## Knowledge Relevance

Scaling note for SageMaker AI endpoints and supporting services using target tracking, step, scheduled, or predictive scaling patterns.

## When To Use

- Use Application Auto Scaling for SageMaker AI endpoint variants, inference components, and serverless provisioned concurrency.
- Use target tracking when a metric target such as invocations per instance should stay near a value.
- Use scheduled scaling for known traffic patterns.

## Core Concepts

- Application Auto Scaling supports resources beyond EC2 Auto Scaling groups.
- Scaling policies can be target tracking, step, scheduled, or predictive where supported.
- CloudWatch metrics drive most scaling decisions.

## AWS Services And Features

- Application Auto Scaling
- Amazon SageMaker AI
- Amazon CloudWatch

## Implementation Patterns

- Endpoint variant -> scalable target -> target tracking policy on invocation metric.
- Known traffic spike -> scheduled scaling before the event -> scale down afterward.

## Tradeoffs And Pitfalls

- Scaling policy cannot fix a poorly chosen model/container bottleneck by itself.
- Cold starts and provisioned concurrency matter for serverless inference.
- Cost and latency objectives must be balanced.

## Decision Triggers

- Endpoint variant autoscaling points to Application Auto Scaling.
- Metric-based scaling policy plus CloudWatch points to Application Auto Scaling.

## Related Notes

- [[endpoint-autoscaling-metrics]]
- [[sagemaker-model-endpoints]]
- [[cloudwatch]]


## Sources

- https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
