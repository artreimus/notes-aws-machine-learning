---
title: "Amazon Keyspaces (for Apache Cassandra)"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "draft"
domain:
  - "1.1"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "02_data_ingestion_and_storage"
aliases:
  - "Amazon Keyspaces (for Apache Cassandra)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Keyspaces (for Apache Cassandra)

## 1. Overview

Amazon Keyspaces is a managed, scalable database compatible with **Apache Cassandra** and the **Cassandra Query Language (CQL)**. It’s designed for high-throughput workloads using a **wide-column** data model.

**Where it fits in ML workflows**

- Store high-ingest event/sensor data that is naturally modeled as wide rows/partitions.
- Support fast lookup for time-ordered or entity-partitioned data used for feature generation.

---

## 2. Core Concepts

- **Keyspaces** contain **tables** (similar to Cassandra).
- Tables are modeled around **partition keys** and optional **clustering keys** for ordering within a partition.
- Like DynamoDB, good performance depends on **data modeling for access patterns** and avoiding hot partitions.

---

## 3. ML-Relevant Patterns

- Model by **entity + time window** (e.g., `device_id` as partition key, timestamp as clustering key) for efficient recent-history retrieval.
- Use batch/stream ingestion patterns (often via Kinesis, MSK, or app writers) then periodically export to S3 for training.

---

## 4. When to Choose Keyspaces vs DynamoDB

- Choose **Keyspaces** when you want Cassandra compatibility (CQL, wide-column patterns) or you’re migrating Cassandra workloads.
- Choose **DynamoDB** when your access patterns are primarily key/value or document lookups and you want tighter integration with DynamoDB-specific features (Streams, DAX, etc.).

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
