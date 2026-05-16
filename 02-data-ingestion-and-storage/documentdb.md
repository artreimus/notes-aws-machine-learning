---
title: "Amazon DocumentDB (with MongoDB compatibility)"
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
  - "Amazon DocumentDB (with MongoDB compatibility)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon DocumentDB (with MongoDB compatibility)

## 1. Overview

Amazon DocumentDB is a managed document database service designed to be **MongoDB API compatible**. It’s commonly used for applications built around **JSON-like documents**, flexible schemas, and rich document queries.

**Where it fits in ML workflows**

- Store semi-structured operational data (catalogs, content, app events) that may later be exported to S3/Redshift for training.
- Serve application state or metadata used to enrich inference requests (often with caching).

---

## 2. Core Concepts

- **Documents** (JSON/BSON-like) grouped into **collections**.
- Indexes support query patterns across document fields.
- Schema is flexible, but you should still enforce consistency at the application layer when possible.

---

## 3. Scaling, Availability, and Storage

- Designed for **high availability** via replication across multiple AZs.
- Storage is separated from compute and scales to support growing datasets.

**Practical pattern:** scale reads via replicas; scale writes by choosing appropriate instance sizes and write patterns.

---

## 4. Operations & Administration (Managed)

- Automated backups, patching, monitoring, and recovery features.
- Integrates with common AWS operational tooling (CloudWatch metrics/logs, IAM/VPC controls).

---

## 5. Security

- Encryption at rest (KMS) and in transit (TLS).
- Network isolation via VPC security groups and subnets.
- IAM-integrated access patterns (service-level) plus database authentication/authorization models.

---

## 6. Practical Considerations

- DocumentDB targets **MongoDB compatibility**, but feature parity and version support can differ from upstream MongoDB.
- You still need to design indexes around query patterns to avoid slow collection scans.
- For analytics/ML, the common approach is to **export** or **ETL** data into S3/Redshift rather than running heavy scans on the operational store.

---

## 7. When to Choose DocumentDB vs DynamoDB

- **Choose DocumentDB** when:
  - You need **MongoDB-style queries** over nested documents and existing MongoDB-compatible tooling.
  - You want a managed document store with familiar MongoDB APIs.
- **Choose DynamoDB** when:
  - You need **serverless**, massive scale, and predictable key-based access with very low latency.
  - Your access patterns can be modeled with partition/sort keys and indexes.

---

## 8. ML-Relevant Integration Notes

- Often used as an **operational store**; ML training typically pulls data into S3 (via ETL/ELT) and then into analytics stores (Athena/Redshift) or feature pipelines (Glue/SageMaker).
- Consider exporting snapshots or CDC-style patterns to a lake for reproducible training datasets.

---

## 9. Exam/Interview Callouts

- DocumentDB emphasizes **MongoDB API compatibility**; it’s not “MongoDB hosted by AWS” in every internal detail.
- Use it for document-centric workloads and existing MongoDB ecosystems; use DynamoDB for serverless key-value access at scale.

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
