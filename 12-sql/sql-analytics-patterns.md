# SQL analytics patterns

## Why it matters

- AWS data engineers translate business KPIs into SQL for dashboards, feature
  stores, and ML datasets.
- The exam checks fluency with joins, aggregations, window functions, and CTEs
  that power analytical workflows.
- Mastery enables efficient use of `Amazon Redshift`, `Amazon Athena`, and
  `AWS Glue` transformations.

## Aggregations and grouping

- Aggregate functions (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`) summarize fact
  tables.
- Always pair aggregates with `GROUP BY` columns to avoid accidental cross
  joins.
- Use conditional aggregation via `FILTER` (Redshift, PostgreSQL) or `CASE WHEN`
  expressions for cohort analysis.

```sql
SELECT region,
       COUNT(*) AS orders,
       SUM(total_amount) AS gross_revenue,
       SUM(
         CASE WHEN status = 'returned' THEN 1 ELSE 0 END
       ) AS returns
FROM fact_orders
GROUP BY region
ORDER BY gross_revenue DESC;
```

## Join strategies

- **Inner join:** Match rows across tables when both sides include required
  records.
- **Left join:** Preserve driving table rows even when related data is missing.
- **Full outer join:** Merge all rows with null placeholders to reconcile data
  sources.
- **Cross join:** Produce a Cartesian product; pair with filters to create date
  scaffolds or permutations.
- Push selective filters on the driving table before joining to shrink
  intermediates.
- In star schemas, join on surrogate keys and filter by dimension attributes
  such as `dim_date.calendar_month`.

## Window functions

- Window syntax uses `OVER (PARTITION BY ... ORDER BY ...)` to add context
  without reducing row count.
- Running totals, rankings, and lag/lead comparisons reuse the same partition
  keys but change function choice.

```sql
SELECT customer_id,
       order_date,
       total_amount,
       SUM(total_amount) OVER (
         PARTITION BY customer_id
         ORDER BY order_date
         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS cumulative_spend,
       LAG(order_date) OVER (
         PARTITION BY customer_id
         ORDER BY order_date
       ) AS previous_order
FROM fact_orders;
```

- Use frame clauses (`ROWS BETWEEN`) for running totals; defaults vary by engine.
- Prefer `ROW_NUMBER()` for unique rankings and `RANK()` when ties should share
  placement.

## Common table expressions

- `WITH` clauses break large transformations into named steps that stay readable
  and reusable.
- Recursive CTEs (`WITH RECURSIVE`) support hierarchies such as organization
  charts or bill of materials in PostgreSQL and Redshift.
- Confirm whether the engine materializes or inlines CTEs; Redshift inlines
  simple cases for better optimization.

```sql
WITH top_customers AS (
  SELECT customer_id, SUM(total_amount) AS spend
  FROM fact_orders
  WHERE order_date >= DATE_TRUNC('year', CURRENT_DATE)
  GROUP BY customer_id
  HAVING SUM(total_amount) > 5000
)
SELECT c.customer_id, c.spend, d.segment
FROM top_customers c
JOIN dim_customer d
  ON c.customer_id = d.customer_id;
```

## Time-series analysis

- Generate continuous date scaffolds with `DATE_TRUNC`, `DATEADD`, or
  `GENERATE_SERIES()` to expose gaps.
- Bucket events by hour or day using `DATE_TRUNC` and aggregate by the truncated
  timestamp.
- Detect session breaks by comparing `LAG(event_time)` to the current event and
  resetting when gaps exceed the threshold.
- Partition Athena tables by time columns to limit data scanned during ad hoc
  analysis.

## Handling nulls and conditionals

- Apply `COALESCE` to substitute default values and keep aggregates from
  returning null.
- Use `NULLIF` to prevent divide-by-zero errors before computing ratios.
- Structure `CASE` expressions with mutually exclusive conditions and a final
  `ELSE` path to catch unexpected data.

## Exam tips

- Choose window functions when the question retains row granularity; use
  aggregates when summarizing.
- Left joins keep the grain of the driving table, while inner joins filter out
  mismatches.
- Reduce cost in Athena by filtering on partitions, selecting only needed
  columns, and preferring columnar formats.
- Respect boolean operator precedence (`NOT`, `AND`, `OR`) to avoid logical
  errors in complex filters.
