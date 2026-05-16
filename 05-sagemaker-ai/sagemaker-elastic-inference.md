---
title: "SageMaker Elastic Inference"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "legacy"
domain:
  - "3.1"
service:
  - "Amazon SageMaker AI"
  - "Amazon Elastic Inference"
tags:
  - "aws"
  - "mla-c01"
  - "legacy"
  - "inference"
aliases:
  - "SageMaker Elastic Inference"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SageMaker Elastic Inference

## Knowledge Relevance

Legacy inference acceleration note. AWS stopped onboarding new Elastic Inference customers after April 15, 2023.

## When To Use

- Use only for existing Elastic Inference environments.
- For current endpoint cost/performance decisions, use instance selection, accelerator instances, serverless/async/batch modes, and Inference Recommender.

## Core Concepts

- Elastic Inference let customers attach fractional GPU acceleration to endpoints in older patterns.
- The current study emphasis should be SageMaker Inference Recommender, endpoint modes, Application Auto Scaling, and modern accelerator instances.

## AWS Services And Features

- Amazon Elastic Inference
- Amazon SageMaker AI
- SageMaker Inference Recommender

## Implementation Patterns

- Historical: endpoint + EI accelerator.
- Current: benchmark with Inference Recommender -> choose endpoint instance/mode -> autoscale.

## Tradeoffs And Pitfalls

- No new customer onboarding after April 15, 2023.
- Do not select EI for greenfield current architecture questions.

## Decision Triggers

- Elastic Inference wording should trigger legacy caveat.
- Cost/performance endpoint recommendation points to Inference Recommender.

## Related Notes

- [[sagemaker-inference-recommender]]
- [[deployment-mode-decision-guide]]
- [[endpoint-autoscaling-metrics]]


## Sources

- https://docs.aws.amazon.com/sdk-for-go/api/service/elasticinference/
- https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html
