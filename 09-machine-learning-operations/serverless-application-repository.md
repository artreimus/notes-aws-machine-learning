---
title: "AWS Serverless Application Repository"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "3.1"
service:
  - "AWS Serverless Application Repository"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "serverless"
aliases:
  - "AWS Serverless Application Repository"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Serverless Application Repository

## Exam Relevance

In-scope compute-adjacent service for finding, deploying, and publishing packaged serverless applications.

## When To Use

- Use when teams need prebuilt or reusable serverless applications.
- Use with AWS SAM templates to publish or deploy Lambda-based apps.
- Use as low-priority exam context for serverless deployment options.

## Core Concepts

- Applications are packaged with AWS SAM templates.
- Apps can be published publicly or privately.
- The service is integrated with the Lambda console.

## AWS Services And Features

- AWS Serverless Application Repository
- AWS Lambda
- AWS SAM

## Implementation Patterns

- Find app -> configure parameters -> deploy serverless resources.
- Publish internal reusable processing app -> share privately across teams.

## Tradeoffs And Pitfalls

- This is not an ML model registry.
- Use SageMaker Model Registry for model versions and approval workflows.
- Security depends on reviewing app permissions and templates before deployment.

## Exam Triggers

- Prebuilt serverless app catalog points to Serverless Application Repository.
- Model package/version governance points to SageMaker Model Registry.

## Related Notes

- [[lambda-for-ml-workflows]]
- [[sagemaker-model-registry]]


## Sources

- https://docs.aws.amazon.com/serverlessrepo/latest/devguide/what-is-serverlessrepo.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
