---
title: "Data Quality Validation"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "1.3"
  - "4.1"
service:
  - "AWS Glue Data Quality"
  - "AWS Glue DataBrew"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "data-quality"
aliases:
  - "Data Quality Validation"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Data Quality Validation

## Knowledge Relevance

Cross-service note for validating ML datasets before training and monitoring quality drift after deployment.

## When To Use

- Use schema checks, completeness checks, uniqueness checks, referential checks, and range checks before model training.
- Use Glue Data Quality for rules and scores.
- Use DataBrew for visual profiling and cleanup.

## Core Concepts

- Validation catches invalid, missing, duplicated, out-of-range, and inconsistent data.
- Quality rules should align with feature contracts and model assumptions.
- Quality results can trigger quarantine, alerts, or retraining workflows.

## AWS Services And Features

- AWS Glue Data Quality
- AWS Glue DataBrew
- Amazon EventBridge
- Amazon CloudWatch

## Implementation Patterns

- Raw dataset -> profiling -> ruleset -> fail/quarantine bad records -> only validated data enters training.

## Tradeoffs And Pitfalls

- Passing schema validation does not guarantee useful features.
- Rules should be versioned with the pipeline.
- Bad validation thresholds can block valid data or permit silent drift.

## Decision Triggers

- DQDL and ruleset point to Glue Data Quality.
- Visual profiling/no-code cleanup points to DataBrew.
- Data integrity before modeling points to Domain 1.

## Related Notes

- [[glue-data-quality]]
- [[glue-databrew]]
- [[feature-engineering]]


## Sources

- https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html
- https://docs.aws.amazon.com/databrew/latest/dg/what-is.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
