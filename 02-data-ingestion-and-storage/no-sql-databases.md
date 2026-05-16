---
title: "NoSQL Databases in AWS"
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
  - "NoSQL Databases in AWS"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# NoSQL Databases in AWS

## 1. Overview

**NoSQL databases** are a class of database management systems designed to handle large volumes of unstructured, semi-structured, or structured data that may not fit well into traditional relational (SQL) databases. Unlike SQL databases, NoSQL systems are optimized for scalability, flexibility, and high performance, making them ideal for modern applications that require rapid development, horizontal scaling, and the ability to handle diverse data types.

**Key Features of NoSQL Databases:**

- **Schema Flexibility:** NoSQL databases allow dynamic, schema-less data models, enabling easy adaptation to changing data requirements.
- **Horizontal Scalability:** Designed to scale out by distributing data across multiple servers or nodes, supporting high throughput and low latency.
- **Variety of Data Models:** Support for key-value, document, column-family, and graph data models.
- **High Availability & Fault Tolerance:** Built-in replication and failover mechanisms ensure data durability and availability.

**Relevance in AWS Machine Learning Workflows:**

- **Handling Diverse Data:** ML applications often ingest and process data from various sources (e.g., logs, IoT devices, social media) that may not have a fixed schema.
- **Real-Time Processing:** NoSQL databases can support real-time data ingestion and retrieval, which is crucial for ML models that require up-to-date information.
- **Scalability:** As ML workloads grow, NoSQL databases can scale seamlessly to accommodate increasing data volumes.

---

## 2. AWS Services & Features

AWS offers several managed NoSQL database services, each tailored to specific use cases:

### Amazon DynamoDB

- **Type:** Key-value and document database.
- **Key Features:**
  - Fully managed, serverless, and highly scalable.
  - Single-digit millisecond performance at any scale.
  - Built-in security, backup, restore, and in-memory caching (DAX).
  - Supports both provisioned and on-demand capacity modes.
- **Use Cases:** Real-time analytics, recommendation engines, user profiles, IoT data storage, session management.
- **Why Essential:** DynamoDB is the go-to NoSQL service for most AWS ML workloads due to its flexibility, scalability, and seamless integration with other AWS services (e.g., Lambda, SageMaker, Kinesis).

### Amazon DocumentDB (with MongoDB compatibility)

- **Type:** Document database (JSON-like documents).
- **Key Features:**
  - Fully managed, scalable, and compatible with MongoDB APIs.
  - Automated backups, patching, and monitoring.
  - Designed for high availability with replication across multiple AZs.
- **Use Cases:** Content management, cataloging, mobile/web applications.
- **Why Essential:** Useful for applications already using MongoDB or requiring rich document querying.

### Amazon Keyspaces (for Apache Cassandra)

- **Type:** Wide-column database.
- **Key Features:**
  - Managed Cassandra-compatible service.
  - Serverless, scalable, and highly available.
  - Supports Cassandra Query Language (CQL).
- **Use Cases:** Time-series data, sensor data, messaging applications.
- **Why Essential:** Ideal for workloads that require Cassandra's data model and scalability.

### Amazon Neptune

- **Type:** Graph database.
- **Key Features:**
  - Supports property graph and RDF graph models.
  - Fully managed, with high performance and availability.
- **Use Cases:** Fraud detection, knowledge graphs, recommendation engines.
- **Why Essential:** Enables graph-based ML use cases, such as relationship analysis.

---

**Summary Table: AWS NoSQL Database Services**

| Service    | Data Model          | Key Use Cases                  | Distinctive Features             |
| ---------- | ------------------- | ------------------------------ | -------------------------------- |
| DynamoDB   | Key-value, Document | Real-time, IoT, ML pipelines   | Serverless, millisecond latency  |
| DocumentDB | Document (JSON)     | Content, catalogs, web/mobile  | MongoDB-compatible, managed      |
| Keyspaces  | Wide-column         | Time-series, sensor, messaging | Cassandra-compatible, serverless |
| Neptune    | Graph               | Fraud, recommendations, graphs | Graph queries, high performance  |

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
