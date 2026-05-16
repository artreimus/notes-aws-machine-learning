---
title: "Amazon CodeGuru"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.3"
  - "4.1"
service:
  - "Amazon CodeGuru"
tags:
  - "aws"
  - "mla-c01"
  - "developer-tools"
  - "operations"
aliases:
  - "Amazon CodeGuru"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon CodeGuru

## Knowledge Relevance

In-scope ML-powered developer/operations tooling for code review, security finding, and application performance insight context.

## When To Use

- Use CodeGuru Reviewer/Security context for code recommendations and vulnerability/secrets detection.
- Use CodeGuru Profiler context for identifying expensive or slow code paths.
- Use as developer-tooling context, not as an ML modeling service.

## Core Concepts

- CodeGuru uses machine learning and automated reasoning to help improve code quality and performance.
- Profiler highlights expensive lines and runtime behavior.
- Reviewer/Security analyze code for defects, security concerns, and secrets.

## AWS Services And Features

- Amazon CodeGuru Reviewer
- Amazon CodeGuru Profiler
- Amazon CodeGuru Security

## Implementation Patterns

- Repository association -> code review findings -> remediation.
- Runtime profiling group -> performance insights -> optimize hot paths.

## Tradeoffs And Pitfalls

- CodeGuru is not a replacement for unit tests, static analysis policy, or runtime monitoring.
- For request tracing, use X-Ray; for application metrics, use CloudWatch.

## Decision Triggers

- ML-powered code review/profiling points to CodeGuru.
- Distributed request trace map points to X-Ray.

## Related Notes

- [[x-ray]]
- [[code-build]]
- [[code-pipeline]]


## Sources

- https://aws.amazon.com/documentation-overview/codeguru/
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
