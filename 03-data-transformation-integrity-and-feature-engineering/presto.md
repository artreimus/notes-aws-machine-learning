---
title: "What is Presto?"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "draft"
domain:
  - "1.2"
  - "1.3"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "03_data_transformation_integrity_and_feature_engineering"
aliases:
  - "What is Presto?"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# What is Presto?

**Presto** is an open-source, distributed SQL query engine designed for fast, interactive analytics on large datasets. It allows you to run SQL queries across data stored in a variety of sources, including Amazon S3, HDFS, relational databases, and NoSQL systems.

## Key Features

- **Distributed Architecture:**  
  Presto can scale out to hundreds of nodes, enabling high-performance querying on petabyte-scale data.
- **Separation of Storage and Compute:**  
  Presto queries data where it lives, without requiring data movement or duplication.
- **ANSI SQL Support:**  
  Provides full support for standard SQL, making it accessible to analysts and data scientists.
- **Connector Ecosystem:**  
  Integrates with a wide range of data sources, including S3, Hive, Cassandra, MySQL, PostgreSQL, and more.

## Relevance to Machine Learning

- **Data Exploration and Analysis:**  
  Presto is often used to quickly explore and aggregate large datasets before ML model training.
- **Feature Engineering:**  
  Enables complex SQL-based feature extraction and transformation at scale.
- **Integration with AWS:**  
  Available as Amazon Athena (a serverless Presto service) and as a supported engine on Amazon EMR, making it easy to use in AWS-based ML workflows.

## Typical Use Cases

- Interactive analytics on data lakes (e.g., querying S3 data with Athena).
- Ad hoc reporting and dashboarding.
- Preprocessing and aggregating data for ML pipelines.

**References:**  
- [Presto Documentation](https://prestodb.io/docs/current/)
- [Amazon Athena Documentation](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
