---
title: "AWS Storage Gateway"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "1.1"
service:
  - "AWS Storage Gateway"
tags:
  - "aws"
  - "mla-c01"
  - "storage"
  - "hybrid"
aliases:
  - "AWS Storage Gateway"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Storage Gateway

## Exam Relevance

Hybrid storage service that connects on-premises environments to AWS storage for ingestion, backup, and migration patterns.

## When To Use

- Use when on-premises applications need low-latency local access with cloud-backed storage.
- Use file, volume, or tape gateway patterns depending on workload.
- Use for hybrid data ingestion and backup before analytics/ML processing in AWS.

## Core Concepts

- Runs as a VM, hardware appliance, or EC2-hosted gateway.
- Supports file-based, volume-based, and tape-based storage solutions.
- Volume Gateway can use cached or stored volume modes.

## AWS Services And Features

- AWS Storage Gateway
- Amazon S3
- Amazon FSx
- Amazon EBS snapshots

## Implementation Patterns

- On-prem application -> File/Volume Gateway -> AWS storage -> downstream data lake/ML workflow.

## Tradeoffs And Pitfalls

- Storage Gateway is for hybrid storage access, not stream processing.
- Gateway type choice changes latency, storage, and access semantics.
- Network reliability and data consistency need planning.

## Exam Triggers

- Hybrid on-prem to cloud storage bridge points to Storage Gateway.
- Bulk online transfer between storage systems points to DataSync.

## Related Notes

- [[datasync]]
- [[s3]]
- [[fsx]]


## Sources

- https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
