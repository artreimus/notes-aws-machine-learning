---
title: "Amazon SNS"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.3"
  - "4.1"
service:
  - "Amazon SNS"
tags:
  - "aws"
  - "mla-c01"
  - "domain-3"
  - "application-integration"
aliases:
  - "Amazon SNS"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon SNS

## Knowledge Relevance

Application integration service for pub/sub notifications and fanout in ML workflows.

## When To Use

- Use to publish one event to multiple subscribers.
- Use for alarms, notifications, and fanout to SQS, Lambda, HTTP endpoints, email, or Firehose.
- Use with CloudWatch alarms or EventBridge workflows for operational notification.

## Core Concepts

- Topics are logical channels for publishers.
- Subscriptions deliver topic messages to endpoint types.
- Fanout copies one event to multiple processing paths.

## AWS Services And Features

- Amazon SNS
- Amazon SQS
- AWS Lambda
- Amazon Data Firehose
- Amazon CloudWatch

## Implementation Patterns

- Training failure alarm -> SNS topic -> email/Slack/Lambda remediation.
- New prediction object -> SNS topic -> multiple SQS queues for independent downstream processing.

## Tradeoffs And Pitfalls

- SNS is pub/sub, not a durable work queue by itself.
- Use SQS subscriptions when subscribers need buffering and retries.
- Avoid sending sensitive production data to test subscribers without controls.

## Decision Triggers

- Fanout to multiple consumers points to SNS.
- Durable decoupled queue with visibility timeout points to SQS.
- Operational notification from an alarm often uses SNS.

## Related Notes

- [[sqs]]
- [[event-bridge]]
- [[cloudwatch]]


## Sources

- https://docs.aws.amazon.com/sns/latest/dg/welcome.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
