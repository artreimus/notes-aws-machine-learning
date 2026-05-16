---
title: "Amazon API Gateway"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "3.1"
  - "3.2"
  - "4.3"
service:
  - "Amazon API Gateway"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "api"
aliases:
  - "Amazon API Gateway"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon API Gateway

## Exam Relevance

Managed service for creating and securing APIs in front of ML applications and inference workflows.

## When To Use

- Use to expose HTTP/REST/WebSocket APIs for inference applications.
- Use with Lambda as an integration layer before SageMaker endpoints.
- Use authorizers, throttling, stages, and logging for API governance.

## Core Concepts

- API Gateway creates, publishes, maintains, monitors, and secures APIs.
- Common ML path is API Gateway -> Lambda -> SageMaker endpoint.
- Use CloudWatch/X-Ray for API observability.

## AWS Services And Features

- Amazon API Gateway
- AWS Lambda
- Amazon SageMaker AI
- Amazon CloudWatch
- AWS X-Ray

## Implementation Patterns

- Client -> API Gateway -> Lambda -> SageMaker endpoint -> response.
- Private integration or VPC link patterns for internal services.

## Tradeoffs And Pitfalls

- API Gateway is not the model hosting layer.
- Throttling and payload limits matter for inference API design.
- Authentication/authorization must be explicit.

## Exam Triggers

- Secure public API front door points to API Gateway.
- Model hosting endpoint points to SageMaker endpoint.

## Related Notes

- [[lambda-for-ml-workflows]]
- [[sagemaker-model-endpoints]]
- [[x-ray]]


## Sources

- https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
