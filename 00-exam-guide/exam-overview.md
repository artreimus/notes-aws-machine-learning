---
title: "MLA-C01 Exam Overview"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "all"
service:
  - "AWS Certification"
tags:
  - "aws"
  - "mla-c01"
  - "exam-guide"
aliases:
  - "MLA-C01 Exam Overview"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# MLA-C01 Exam Overview

## Knowledge Relevance

This is the top-level map for the AWS Certified Machine Learning Engineer - Associate exam.

## Current Exam Shape

| Domain | Weight | Local starting point |
| --- | ---: | --- |
| Domain 1: Data Preparation for Machine Learning | 28% | [[domain-1-data-preparation]] |
| Domain 2: ML Model Development | 26% | [[domain-2-model-development]] |
| Domain 3: Deployment and Orchestration of ML Workflows | 22% | [[domain-3-deployment-orchestration]] |
| Domain 4: ML Solution Monitoring, Maintenance, and Security | 24% | [[domain-4-monitoring-security]] |

## Study Flow

```mermaid
flowchart LR
    Overview["Exam overview"] --> D1["Domain 1 data prep"]
    Overview --> D2["Domain 2 model development"]
    Overview --> D3["Domain 3 deployment"]
    Overview --> D4["Domain 4 monitoring and security"]
    D1 --> Data["02 and 03 notes"]
    D2 --> SageMaker["05 and 06 notes"]
    D3 --> Ops["09 notes"]
    D4 --> Security["10 and 11 notes"]
    D2 --> Bedrock["13 Bedrock notes"]
```

## Scope Rules

- Prefer the official exam guide and official AWS service docs over third-party summaries.
- Treat services in AWS full shutdown or sunset as lifecycle caveats even if a service appears in a static certification service list.
- Keep supplemental notes, but do not let them crowd out current in-scope services.

## Related Notes

- [[in-scope-services]]
- [[out-of-scope-services]]
- [[study-roadmap]]

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-out-of-scope-services.html
