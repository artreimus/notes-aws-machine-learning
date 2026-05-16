---
title: "AWS Lambda For ML Workflows"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.1"
  - "3.3"
  - "4.1"
service:
  - "AWS Lambda"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "serverless"
aliases:
  - "AWS Lambda For ML Workflows"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Lambda For ML Workflows

## Knowledge Relevance

Compute service for event-driven orchestration glue, preprocessing, lightweight inference wrappers, and automation around ML workflows.

## When To Use

- Use for event-triggered preprocessing, routing, notification, and small integration tasks.
- Use to invoke SageMaker endpoints or start Step Functions, Glue, or Batch jobs.
- Use when automatic scaling and pay-per-use are more important than custom infrastructure.

## Core Concepts

- Lambda runs code without server management and scales automatically.
- Event sources can include S3, EventBridge, SQS, API Gateway, and streams.
- Functions use IAM execution roles and CloudWatch logs.

## AWS Services And Features

- AWS Lambda
- Amazon S3
- Amazon SQS
- Amazon EventBridge
- Amazon API Gateway
- AWS Step Functions

## Implementation Patterns

- S3 object created -> Lambda validates metadata -> starts SageMaker Pipeline.
- API Gateway -> Lambda -> SageMaker endpoint invocation.
- CloudWatch alarm -> SNS/EventBridge -> Lambda remediation.

## Tradeoffs And Pitfalls

- Lambda has runtime, package, memory, concurrency, and timeout constraints.
- Large training jobs belong in SageMaker Training, AWS Batch, EMR, or Glue, not Lambda.
- Use VPC configuration carefully because networking choices affect access and latency.

## Decision Triggers

- Small event-driven integration points to Lambda.
- Long-running ML training does not point to Lambda.
- Serverless API wrapper around endpoint often uses API Gateway plus Lambda.

## Related Notes

- [[api-gateway]]
- [[sqs]]
- [[step-functions]]
- [[sagemaker-pipelines]]


## Sources

- https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
