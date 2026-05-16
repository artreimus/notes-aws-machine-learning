---
title: "Kinesis Data Stream Vs Firehose"
exam: "MLA-C01"
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
  - "Kinesis Data Stream Vs Firehose"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Kinesis Data Stream Vs Firehose

Here's a comprehensive comparison between **Amazon Kinesis Data Streams (KDS)** and **Amazon Data Firehose (formerly Kinesis Data Firehose)**, highlighting their key differences and providing guidance on when to use each service.

---

### 📊 Comparison Table: Kinesis Data Streams vs. Data Firehose

|                         | Feature                                                            | **Kinesis Data Streams (KDS)**                                    | **Amazon Data Firehose** |
| ----------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------- | ------------------------ |
| **Purpose**             | Real-time data streaming with custom processing capabilities       | Fully managed service for loading data into AWS destinations      |
| **Latency**             | Real-time processing (~70–200 ms)                                  | Near real-time processing (buffering delay of 60 seconds or more) |
| **Data Retention**      | 24 hours by default; up to 7 days (extendable to 365 days)         | No data retention; data is delivered immediately to destinations  |
| **Scaling**             | Manual scaling by configuring shards                               | Automatic scaling managed by the service                          |
| **Data Replay**         | Supported; can reprocess data within retention period              | Not supported; data cannot be replayed once delivered             |
| **Data Transformation** | Requires custom code or integration with other services            | Supports basic transformations using AWS Lambda functions         |
| **Destinations**        | Requires custom consumers to process and route data                | Directly delivers data to S3, Redshift, OpenSearch, Splunk, etc.  |
| **Use Cases**           | Complex real-time analytics, custom processing, multiple consumers | Simple ETL, data archiving, loading data into AWS services        |
| **Management Overhead** | Higher; requires managing shards, scaling, and consumers           | Lower; fully managed with minimal configuration                   |
| **Cost Model**          | Based on shard hours and data volume                               | Based on data volume ingested and processed                       |

---

### 🧭 When to Use Each Service

#### ✅ Use **Kinesis Data Streams** when:

- You need **real-time processing** with low latency.
- Your application requires **custom processing logic** or integration with other AWS services like AWS Lambda, Amazon Managed Service for Apache Flink, or custom consumers.
- You need to **reprocess or replay** data within a retention window.
- You require **multiple consumers** to process the same stream concurrently.

#### ✅ Use **Amazon Data Firehose** when:

- You want a **fully managed service** to load streaming data into AWS destinations like S3, Redshift, or OpenSearch.
- Your use case involves **simple data transformation** and delivery without complex processing.
- You prefer **automatic scaling** and minimal management overhead.
- You do **not require data replay** capabilities.

---

### 🔗 Additional Resources

- [Amazon Kinesis Data Streams Documentation](https://docs.aws.amazon.com/kinesis/latest/dev/introduction.html)
- [Amazon Data Firehose Documentation](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
- [AWS Kinesis Data Streams vs. Data Firehose Comparison](https://jayendrapatil.com/aws-kinesis-data-streams-vs-kinesis-firehose/)

By understanding the differences and use cases for Kinesis Data Streams and Data Firehose, you can choose the service that best fits your application's requirements.


## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
