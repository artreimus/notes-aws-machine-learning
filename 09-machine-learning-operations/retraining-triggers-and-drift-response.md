---
title: "Retraining Triggers And Drift Response"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "4.1"
  - "3.3"
service:
  - "Amazon SageMaker AI"
  - "Amazon EventBridge"
tags:
  - "aws"
  - "mla-c01"
  - "domain-4"
  - "monitoring"
  - "drift"
aliases:
  - "Retraining Triggers And Drift Response"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Retraining Triggers And Drift Response

## Exam Relevance

Monitoring and maintenance note for responding to data drift, model quality drift, bias drift, and infrastructure signals.

## When To Use

- Trigger retraining from scheduled cadence, drift threshold breach, new labeled data, or business KPI degradation.
- Use EventBridge, Step Functions, and SageMaker Pipelines to automate response.
- Use human approval for high-risk model promotions.

## Core Concepts

- Data drift means input distribution changes.
- Model quality drift means prediction performance changes against labels.
- Bias drift means fairness metrics shift.
- Retraining should include validation and approval before deployment.

## AWS Services And Features

- SageMaker Model Monitor
- SageMaker Clarify
- Amazon EventBridge
- AWS Step Functions
- SageMaker Pipelines

## Implementation Patterns

- Model Monitor violation -> EventBridge -> Step Functions/SageMaker Pipeline -> retrain -> evaluate -> Model Registry approval -> deploy.

## Tradeoffs And Pitfalls

- Retraining without fresh labels may not improve model quality.
- Automated promotion can be risky in regulated workflows.
- Need baselines and thresholds before alerts are meaningful.

## Exam Triggers

- Drift threshold breach and automated retraining point to Model Monitor plus EventBridge/Pipelines.
- Bias drift points to Clarify.

## Related Notes

- [[sagemaker-model-monitor]]
- [[sagemaker-clarify]]
- [[sagemaker-pipelines]]


## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html
