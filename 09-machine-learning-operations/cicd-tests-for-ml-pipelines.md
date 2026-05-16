---
title: "CI/CD Tests For ML Pipelines"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.2"
  - "3.3"
service:
  - "AWS CodePipeline"
  - "AWS CodeBuild"
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "cicd"
  - "testing"
aliases:
  - "CI/CD Tests For ML Pipelines"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# CI/CD Tests For ML Pipelines

## Knowledge Relevance

Testing strategy note for validating ML code, data contracts, pipelines, model artifacts, and deployments in CI/CD.

## When To Use

- Use unit tests for transforms and training utilities.
- Use data validation tests for schema and feature contracts.
- Use integration tests for pipelines, containers, permissions, and endpoints.
- Use smoke/canary tests before full rollout.

## Core Concepts

- ML CI/CD must test code, data, model behavior, infrastructure, and deployment safety.
- Different test stages belong in CodeBuild, SageMaker Pipelines, deployment guardrails, or monitoring workflows.

## AWS Services And Features

- AWS CodeBuild
- AWS CodePipeline
- SageMaker Pipelines
- SageMaker Model Registry

## Implementation Patterns

- Commit -> CodePipeline -> CodeBuild unit/data tests -> SageMaker pipeline -> model evaluation -> registry approval -> deployment guardrail.

## Tradeoffs And Pitfalls

- Model accuracy tests alone are insufficient.
- Non-determinism requires tolerances and seeded/reproducible runs where possible.
- Production deployment needs rollback and monitoring.

## Decision Triggers

- CI/CD tests, model approval, and pipeline validation point to MLOps testing.
- Shadow/canary wording points to deployment guardrails.

## Related Notes

- [[code-build]]
- [[code-pipeline]]
- [[sagemaker-pipelines]]
- [[deployment-guardrails-and-shadow-test]]


## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html
