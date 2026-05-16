---
title: "Amazon Q Developer In Chat Applications"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "4.1"
  - "4.2"
service:
  - "Amazon Q Developer in chat applications"
tags:
  - "aws"
  - "mla-c01"
  - "domain-4"
  - "chatops"
aliases:
  - "Amazon Q Developer In Chat Applications"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Q Developer In Chat Applications

## Exam Relevance

Current name for AWS Chatbot: ChatOps service for receiving AWS notifications and running AWS CLI commands from chat channels.

## When To Use

- Use for operational notifications in Slack, Microsoft Teams, or Amazon Chime.
- Use when teams need to respond to CloudWatch alarms, budgets, or security events from chat.
- Use with SNS topics as notification sources.

## Core Concepts

- AWS Chatbot is now Amazon Q Developer in chat applications.
- Uses SNS topics to forward events and alarms to chat channels.
- Supports IAM permission templates, guardrails, custom actions, and AWS CLI commands.

## AWS Services And Features

- Amazon Q Developer in chat applications
- Amazon SNS
- Amazon CloudWatch
- AWS Budgets

## Implementation Patterns

- CloudWatch alarm -> SNS topic -> Q Developer chat channel notification.
- Budget threshold -> SNS -> chat notification -> operator command/action.

## Tradeoffs And Pitfalls

- Channel IAM role and guardrail policies control command permissions.
- ChatOps does not replace incident management or observability data.
- Use SNS for the notification fanout layer.

## Exam Triggers

- AWS Chatbot wording should map to Amazon Q Developer in chat applications.
- Notifications from SNS to Slack/Teams point here.

## Related Notes

- [[amazon-q]]
- [[sns]]
- [[cloudwatch]]


## Sources

- https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
