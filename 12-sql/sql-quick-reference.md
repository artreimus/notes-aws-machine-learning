---
title: "SQL quick reference"
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
  - "SQL quick reference"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SQL quick reference

Short, exam-ready reminders for common SQL tasks and patterns.

## Query skeleton

```sql
SELECT column_list
FROM table_name AS t
JOIN other_table AS o ON t.key = o.key
WHERE conditions
GROUP BY grouping_columns
HAVING post_aggregate_filter
ORDER BY sort_columns
LIMIT n OFFSET m;
```

- Start with `SELECT` + `FROM`, then layer filters, joins, aggregation, sort, and limit.
- Alias tables (`orders o`) to keep joins readable and unambiguous.

## Filtering and ordering

- `WHERE` filters rows before grouping; `HAVING` filters after aggregation.
- Combine logic with `AND`/`OR`; wrap OR groups in parentheses to avoid surprises.
- Use `IN` for short lists, `BETWEEN` for ranges, and `LIKE 'abc%'` for prefixes.
- `ORDER BY 1, 2` sorts by select-list positions; explicit column names are clearer.

## Join essentials

| Join type  | Keeps rows from         | Typical use                                        |
| ---------- | ----------------------- | -------------------------------------------------- |
| Inner      | Only matched rows       | Standard fact-to-dimension joins                   |
| Left       | Left table + matches    | Preserve driving table even when lookups are blank |
| Right      | Right table + matches   | Same as left, but with reversed driving table      |
| Full outer | All rows with null gaps | Reconciling two sources                            |
| Cross      | All combinations        | Date scaffolds, permutations (filter immediately)  |

- Place the most selective table first to reduce join size.
- Prefer explicit `JOIN ... ON` to comma joins for readability and optimizer clarity.

## Aggregation basics

- Pair aggregates with `GROUP BY` columns; only aggregates and grouped columns can appear in the select list.
- Use conditional aggregation with `CASE WHEN` or `FILTER`.
- `COUNT(*)` counts rows; `COUNT(col)` ignores nulls.

```sql
SELECT customer_id,
       COUNT(*) AS orders,
       SUM(total_amount) AS revenue,
       SUM(CASE WHEN status = 'returned' THEN 1 ELSE 0 END) AS returns
FROM fact_orders
WHERE order_date >= DATE_TRUNC('year', CURRENT_DATE)
GROUP BY customer_id
HAVING SUM(total_amount) > 5000;
```

## Window functions

- Syntax: `function(...) OVER (PARTITION BY ... ORDER BY ... [ROWS BETWEEN ...])`.
- Keep all original rows while adding context like rankings or running totals.
- Use `ROW_NUMBER()` for deterministic ranking; `LAG()`/`LEAD()` for previous/next comparisons.

```sql
SELECT customer_id,
       order_date,
       total_amount,
       SUM(total_amount) OVER (
         PARTITION BY customer_id
         ORDER BY order_date
         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS cumulative_spend
FROM fact_orders;
```

## Subqueries, CTEs, and set operations

- Inline subqueries filter with `IN`/`EXISTS`; correlated subqueries reference the outer query.
- CTEs (`WITH alias AS (...)`) break complex logic into named steps; recursive CTEs walk hierarchies.
- Combine result sets with `UNION` (deduplicates), `UNION ALL` (keeps duplicates), `INTERSECT`, and `EXCEPT`.

## Data types and functions

- Common types: integers, decimals, `VARCHAR`, `BOOLEAN`, `DATE`, `TIMESTAMP`; choose the smallest precise type.
- Convert explicitly with `CAST(expr AS type)` or `::type` (PostgreSQL/Redshift).
- String helpers: `LOWER`, `UPPER`, `TRIM`, `SUBSTRING`, `CONCAT`.
- Date helpers: `CURRENT_DATE`, `DATE_TRUNC('month', ts)`, `DATEADD('day', 7, ts)` (engine-specific).

## Modifying data

```sql
INSERT INTO table_name (col1, col2) VALUES ('a', 10);
UPDATE table_name SET col2 = col2 + 1 WHERE id = 42;
DELETE FROM table_name WHERE created_at < CURRENT_DATE - INTERVAL '30 days';
MERGE target t USING source s
  ON t.id = s.id
WHEN MATCHED THEN UPDATE SET col = s.col
WHEN NOT MATCHED THEN INSERT (id, col) VALUES (s.id, s.col);
```

- Wrap multi-statement changes in `BEGIN`/`COMMIT` to keep them atomic; use `ROLLBACK` on error.
- Add `RETURNING` (PostgreSQL/Redshift) to capture changed rows without a second query.

## Table design and constraints

- Primary keys enforce uniqueness; foreign keys maintain relationships; `NOT NULL` guards required fields.
- Use surrogate keys when natural keys are composite or volatile; expose natural keys for reporting clarity.
- Default values prevent null drift (`created_at DEFAULT CURRENT_TIMESTAMP`).

## Performance quick wins

- Project only needed columns; avoid `SELECT *` in production or exam scenarios.
- Filter early and on indexed columns to stay sargable (avoid wrapping columns in functions).
- For analytics engines, prefer columnar formats, partitions, and sort keys (Redshift, Athena).

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
