---
title: "SageMaker AI Current Capabilities"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "2.1"
  - "2.2"
  - "3.1"
  - "4.1"
service:
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "sagemaker"
  - "current"
aliases:
  - "SageMaker AI Current Capabilities"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SageMaker AI Current Capabilities

## Exam Relevance

Current landscape note for Amazon SageMaker AI versus next-generation SageMaker, Studio, and related ML lifecycle features.

## When To Use

- Use SageMaker AI for build/train/tune/deploy/monitor/govern classic ML and foundation model customization workflows.
- Use next-generation SageMaker context when docs mention Unified Studio, governance, and access to SageMaker AI.
- Use this note to normalize old `Amazon SageMaker` wording to current `Amazon SageMaker AI` where appropriate.

## Core Concepts

- SageMaker AI covers notebooks/Studio, processing, training, tuning, pipelines, feature store, registry, endpoints, monitor, clarify, and governance features.
- Next-generation SageMaker includes SageMaker Unified Studio, data/AI governance, and access to SageMaker AI.
- Studio Classic is legacy onboarding behavior; new domains use updated Studio.

## AWS Services And Features

- Amazon SageMaker AI
- SageMaker Studio
- SageMaker Unified Studio
- SageMaker Pipelines
- SageMaker Model Monitor

## Implementation Patterns

- Data -> processing/feature store -> training/tuning -> registry -> deployment -> monitoring/retraining.

## Tradeoffs And Pitfalls

- AWS docs now use updated naming; older notes may say SageMaker without AI.
- Do not confuse Studio, Studio Classic, and SageMaker Unified Studio.
- Lifecycle caveats apply to Training Compiler, Elastic Inference, and Edge Manager.

## Exam Triggers

- Build/train/deploy/monitor ML lifecycle points to SageMaker AI.
- Managed foundation model API points to Bedrock.
- Unified development/governance wording may point to next-generation SageMaker.

## Related Notes

- [[sagemaker-studio]]
- [[sagemaker-pipelines]]
- [[sagemaker-model-monitor]]
- [[amazon-bedrock]]


## Sources

- https://docs.aws.amazon.com/sagemaker/
- https://docs.aws.amazon.com/next-generation-sagemaker/latest/userguide/what-is-sagemaker.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html
