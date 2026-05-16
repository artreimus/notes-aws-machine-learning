---
title: "Amazon Timestream"
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
  - "Amazon Timestream"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Timestream

## 1. Overview

Amazon Timestream is a managed **time-series database** optimized for data indexed by time (metrics, telemetry, events). It’s designed to make time-window queries and time-based retention straightforward.

**Where it fits in ML workflows**

- Store high-volume telemetry for feature engineering (rolling windows, aggregates, anomaly signals).
- Support near real-time dashboards/monitoring that can feed ML triggers or retraining signals.

---

## 2. Core Concepts

- Time-series data is typically modeled with:
  - **Dimensions** (who/what generated the data: device, user, region)
  - **Measures** (the values: temperature, latency, count)
  - **Timestamps** (when the measure happened)
- Time-series querying commonly relies on **time filtering** plus grouping/aggregation over windows.

---

## 3. ML-Relevant Patterns

- Compute rolling aggregates (e.g., last 5 minutes / last 24 hours) for anomaly detection or dynamic thresholds.
- Periodically export or replicate data to **S3** for training set construction and reproducibility.

---

## 4. When to Choose Timestream vs DynamoDB

- Choose **Timestream** when time-window queries, downsampling/aggregation, and time-based retention are primary requirements.
- Choose **DynamoDB** for general-purpose key-value/document access and predictable key-based query patterns (often with time bucketing + TTL as a lightweight alternative).

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
