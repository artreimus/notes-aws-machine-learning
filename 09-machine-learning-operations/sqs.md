---
title: "Amazon SQS"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.3"
service:
  - "Amazon SQS"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "application-integration"
aliases:
  - "Amazon SQS"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon SQS

## Knowledge Relevance

Application integration service for durable queue-based decoupling in asynchronous ML workflows.

## When To Use

- Use when producers and consumers need to be decoupled.
- Use to buffer batch jobs, inference requests, or post-processing tasks.
- Use dead-letter queues for failures that require investigation.

## Core Concepts

- Standard queues provide at-least-once delivery and high throughput.
- FIFO queues support ordering and exactly-once processing semantics.
- Visibility timeout hides a message while a consumer processes it.

## AWS Services And Features

- Amazon SQS
- Amazon SNS
- AWS Lambda
- AWS KMS

## Implementation Patterns

- EventBridge or SNS -> SQS queue -> Lambda or container worker -> SageMaker endpoint/batch transform.
- Failed processing -> dead-letter queue -> operator review.

## Tradeoffs And Pitfalls

- At-least-once delivery means consumers should be idempotent.
- Visibility timeout must exceed normal processing time.
- SQS is pull-based; SNS is push/fanout.

## Decision Triggers

- Queue, visibility timeout, DLQ, and decoupling point to SQS.
- Multiple subscribers receiving the same event point to SNS fanout.

## Related Notes

- [[sns]]
- [[lambda-for-ml-workflows]]
- [[event-bridge]]


## Sources

- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
