---
title: "AWS Glue Data Quality"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "1.3"
  - "4.1"
service:
  - "AWS Glue"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "domain-4"
  - "glue"
  - "data-quality"
aliases:
  - "AWS Glue Data Quality"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Glue Data Quality

## Knowledge Relevance

Domain 1 and Domain 4 feature for measuring, monitoring, and enforcing data quality before and during ML workflows.

## When To Use

- Use to define DQDL rules over Data Catalog tables or Glue ETL jobs.
- Use to catch bad records before loading a training or inference dataset.
- Use with EventBridge and CloudWatch for automated data quality response.

## Core Concepts

- DQDL defines data quality rules.
- Rulesets group rules and receive data quality scores.
- Data Catalog quality checks evaluate stored datasets; Glue ETL checks can identify failed records in pipelines.

## AWS Services And Features

- AWS Glue Data Quality
- AWS Glue Data Catalog
- AWS Glue ETL
- Amazon EventBridge
- Amazon CloudWatch

## Implementation Patterns

- Catalog table -> recommended or authored ruleset -> scheduled evaluation -> score/result in Glue.
- Glue ETL job -> DQDL transform -> route failed records to quarantine and publish metrics.

## Tradeoffs And Pitfalls

- Nested/list data types have support limitations.
- Catalog checks are useful for stewardship; ETL checks are better for pipeline enforcement.
- Rules should match the ML feature contract, not just table schema.

## Decision Triggers

- DQDL, data quality score, and rulesets point to Glue Data Quality.
- Bad records need quarantining before model training points to Glue ETL with Data Quality.
- Ongoing monitoring of data quality points to Domain 4.

## Related Notes

- [[glue]]
- [[data-quality-validation]]
- [[retraining-triggers-and-drift-response]]


## Sources

- https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
