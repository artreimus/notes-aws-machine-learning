---
title: "AWS Glue DataBrew"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "1.2"
  - "1.3"
service:
  - "AWS Glue DataBrew"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "glue"
  - "data-preparation"
aliases:
  - "AWS Glue DataBrew"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Glue DataBrew

## Knowledge Relevance

Domain 1 data preparation service for visual cleaning, profiling, and no-code transformation before analytics or ML.

## When To Use

- Use when analysts need visual data preparation without writing Spark code.
- Use for profiling, cleaning, normalizing, and recipe-based transformations.
- Use before data lands in curated S3, Athena, Redshift, or SageMaker training datasets.

## Core Concepts

- Projects connect to datasets and show a grid-like preparation workspace.
- Recipes capture reusable transformation steps.
- Jobs apply recipes and usually write prepared output to Amazon S3.

## AWS Services And Features

- AWS Glue DataBrew
- Amazon S3
- AWS Glue Data Catalog

## Implementation Patterns

- Raw data in S3 -> DataBrew project -> recipe -> DataBrew job -> prepared S3 dataset.
- Use DataBrew for no-code exploratory cleanup; use Glue ETL when engineering-controlled Spark jobs are required.

## Tradeoffs And Pitfalls

- DataBrew is not a model-training service.
- Prefer Glue ETL or Glue Data Quality for automated production enforcement when code-first control is needed.
- Validate output schema before using the prepared dataset for training.

## Decision Triggers

- Visual/no-code data preparation points to DataBrew.
- Recipe-based transformations and profiling point to DataBrew.
- Code-first ETL or distributed Spark transformations point to AWS Glue ETL instead.

## Related Notes

- [[glue]]
- [[glue-data-quality]]
- [[data-quality-validation]]


## Sources

- https://docs.aws.amazon.com/databrew/latest/dg/what-is.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
