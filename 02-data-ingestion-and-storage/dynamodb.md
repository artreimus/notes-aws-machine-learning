# Amazon DynamoDB

## 1. Overview

Amazon DynamoDB is a fully managed, serverless NoSQL database that supports **key-value** and **document** data models. It provides **single-digit millisecond** latency at scale, with built-in high availability and durability across multiple AZs.

**Where it fits in ML workflows**

- Store **online features** / low-latency lookup data (user profiles, counters, embeddings metadata).
- Power **real-time inference** enrichment (feature retrieval by key).
- Ingest high-velocity event data (often via Kinesis/Lambda) for near real-time pipelines.

---

## 2. Data Model & Core Concepts

- **Items** live in a **table**; items have **attributes** (schema-flexible).
- Each table has a **primary key**:
  - **Partition key** (required): determines distribution.
  - **Sort key** (optional): enables range queries and grouping within a partition.
- **Secondary indexes** for alternate access patterns:
  - **GSI (Global Secondary Index)**: different partition/sort keys; eventually consistent reads only.
  - **LSI (Local Secondary Index)**: same partition key, different sort key; must be defined at table creation.

**Design tip:** model access patterns first; avoid scans; choose keys that spread load and support queries.

---

## 3. Reads/Writes, Consistency, and Performance

- **Read consistency**
  - **Eventually consistent** (default): higher throughput, lower cost.
  - **Strongly consistent**: only for base table reads (not for GSIs).
- **Access patterns**
  - **Query** is the default for key-based reads (efficient).
  - **Scan** reads the whole table/index (expensive; avoid for ML extraction at scale).
- **Batch operations**
  - `BatchGetItem` / `BatchWriteItem` reduce round-trips but do not make writes transactional.
- **Transactions**
  - ACID transactions across multiple items/tables are supported, with extra cost/latency.

**Hot partitions**

- Caused by skewed partition keys (e.g., “US” or a single customer ID receiving most traffic).
- Mitigations: add entropy (suffix/prefix), use composite keys, time-bucketing, or redesign access pattern.

---

## 4. Capacity Modes & Scaling

- **On-demand capacity**
  - Pay per request; best for spiky/unpredictable traffic and new apps.
- **Provisioned capacity**
  - Specify RCU/WCU; optional **auto scaling**; best for steady workloads.
- **Adaptive capacity** helps handle uneven access patterns, but doesn’t eliminate hot keys.

---

## 5. Streams, Events, and Integrations

- **DynamoDB Streams**
  - Change data capture (CDC) for inserts/updates/deletes.
  - Common pattern: stream → Lambda → downstream (S3, OpenSearch, feature store, notifications).
- **DAX (DynamoDB Accelerator)**
  - In-memory cache for read-heavy workloads; microsecond latency.
  - Not a general substitute for good key design.
- **TTL**
  - Automatically expires items (good for sessions, temporary features, time-bound data).

---

## 6. Availability, Durability, and DR

- Data is replicated across **multiple AZs** automatically.
- **Global Tables** provide multi-region active-active replication for low-latency global apps and DR.

---

## 7. Security & Governance

- **IAM** for API-level access control; fine-grained permissions per table/index/operation.
- **KMS encryption at rest**; TLS in transit.
- **VPC endpoints (PrivateLink)** for private access from VPCs.
- **Backup & restore**
  - **Point-in-time recovery (PITR)** (continuous backups, limited window).
  - **On-demand backups** for longer retention and cloning.

---

## 8. Common Use Cases

- User profiles, personalization context, session stores.
- Online feature retrieval for inference.
- IoT telemetry (often combined with time bucketing + TTL).
- Event-sourced systems using streams as CDC.

---

## 9. Exam/Interview Callouts

- Strong consistency is **not** available on **GSI** reads.
- DynamoDB performance is mostly about **key design** and **avoiding scans**.
- Choose **on-demand** for spiky workloads; **provisioned + auto scaling** for predictable ones.
- Consider **Global Tables** for multi-region active-active + DR.
- Remember common constraints (e.g., item size limits) and design around them.
