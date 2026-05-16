---
title: "Amazon DevOps Guru"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "4.1"
  - "4.2"
service:
  - "Amazon DevOps Guru"
tags:
  - "aws"
  - "mla-c01"
  - "domain-4"
  - "operations"
aliases:
  - "Amazon DevOps Guru"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon DevOps Guru

## Knowledge Relevance

In-scope ML-powered operations service for detecting abnormal operational behavior and producing recommendations.

## When To Use

- Use to identify operational issues and risks from metrics/events.
- Use for reactive and proactive insights about application health.
- Use as an operations signal alongside CloudWatch, X-Ray, and Trusted Advisor.

## Core Concepts

- Applies ML to operational data, application metrics, and events.
- Creates reactive insights for current issues and proactive insights for future risks.
- Provides recommendations to address detected operational problems.

## AWS Services And Features

- Amazon DevOps Guru
- Amazon CloudWatch
- AWS CloudFormation
- AWS Systems Manager

## Implementation Patterns

- Enable resource analysis coverage -> DevOps Guru analyzes telemetry -> insight and recommendation -> operator remediation.

## Tradeoffs And Pitfalls

- DevOps Guru improves operational diagnosis; it does not retrain ML models.
- Disable or scope coverage to avoid unwanted charges.
- Use Model Monitor/Clarify for model/data drift, not DevOps Guru.

## Decision Triggers

- Operational issue/risk with ML-generated recommendation points to DevOps Guru.
- Model drift or bias points to SageMaker Model Monitor or Clarify.

## Related Notes

- [[cloudwatch]]
- [[x-ray]]
- [[trusted-advisor]]


## Sources

- https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
