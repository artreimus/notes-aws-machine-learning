---
title: "Amazon Managed Service For Apache Flink"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "1.1"
  - "1.2"
  - "3.3"
service:
  - "Amazon Managed Service for Apache Flink"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "streaming"
  - "flink"
aliases:
  - "Amazon Managed Service For Apache Flink"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Managed Service For Apache Flink

## Knowledge Relevance

In-scope streaming analytics service for low-latency stream processing and stateful streaming transformations.

## When To Use

- Use for long-running streaming ETL and real-time analytics on Kinesis/MSK streams.
- Use Flink Studio for interactive stream queries and notebook-style exploration.
- Use when stateful processing, windows, checkpoints, snapshots, or stream joins matter.

## Core Concepts

- Supports Java, Scala, Python, and SQL depending on the Flink API.
- Provides managed provisioning, parallel computation, automatic scaling, AZ failover, checkpoints, and snapshots.
- This is the current name for the former Kinesis Data Analytics service family.

## AWS Services And Features

- Amazon Managed Service for Apache Flink
- Managed Service for Apache Flink Studio
- Kinesis Data Streams
- Amazon MSK

## Implementation Patterns

- Kinesis stream -> Flink application -> enriched stream, S3 sink, OpenSearch, or dashboard.
- Studio notebook -> interactive SQL/Python/Scala analysis -> optionally promote to a long-running application.

## Tradeoffs And Pitfalls

- Kinesis Data Analytics for SQL is in full shutdown; use Managed Service for Apache Flink or Flink Studio.
- Use Data Firehose for delivery/transformation when full stateful stream processing is unnecessary.
- DataStream API gives more control than SQL/Table API but requires more engineering ownership.

## Decision Triggers

- Stateful streaming ETL or real-time windows point to Flink.
- Ad hoc streaming SQL notebook points to Flink Studio.
- Simple delivery to S3/OpenSearch/Redshift points to Data Firehose.

## Related Notes

- [[kinesis-data-analytics]]
- [[kinesis-data-streams]]
- [[kinesis-data-firehose]]


## Sources

- https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html
- https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
