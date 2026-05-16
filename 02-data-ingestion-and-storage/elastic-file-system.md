---
title: "Amazon Elastic File System (EFS)"
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
  - "Amazon Elastic File System (EFS)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Elastic File System (EFS)

## Overview

Amazon Elastic File System (EFS) is a fully managed, scalable, cloud-native Network File System (NFS) that provides simple, serverless, set-and-forget file storage for use with AWS Cloud services and on-premises resources. EFS automatically grows and shrinks as files are added and removed, eliminating the need for provisioning and managing capacity. It is designed for high availability and durability, making it suitable for a wide range of workloads, including machine learning (ML), analytics, web serving, and content management.

**Key Features:**

- Fully managed, elastic, and serverless
- Supports NFSv4 protocol
- Scales automatically to petabytes
- High availability and durability across multiple Availability Zones (AZs)
- Pay-as-you-go pricing
- Supports encryption at rest and in transit

**Relevance to AWS ML:**
EFS is commonly used to provide shared storage for ML training jobs, especially when multiple compute instances (e.g., Amazon SageMaker, EC2) need concurrent access to the same data.

## AWS Services & Features

- **Amazon SageMaker:** EFS can be mounted as a file system in SageMaker training jobs, enabling access to large datasets and shared resources across distributed training clusters.
- **Amazon EC2:** EFS can be mounted on EC2 instances, providing persistent, shared storage for ML workloads, data preprocessing, and model artifacts.
- **AWS Lambda:** EFS integration allows Lambda functions to access large files and datasets, enabling serverless ML inference or preprocessing.
- **AWS DataSync:** Facilitates fast, automated data transfer between on-premises storage and EFS, or between EFS file systems.
- **AWS Backup:** Provides centralized backup management for EFS file systems.

**Distinctive Capabilities:**

- Shared, concurrent access from thousands of compute nodes
- Seamless scaling with no performance degradation
- Integration with AWS Identity and Access Management (IAM) for access control
- Lifecycle management to move infrequently accessed files to lower-cost storage

## Practical Application

**Example 1: Distributed ML Training with SageMaker**

- Multiple SageMaker training instances mount the same EFS file system to access training data, share checkpoints, and store model outputs. This is especially useful for distributed training or when datasets are too large for instance storage.

**Example 2: Data Preprocessing Pipeline**

- EC2 instances running data preprocessing jobs read raw data from S3, process it, and write the results to EFS. Downstream ML training jobs then read the processed data from EFS.

**Example 3: Serverless ML Inference**

- Lambda functions mount EFS to access large ML models or datasets that exceed the Lambda package size limit, enabling scalable, serverless inference workflows.

**Sample Architecture:**

- S3 (raw data) → EC2/Lambda (preprocessing) → EFS (shared processed data) → SageMaker (training)

## Challenges & Best Practices

**Common Challenges:**

- **Performance Tuning:** Suboptimal throughput or IOPS if not configured for workload patterns (e.g., burst vs. provisioned throughput).
- **Cost Management:** Unused or infrequently accessed data can increase costs if not managed with lifecycle policies.
- **Security:** Misconfigured network or IAM policies can expose data.
- **Data Consistency:** Applications must handle NFS semantics for file locking and consistency.

**Best Practices:**

- Use EFS lifecycle management to automatically move infrequently accessed files to EFS Infrequent Access (IA) storage class.
- Monitor usage and performance with Amazon CloudWatch.
- Restrict network access using security groups and NFS mount targets.
- Use IAM policies and EFS access points for fine-grained access control.
- Encrypt data at rest and in transit.
- For high-performance ML workloads, consider using provisioned throughput mode.

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
