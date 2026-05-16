---
title: "Endpoint Autoscaling Metrics"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.1"
  - "4.2"
service:
  - "Amazon SageMaker AI"
  - "Application Auto Scaling"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "domain-4"
  - "autoscaling"
aliases:
  - "Endpoint Autoscaling Metrics"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Endpoint Autoscaling Metrics

## Knowledge Relevance

Operational note for choosing SageMaker endpoint scaling metrics and policies.

## When To Use

- Use invocations per instance or concurrency metrics for target tracking.
- Use latency and error metrics as health signals, not blindly as scaling triggers.
- Use scheduled scaling when traffic patterns are predictable.

## Core Concepts

- Endpoint variants are scalable targets.
- Target tracking aims to maintain a metric target.
- CloudWatch supplies endpoint metrics and alarms.

## AWS Services And Features

- Amazon SageMaker AI
- Application Auto Scaling
- Amazon CloudWatch

## Implementation Patterns

- Register endpoint variant as scalable target -> configure target tracking policy -> monitor latency/errors/cost.

## Tradeoffs And Pitfalls

- Scaling out cannot fix slow model code or insufficient instance memory.
- Aggressive scaling can increase cost without improving bottlenecks.
- Need load testing to set realistic targets.

## Decision Triggers

- Invocations per instance and target tracking point to endpoint autoscaling.
- Known traffic spike points to scheduled scaling.

## Related Notes

- [[aws-auto-scaling]]
- [[sagemaker-model-endpoints]]
- [[cloudwatch]]


## Sources

- https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
