---
title: "AWS CodeArtifact"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "3.2"
  - "3.3"
service:
  - "AWS CodeArtifact"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "developer-tools"
aliases:
  - "AWS CodeArtifact"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS CodeArtifact

## Exam Relevance

Managed artifact repository for software packages used by ML application and pipeline builds.

## When To Use

- Use to store private Python, npm, Maven, NuGet, or other supported packages.
- Use to proxy public repositories and reduce dependency availability risk.
- Use in CodeBuild/CodePipeline workflows for controlled dependency retrieval.

## Core Concepts

- Domains contain repositories.
- Repositories store packages and can use upstream repositories and external connections.
- Authentication tokens are required; packages cannot be made publicly available from CodeArtifact.

## AWS Services And Features

- AWS CodeArtifact
- AWS CodeBuild
- AWS CodePipeline
- IAM

## Implementation Patterns

- Private ML preprocessing package -> CodeArtifact -> CodeBuild training image build.
- Proxy PyPI/npm through CodeArtifact for reproducible CI/CD dependencies.

## Tradeoffs And Pitfalls

- CodeArtifact is for software packages, not model artifacts.
- Repository permissions and token lifetime affect CI/CD reliability.
- Pin package versions for reproducible ML pipelines.

## Exam Triggers

- Package dependency repository points to CodeArtifact.
- Model artifact registry points to SageMaker Model Registry or S3.

## Related Notes

- [[code-build]]
- [[code-pipeline]]
- [[sagemaker-model-registry]]


## Sources

- https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
