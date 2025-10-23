# SQL on AWS

## Why it matters

- AWS services expose SQL interfaces for transactional apps, analytics, and serverless querying.
- Exam questions blend SQL capabilities with platform choice, cost control, and integration patterns.
- Knowing where SQL runs—managed databases, warehouses, or federated query engines—guides architecture decisions.

## Managed relational databases

| Service             | Highlights                                                      | Exam focus                                             |
| ------------------- | --------------------------------------------------------------- | ------------------------------------------------------ |
| `Amazon RDS`        | Managed MySQL, PostgreSQL, MariaDB, Oracle, SQL Server          | Backups, Multi-AZ, read replicas, parameter groups     |
| `Amazon Aurora`     | MySQL/PostgreSQL compatible, distributed storage, Serverless v2 | Global Database, parallel query, auto-scaling capacity |
| `Amazon RDS Custom` | Gives OS-level access for Oracle & SQL Server                   | When workloads need custom agents or host-level tuning |

- Use read replicas for reporting workloads; promote to standalone instance during DR.
- Enable IAM database authentication (MySQL/Aurora) to centralize credential management.
- For migration, combine `AWS DMS` with `Schema Conversion Tool` to modernize legacy engines.

## Data warehousing and analytics

| Service                                | SQL engine traits                                            | Cost levers                                            |
| -------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| `Amazon Redshift`                      | Columnar storage, MPP architecture, ANSI SQL with extensions | RA3 managed storage, concurrency scaling, result cache |
| `Amazon Athena`                        | Presto-based serverless query service over S3                | Pay per TB scanned; compress and partition data        |
| `Amazon EMR` (Hive, Presto, Spark SQL) | Elastic clusters running open-source SQL engines             | Spot instances, right-sizing nodes, auto-scaling       |

- Redshift Spectrum extends Redshift SQL to external tables on S3—ideal for staging data without loading.
- Use materialized views to pre-compute aggregations; refresh incrementally for dashboards.
- In Athena, define tables in AWS Glue Data Catalog; leverage `CREATE TABLE AS SELECT (CTAS)` for transforming data into columnar formats.

## Serverless and federated options

- `AWS Glue Interactive Sessions` allow ad-hoc Spark SQL without managing clusters.
- `Amazon Athena Federated Query` connects to RDS, Redshift, DynamoDB, or external JDBC sources via connectors.
- `Amazon Redshift Data API` provides HTTPS access to execute SQL without managing persistent connections.
- `AWS Lake Formation` grants fine-grained permissions for Glue/Athena SQL access across data lakes.

## Security and governance

- Combine IAM policies with database roles; for example, grant analysts IAM access to `redshift:GetClusterCredentials` and attach SQL role privileges.
- Use parameter groups to enforce SSL connections and password policies on RDS instances.
- Enable auditing: RDS Enhanced Monitoring, Aurora database activity streams, and Redshift audit logs in CloudWatch or S3.
- Tag resources and integrate with AWS Config rules to identify publicly accessible SQL endpoints.

## Operational playbook

- Automate schema migrations with tools like AWS CodeBuild + Flyway or Liquibase pipelines.
- Schedule maintenance windows for RDS to apply patches; Multi-AZ keeps downtime minimal.
- Configure Redshift snapshots; cross-region copy supports DR requirements.
- In Athena, manage Data Catalog versions and monitor query history for cost anomalies.

## Exam tips

- Map workload type to service: OLTP -> RDS/Aurora, OLAP -> Redshift, ad hoc -> Athena.
- Remember pricing units: RDS instance-hours + storage; Redshift node-hours; Athena per TB scanned.
- Highlight integration points (e.g., SageMaker consuming Redshift via Data Wrangler) when asked about ML pipelines.
- Watch for questions on security boundaries—network-level (VPC, SG) plus SQL-level controls.
