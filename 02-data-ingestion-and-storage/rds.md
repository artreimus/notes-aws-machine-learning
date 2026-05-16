---
title: "Amazon RDS (Relational Database Service)"
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
  - "Amazon RDS (Relational Database Service)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon RDS (Relational Database Service)

## 1. Overview

Amazon RDS is a managed service for running relational database engines. RDS handles common operational tasks like provisioning, patching, backups, monitoring, and (engine-dependent) replication.

**Where it fits in ML workflows**

- Common **system of record** for business entities and transactions used to build labels/features.
- Often used as an **upstream source** feeding S3/Redshift for analytics and training datasets.

---

## 2. Supported Engines (High-Level)

RDS supports multiple database engines (availability varies by region), such as:

- **PostgreSQL**
- **MySQL**
- **MariaDB**
- **Oracle**
- **SQL Server**

If you only need MySQL/PostgreSQL and want Aurora’s performance/HA characteristics, compare against **Amazon Aurora**.

---

## 3. ML-Relevant Patterns

- Prefer **read replicas** (where supported) for feature extraction queries so you don’t overload OLTP traffic.
- Use scheduled exports/ETL (Glue, DMS, custom jobs) to land data in **S3** for reproducible training sets.
- Combine with **Secrets Manager** for credential storage/rotation for pipelines and apps.

---

## 4. Operations & Availability

- **Multi-AZ** deployments improve availability via synchronous replication and managed failover.
- **Backups** include automated backups (with a retention window) and manual snapshots.
- Monitor with **CloudWatch**; use Performance Insights where available for query-level visibility.

---

## 5. When to Choose RDS vs DynamoDB

- Choose **RDS** when you need **SQL**, joins, constraints, complex queries/aggregations, or strong relational modeling.
- Choose **DynamoDB** when you need **very low-latency key-based access** at high scale with flexible schema and predictable access patterns.

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
