---
title: "Amazon FSx"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "1.1"
  - "2.2"
service:
  - "Amazon FSx for Lustre"
tags:
  - "aws"
  - "mla-c01"
  - "storage"
  - "sagemaker"
aliases:
  - "Amazon FSx"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon FSx

## Exam Relevance

High-performance file system service; FSx for Lustre is especially relevant for ML/HPC training datasets that need fast POSIX file access.

## When To Use

- Use FSx for Lustre for high-throughput, low-latency file access during training.
- Use when training jobs need POSIX file semantics and fast reads over large datasets.
- Use S3 data repository integration to present S3 objects as files.

## Core Concepts

- FSx for Lustre is fully managed and POSIX-compliant.
- Designed for ML, HPC, video processing, and other speed-sensitive workloads.
- Can link to S3 repositories and write results back to S3.

## AWS Services And Features

- Amazon FSx for Lustre
- Amazon S3
- Amazon EC2
- Amazon ECS
- Amazon EKS
- Amazon SageMaker AI

## Implementation Patterns

- S3 training dataset -> FSx for Lustre linked file system -> SageMaker/EC2 training -> output back to S3.

## Tradeoffs And Pitfalls

- FSx is not object storage; S3 remains the durable data lake default.
- Scratch vs persistent deployment choices affect durability and cost.
- Choose storage class based on throughput/latency/cost needs.

## Exam Triggers

- High-performance POSIX training file system points to FSx for Lustre.
- Durable object data lake points to S3.

## Related Notes

- [[s3]]
- [[elastic-file-system]]
- [[sagemaker-input-modes]]


## Sources

- https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
