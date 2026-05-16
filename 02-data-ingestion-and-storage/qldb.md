---
title: "Amazon QLDB"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "legacy"
domain:
  - "supplemental"
service:
  - "Amazon QLDB"
tags:
  - "aws"
  - "mla-c01"
  - "legacy"
  - "supplemental"
aliases:
  - "Amazon QLDB"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon QLDB

## Knowledge Relevance

Legacy/supplemental note. Amazon QLDB is in full shutdown and is not a current MLA-C01 study target.

## When To Use

- Use only for historical audit-ledger context.
- For current AWS audit/compliance study, focus on CloudTrail, Config, S3 object lock/versioning, and governed data stores.

## Core Concepts

- QLDB was a ledger database service.
- AWS General Reference lists Amazon QLDB in full shutdown as of July 31, 2025.

## AWS Services And Features

- Amazon QLDB
- AWS CloudTrail
- AWS Config

## Implementation Patterns

- Historical ledger database pattern -> current alternatives depend on audit requirement and data model.

## Tradeoffs And Pitfalls

- Do not prioritize QLDB for MLA-C01.
- Full shutdown means it should not be a current answer choice.

## Decision Triggers

- Ledger database with shutdown caveat points to legacy QLDB.
- API activity history points to CloudTrail.

## Related Notes

- [[cloudtrail]]
- [[aws-config]]


## Sources

- https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-out-of-scope-services.html
