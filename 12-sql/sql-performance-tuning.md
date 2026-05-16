---
title: "SQL performance tuning"
exam: "MLA-C01"
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
  - "SQL performance tuning"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SQL performance tuning

## Why it matters

- Poorly tuned queries inflate cost on `Amazon Redshift` and `Amazon RDS` and
  can break pipeline SLAs.
- Exam scenarios probe how to diagnose hotspots, right-size resources, and
  apply indexing or partitioning.
- Optimization skills keep workloads efficient without oversizing
  infrastructure.

## Index strategy basics

- **B-tree indexes:** Balanced structures suited for equality and range scans on
  selective columns such as primary keys.
- **Hash distribution (Redshift):** Spreads rows by a hash key to minimize data
  movement during large joins.
- **Bitmap indexes:** Encode low-cardinality values for fast OLAP filters.
- **Covering indexes:** Include additional columns so queries read from the
  index without touching the base table.
- Index columns that appear in `WHERE`, `JOIN`, and `ORDER BY` clauses; drop
  unused indexes to reduce write overhead.
- Align Redshift distribution style (KEY, EVEN, AUTO) with join partners to
  reduce network shuffles.

## Statistics and query plans

- Refresh stats with `ANALYZE` (PostgreSQL, Redshift) or `ANALYZE TABLE`
  (MySQL) after bulk loads.
- Use `EXPLAIN` to confirm join order, estimated row counts, and index usage.
- Enable Performance Insights on Aurora or RDS to visualize waits such as locks
  and I/O pressure.
- Parameterize queries so cached plans can be reused instead of recompiled.

## Partitioning and data layout

- Partition large tables by date or tenant to prune scans and ease archival
  deletes.
- Aurora MySQL supports `PARTITION BY RANGE (TO_DAYS(order_date))` for rolling
  retention windows.
- Redshift sort keys create zone maps; place frequently filtered columns first
  to maximize pruning.
- Athena partitions follow S3 prefixes (for example `s3://bucket/dt=2024-01-01/`);
  repair metadata with `MSCK REPAIR TABLE` or `ALTER TABLE ADD PARTITION`.

## Workload management

- Configure Redshift Workload Management queues to isolate ETL from BI queries.
- Use connection pooling so RDS hosts avoid connection storms and idle memory
  usage.
- Batch small writes into multi-row inserts to cut transaction overhead.
- Turn on Redshift result caching for recurring dashboards; caches invalidate
  when base tables change.

## Troubleshooting playbook

- Track stage timings; long scans hint at missing partitions or filter
  pushdown.
- Detect skewed joins where one node processes most rows; adjust distribution
  keys or pre-aggregate.
- Keep predicates sargable by avoiding functions on columns (for example
  `DATE(created_at)`); otherwise indexes are ignored.
- Monitor RDS metrics (`ReadIOPS`, `WriteLatency`) to catch storage bottlenecks.

## Exam tips

- Know when to choose sort keys versus distribution keys in Redshift scenarios.
- Distinguish OLTP tuning (indexes, normalization) from OLAP tactics (columnar
  compression, sort keys).
- Use serverless scaling such as Aurora Serverless v2 or Redshift RA3 for burst
  workloads instead of permanent overprovisioning.
- Reduce Athena spend with partition pruning, column projection, and Parquet or
  ORC storage.

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
