---
title: "AWS Compute Optimizer"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "4.2"
service:
  - "AWS Compute Optimizer"
tags:
  - "aws"
  - "mla-c01"
  - "domain-4"
  - "cost-optimization"
aliases:
  - "AWS Compute Optimizer"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Compute Optimizer

## Knowledge Relevance

Cost/performance optimization service for rightsizing supported AWS compute resources.

## When To Use

- Use for rightsizing recommendations and resource optimization.
- Use with cost reviews for EC2, Auto Scaling groups, EBS, Lambda, ECS/Fargate, and other supported resources.
- Use alongside Cost Explorer and Trusted Advisor.

## Core Concepts

- Analyzes resource configuration and utilization metrics.
- Produces recommendations for over-provisioned or under-provisioned resources.
- Helps balance cost and performance.

## AWS Services And Features

- AWS Compute Optimizer
- Amazon CloudWatch
- AWS Cost Management

## Implementation Patterns

- Enable Compute Optimizer -> collect metrics -> review recommendations -> resize resource or adjust scaling.

## Tradeoffs And Pitfalls

- Recommendations are only as good as the observed metric history and supported resource types.
- SageMaker endpoint-specific autoscaling still uses SageMaker/Application Auto Scaling decisions.

## Decision Triggers

- Rightsizing compute resources points to Compute Optimizer.
- Broad support-plan check categories point to Trusted Advisor.

## Related Notes

- [[aws-cost-management-for-ml]]
- [[trusted-advisor]]
- [[aws-auto-scaling]]


## Sources

- https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
