---
title: "AWS Config"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "4.3"
service:
  - "AWS Config"
tags:
  - "aws"
  - "mla-c01"
  - "domain-4"
  - "governance"
  - "compliance"
aliases:
  - "AWS Config"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Config

## Exam Relevance

Governance service for recording resource configuration history and evaluating compliance rules.

## When To Use

- Use to audit configuration history and relationships for AWS resources.
- Use Config rules to detect noncompliant resources.
- Use in multi-account governance with Organizations and aggregators.

## Core Concepts

- Configuration recorder captures supported resource configuration changes.
- Rules evaluate resource configuration against desired conditions.
- Snapshots/history support audit and troubleshooting.

## AWS Services And Features

- AWS Config
- AWS Organizations
- Amazon S3
- Amazon SNS

## Implementation Patterns

- Enable recorder -> store history/snapshots in S3 -> evaluate managed/custom rules -> notify via SNS/EventBridge.
- Organization aggregator -> central compliance view across accounts.

## Tradeoffs And Pitfalls

- Config is not a real-time metrics service.
- You need S3/SNS/IAM setup for recording and notifications.
- Not all resource types support every relationship or rule pattern.

## Exam Triggers

- Configuration drift, compliance rule, resource history, and audit evidence point to AWS Config.
- API call history points to CloudTrail.

## Related Notes

- [[cloudtrail]]
- [[organizations]]
- [[service-catalog]]


## Sources

- https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
