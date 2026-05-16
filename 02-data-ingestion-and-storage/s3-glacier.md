---
title: "Amazon S3 Glacier Storage Classes"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "1.1"
  - "4.2"
service:
  - "Amazon S3 Glacier storage classes"
tags:
  - "aws"
  - "mla-c01"
  - "storage"
  - "lifecycle"
aliases:
  - "Amazon S3 Glacier Storage Classes"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon S3 Glacier Storage Classes

## Exam Relevance

Archive storage note focused on current S3 Glacier storage classes, not the legacy standalone Amazon Glacier vault API.

## When To Use

- Use S3 Glacier Instant Retrieval, Flexible Retrieval, or Deep Archive for low-cost archival storage.
- Use lifecycle policies to move old data to colder storage.
- Use when access latency requirements tolerate archival retrieval behavior.

## Core Concepts

- S3 Glacier storage classes are part of Amazon S3.
- Standalone Amazon Glacier vault service no longer accepts new customers.
- Lifecycle rules automate transitions between S3 storage classes.

## AWS Services And Features

- Amazon S3
- Amazon S3 Glacier Instant Retrieval
- Amazon S3 Glacier Flexible Retrieval
- Amazon S3 Glacier Deep Archive

## Implementation Patterns

- Raw training data in S3 Standard -> lifecycle transition to S3 Glacier after retention window.
- Compliance/archive dataset -> Deep Archive with retrieval planning.

## Tradeoffs And Pitfalls

- Do not confuse current S3 Glacier storage classes with standalone Amazon Glacier vault APIs.
- Retrieval time and retrieval cost matter.
- Archived data is usually not suitable for immediate training without restoration.

## Exam Triggers

- Low-cost long-term archive points to S3 Glacier storage classes.
- Fast active training data points to S3 Standard/EFS/FSx depending on access pattern.

## Related Notes

- [[s3]]
- [[storage-gateway]]
- [[fsx]]


## Sources

- https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
