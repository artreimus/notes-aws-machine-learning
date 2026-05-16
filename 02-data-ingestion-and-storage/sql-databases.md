---
title: "SQL Databases in AWS"
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
  - "SQL Databases in AWS"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SQL Databases in AWS

## 1. Overview

**SQL databases** (also known as relational databases) are structured systems that store data in tables with predefined schemas. They use Structured Query Language (SQL) for defining, manipulating, and querying data. SQL databases are ideal for applications requiring complex queries, transactional consistency, and strong data integrity.

**Key Features of SQL Databases:**

- **Structured Schema:** Data is organized into tables with defined columns and data types.
- **ACID Compliance:** Support for Atomicity, Consistency, Isolation, and Durability, ensuring reliable transactions.
- **Powerful Querying:** SQL enables complex joins, aggregations, and analytical queries.
- **Data Integrity:** Enforces constraints, relationships, and referential integrity between tables.

**Relevance in AWS Machine Learning Workflows:**

- **Data Preparation:** Many ML workflows start with structured data stored in SQL databases, making them a common source for feature engineering and model training.
- **Transactional Data:** Applications that generate transactional data (e.g., e-commerce, finance) often use SQL databases as their primary data store.
- **Integration:** SQL databases integrate with AWS analytics and ML services (e.g., SageMaker, Glue, Redshift) for seamless data pipelines.

---

## 2. AWS Services & Features

AWS provides several managed SQL database services, each optimized for different use cases:

### Amazon RDS (Relational Database Service)

- **Type:** Managed relational database service supporting multiple engines (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server).
- **Key Features:**
  - Automated backups, patching, and scaling.
  - High availability with Multi-AZ deployments.
  - Read replicas for scaling read workloads.
- **Use Cases:** OLTP applications, web/mobile backends, ERP/CRM systems.
- **Why Essential:** Simplifies database management, allowing teams to focus on application development.

### Amazon Aurora

- **Type:** MySQL- and PostgreSQL-compatible relational database.
- **Key Features:**
  - Up to 5x performance of standard MySQL and 3x of PostgreSQL.
  - Fault-tolerant, self-healing storage.
  - Serverless and Global Database options.
- **Use Cases:** High-performance OLTP, SaaS applications, global apps.
- **Why Essential:** Combines the performance and availability of commercial databases with the cost-effectiveness of open source.

### Amazon Redshift

- **Type:** Fully managed, petabyte-scale data warehouse.
- **Key Features:**
  - Columnar storage and massively parallel processing (MPP).
  - Integrates with S3, Glue, and ML services.
  - Advanced analytics and machine learning capabilities.
- **Use Cases:** Data warehousing, analytics, business intelligence, ML feature stores.
- **Why Essential:** Enables fast, complex queries across large datasets for analytics and ML.

### Amazon ElastiCache (for Redis and Memcached)

- **Type:** In-memory data store, often used as a cache for SQL databases.
- **Key Features:**
  - Microsecond latency, high throughput.
  - Supports Redis and Memcached engines.
- **Use Cases:** Caching, session management, real-time analytics.
- **Why Essential:** Improves performance of SQL-backed applications by offloading frequent queries.

---

**Summary Table: AWS SQL Database Services**

| Service     | Engine/Type             | Key Use Cases                   | Distinctive Features                 |
| ----------- | ----------------------- | ------------------------------- | ------------------------------------ |
| RDS         | MySQL, PostgreSQL, etc. | OLTP, web/mobile apps           | Managed, Multi-AZ, read replicas     |
| Aurora      | MySQL, PostgreSQL       | High-performance OLTP, SaaS     | High performance, serverless, global |
| Redshift    | Data warehouse          | Analytics, BI, ML feature store | Petabyte scale, MPP, ML integration  |
| ElastiCache | Redis, Memcached        | Caching, real-time analytics    | In-memory, microsecond latency       |

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
