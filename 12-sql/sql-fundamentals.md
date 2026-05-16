---
title: "SQL fundamentals"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "draft"
domain:
  - "1.2"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "12_sql"
aliases:
  - "SQL fundamentals"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SQL fundamentals

## Why it matters

- SQL underpins transactional systems that feed ML feature stores and analytics
  workloads on AWS.
- Exam scenarios expect fluency in translating business logic into joins,
  aggregations, and constraints.
- Mastery of core statements helps debug pipeline issues when data lands in
  `Amazon RDS`, `Amazon Aurora`, or `Amazon Redshift`.

## Relational model essentials

- Tables represent entities with rows (records) and columns (attributes) governed
  by schemas.
- Normalization (1NF, 2NF, 3NF) reduces redundancy but may trade off query
  simplicity; denormalization accelerates read-heavy analytics.
- Primary keys enforce row uniqueness; foreign keys preserve referential
  integrity across tables.
- Use surrogate keys when natural keys are composite or volatile; expose natural
  keys for reporting clarity.

## Core statement families

| Statement group                  | Purpose                            | Typical syntax cues                   |
| -------------------------------- | ---------------------------------- | ------------------------------------- |
| DDL (Data Definition Language)   | Create or modify schema objects    | `CREATE`, `ALTER`, `DROP`             |
| DML (Data Manipulation Language) | Insert, update, delete, merge data | `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| DQL (Data Query Language)        | Retrieve data via `SELECT`         | `SELECT ... FROM ... WHERE ...`       |
| DCL & TCL                        | Control access and transactions    | `GRANT`, `REVOKE`, `BEGIN`, `COMMIT`  |

## Constraints and relationships

- **Primary key:** Uniqueness + not null; composite keys follow
  `(col_a, col_b)` order for index usage.
- **Foreign key:** Optional `ON DELETE CASCADE` for dimension cleanup; caution in
  high-volume OLTP because cascading can lock child tables.
- **Unique constraint:** Complement to primary key for enforcing alternate
  business keys (e.g., email addresses).
- **Check constraint:** Lightweight data validation; push rules like percentage
  ranges to the database instead of app code.
- **Not null:** Defaults to enforcing data completeness—flag columns that can
  tolerate missing values for pipeline resilience.

## Transactions and isolation

| Isolation level  | Default behavior                                                         | When to choose                                      |
| ---------------- | ------------------------------------------------------------------------ | --------------------------------------------------- |
| Read uncommitted | Allows dirty reads; rare in AWS managed engines                          | Only for diagnostic `SELECT` against volatile data  |
| Read committed   | Prevents dirty reads; `Amazon RDS` default for PostgreSQL and SQL Server | Balanced OLTP workloads                             |
| Repeatable read  | Prevents non-repeatable reads; MySQL + PostgreSQL offer                  | Use when analytics queries re-read the same rows    |
| Serializable     | Strictest, may lock more rows                                            | Financial operations requiring absolute consistency |

- Always wrap multi-statement modifications in `BEGIN`/`COMMIT` blocks to
  maintain atomicity.
- Use `SAVEPOINT` to roll back part of a transaction in long-running ETL
  scripts.
- Monitor transaction logs to size storage and tune replication lag in
  `Amazon RDS`.

## Query building workflow

- Start with a minimal `SELECT` to validate filters, then layer joins and
  aggregations.
- Alias tables (`orders AS o`) to improve readability and join accuracy.
- Apply filtering in `WHERE` before grouping; use `HAVING` only for
  post-aggregation filters.
- Prefer explicit `JOIN ... ON` syntax over comma joins for clarity and
  optimizer hints.

## Exam tips

- Identify when SQL transforms happen inside vs. outside AWS managed services
  (e.g., using `AWS Glue` vs. pushing logic to `Amazon Redshift`).
- Watch for `SELECT *` in scenarios; the exam favors projecting only needed
  columns to reduce cost.
- Review how IAM and database-level permissions combine; `GRANT` statements do
  not override missing IAM policies.
- Understand how SQL data types align with downstream analytics tools (e.g.,
  `BOOLEAN` vs. `TINYINT`).

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
