---
title: "Kinesis Data Analytics"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "supplemental"
domain:
  - "1.2"
  - "3.3"
service:
  - "Amazon Managed Service for Apache Flink"
tags:
  - "aws"
  - "mla-c01"
  - "stale-name"
  - "streaming"
aliases:
  - "Kinesis Data Analytics"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Kinesis Data Analytics

## Knowledge Relevance

Redirect-style note for a stale service name. Use [[managed-service-for-apache-flink]] as the canonical current note.

## When To Use

- Use this only to recognize old documentation or exam wording.
- Use Amazon Managed Service for Apache Flink for current service naming and implementation details.

## Core Concepts

- Amazon Kinesis Data Analytics was renamed to Amazon Managed Service for Apache Flink.
- Kinesis Data Analytics for SQL is in full shutdown as of January 27, 2026.
- Current stream processing study should use Managed Service for Apache Flink and Flink Studio naming.

## AWS Services And Features

- Amazon Managed Service for Apache Flink
- Managed Service for Apache Flink Studio

## Implementation Patterns

- Old reference -> map to current service name -> study [[managed-service-for-apache-flink]].

## Tradeoffs And Pitfalls

- Do not create new notes or diagrams that use Kinesis Data Analytics as the primary current name.
- Kinesis Data Analytics for SQL shutdown is distinct from current Managed Service for Apache Flink.

## Decision Triggers

- Kinesis Data Analytics wording points to Managed Service for Apache Flink.
- Kinesis Data Analytics for SQL points to shutdown/migration caveat.

## Related Notes

- [[managed-service-for-apache-flink]]
- [[kinesis-data-streams]]
- [[kinesis-data-firehose]]


## Sources

- https://aws.amazon.com/about-aws/whats-new/2023/08/amazon-managed-service-apache-flink/
- https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html
- https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html
