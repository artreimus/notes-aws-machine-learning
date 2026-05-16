---
title: "Data Lakes, Lakehouses, And Warehouses"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "1.1"
  - "1.2"
  - "1.3"
service:
  - "Amazon S3"
  - "AWS Lake Formation"
  - "Amazon Redshift"
  - "Amazon Athena"
  - "AWS Glue"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "data-architecture"
aliases:
  - "Data Lakes, Lakehouses, And Warehouses"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Data Lakes, Lakehouses, And Warehouses

## Exam Relevance

Domain 1 architecture note for choosing between data lake, lakehouse, and warehouse patterns for ML datasets.

## When To Use

- Use S3-based data lakes for flexible, durable raw/curated data storage.
- Use Lake Formation for governance over data lake permissions.
- Use Athena for serverless SQL over S3 and Redshift for managed warehouse workloads.
- Use Apache Iceberg/Hudi/Delta-style table formats for lakehouse-style transactional tables where supported.

## Core Concepts

- Data lakes store raw/curated data, often in S3.
- Warehouses optimize structured analytics.
- Lakehouses add table/transaction/governance features over lake storage.
- Glue Elastic Views should not be treated as current exam material; use Glue, Lake Formation, Athena, Redshift, and table formats instead.

## AWS Services And Features

- Amazon S3
- AWS Glue
- AWS Lake Formation
- Amazon Athena
- Amazon Redshift

## Implementation Patterns

- Raw zone -> curated zone -> catalog with Glue -> governed access with Lake Formation -> Athena/Redshift/SageMaker consumption.

## Tradeoffs And Pitfalls

- Data lake flexibility can lead to schema/governance sprawl without catalog and quality controls.
- Warehouse performance comes with modeling and cost tradeoffs.
- Do not rely on stale Glue Elastic Views references.

## Exam Triggers

- S3 data lake and governance point to S3 + Glue Catalog + Lake Formation.
- Warehouse analytics at scale points to Redshift.
- Serverless query over S3 points to Athena.

## Related Notes

- [[s3]]
- [[glue]]
- [[lake-formation]]
- [[athena]]
- [[redshift]]


## Sources

- https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
- https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html
- https://docs.aws.amazon.com/athena/latest/ug/what-is.html
- https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
