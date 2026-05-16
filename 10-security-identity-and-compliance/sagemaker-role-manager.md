---
title: "Amazon SageMaker Role Manager"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "4.3"
service:
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "domain-4"
  - "security"
  - "iam"
aliases:
  - "Amazon SageMaker Role Manager"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon SageMaker Role Manager

## Knowledge Relevance

SageMaker feature for creating persona-based IAM roles with least-privilege permissions for ML activities.

## When To Use

- Use when creating SageMaker execution roles for common ML personas and activities.
- Use to reduce over-permissive IAM roles in SageMaker environments.
- Use with least privilege, VPC, KMS, S3, and service-specific policies.

## Core Concepts

- Role Manager helps generate IAM roles for SageMaker personas.
- Activities define access to resources such as training, processing, notebooks, pipelines, and model registry.
- The generated role still needs review against organizational policy.

## AWS Services And Features

- Amazon SageMaker Role Manager
- IAM
- Amazon S3
- AWS KMS

## Implementation Patterns

- Choose persona/activity -> Role Manager generates role -> review permissions -> attach to SageMaker user/job/domain.

## Tradeoffs And Pitfalls

- Generated roles are a starting point, not a substitute for security review.
- Least privilege requires narrowing data buckets, KMS keys, and network access.
- Separate user roles from execution roles.

## Decision Triggers

- SageMaker persona-based IAM role creation points to Role Manager.
- Generic cross-account governance points to IAM/Organizations/SCPs.

## Related Notes

- [[IAM]]
- [[sagemaker-domains]]
- [[private-ml-networking]]


## Sources

- https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
