---
title: "Amazon Elastic Block Store (EBS)"
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
  - "Amazon Elastic Block Store (EBS)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Elastic Block Store (EBS)

## Overview

Amazon Elastic Block Store (EBS) is a scalable, high-performance block storage service designed for use with Amazon EC2 instances. EBS provides persistent storage volumes that can be attached to EC2 instances, allowing data to persist independently of the instance lifecycle. EBS is essential for workloads that require consistent, low-latency storage, such as databases, big data analytics, and machine learning (ML) pipelines. Key features include durability, snapshot capabilities, encryption, and the ability to dynamically scale storage.

## AWS Services & Features

- **EBS Volume Types**:
  - **General Purpose SSD (gp3, gp2)**: Balanced price and performance for most workloads, including ML training and inference.
  - **Provisioned IOPS SSD (io2, io1)**: High-performance, low-latency storage for I/O-intensive applications like large-scale ML training or databases.
  - **Throughput Optimized HDD (st1)**: Cost-effective for large, sequential workloads (e.g., big data, log processing).
  - **Cold HDD (sc1)**: Lowest cost, suitable for infrequently accessed data.
- **Snapshots**: Point-in-time backups of EBS volumes, stored in Amazon S3. Snapshots enable disaster recovery, data migration, and reproducibility in ML workflows.
- **Encryption**: EBS supports encryption at rest and in transit, using AWS Key Management Service (KMS).
- **Integration**: EBS integrates with EC2, AWS Backup, and can be used as storage for custom ML environments (e.g., SageMaker training on EC2).

## Practical Application

- **ML Training Data Storage**: Store large datasets on EBS volumes attached to EC2 or SageMaker training instances for high-throughput access.
- **Reproducibility**: Use EBS snapshots to capture the state of data and code, enabling consistent, repeatable ML experiments.
- **Performance Tuning**: Select appropriate EBS volume types (e.g., io2 for high IOPS) based on ML workload requirements.
- **Example Architecture**:
  - EC2 instance with attached EBS volumes for storing training data, model artifacts, and logs.
  - Snapshots used to back up data before/after training jobs.

## Challenges & Best Practices

- **Performance Optimization**:
  - Match EBS volume type to workload (e.g., use io2 for high IOPS needs).
  - Monitor and adjust volume size and IOPS as needed.
- **Cost Management**:
  - Delete unused volumes and snapshots to avoid unnecessary charges.
  - Use lower-cost volume types (st1, sc1) for infrequently accessed data.
- **Data Durability & Backup**:
  - Regularly create snapshots for backup and disaster recovery.
  - Automate snapshot management with AWS Backup or Lambda functions.
- **Security**:
  - Enable encryption for sensitive ML data.
  - Use IAM policies to control access to EBS resources.

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
