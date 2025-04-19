**1. ETL vs ELT: Core Concepts**

- **ETL (Extract → Transform → Load)**
  - **Schema‑on‑write** pattern: transform data _before_ loading into the target system.
  - Ideal for data warehouses with fixed schemas and performance SLAs.
- **ELT (Extract → Load → Transform)**
  - **Schema‑on‑read** pattern: load raw data into a data lake (or lakehouse) first, then transform as needed.
  - Enables flexible, ad‑hoc transformations for analytics, machine learning, or varied downstream consumers.

---

**2. “E”: Extract**

- **Purpose**: Retrieve raw data from one or more sources.
- **Common Sources**:
  - Relational databases (Oracle, MySQL, PostgreSQL)
  - SaaS APIs (Salesforce, Google Analytics)
  - Flat files (CSV, log files) in on‑premise or S3
  - Streaming platforms (Kafka, Kinesis)
- **Key Considerations**:
  - **Data integrity**: implement retry logic, idempotent reads, watermarking or checkpoints
  - **Latency requirements**: batch windows vs. real‑time (micro‑batches or continuous pulls)
  - **Authentication & throughput**: use VPC endpoints, parallel reads, or AWS DMS for homogeneous migrations

---

**3. “T”: Transform**

- **Purpose**: Cleanse, conform, enrich, and reshape data into the desired schema/format.
- **Common Transformations**:
  - **Cleansing**: remove duplicates, filter invalid rows, normalize encodings
  - **Type casting**: strings → dates, text → numeric codes, JSON flattening
  - **Business logic**: computing totals, averages, rolling windows, lookup joins
  - **Enrichment**: geocoding IPs, assigning customer tiers, sessionization of clickstreams
  - **Format conversion**: CSV/JSON → Parquet/ORC for columnar efficiency
- **On‑demand vs. Pre‑computed**:
  - In ETL, transforms run once per load.
  - In ELT, transforms may be parametrized and triggered per analytical job or ML pipeline.

---

**4. “L”: Load**

- **Purpose**: Write transformed (or raw) data into the target store.
- **Targets**:
  - **Data Warehouse**: Amazon Redshift, RDS/Aurora
  - **Data Lake**: Amazon S3 (raw and curated zones)
  - **Operational Stores**: DynamoDB, Elasticsearch/OpenSearch, time‑series databases
- **Key Considerations**:
  - **Batch vs. Streaming**: COPY vs. single‑row inserts vs. Kinesis Data Firehose delivery
  - **Data integrity**: transactional writes, checkpointing, dead‑letter queues for failures
  - **Partitioning & indexing**: date/time partitions on S3, distribution keys in Redshift

---

**5. Orchestration & Automation**  
Building reliable pipelines means wiring these steps together, handling dependencies, retries, and notifications:

| Tool / Service                                  | Role                                                                                   |
| ----------------------------------------------- | -------------------------------------------------------------------------------------- |
| **AWS Glue Workflows**                          | Native orchestration for Glue jobs & crawlers; visual DAG editor                       |
| **Amazon Managed Workflows for Apache Airflow** | Production‑grade DAG scheduling; Airflow operators for Glue, EMR, Lambda, Redshift     |
| **AWS Step Functions**                          | Serverless state machines; branching, retries, parallel branches, human‑approval waits |
| **Amazon EventBridge**                          | Event‑driven triggers (S3 object creation, API calls) to kick off workflows or Lambda  |
| **AWS Lambda**                                  | Glue simple micro‑transforms; glue-less pipelines; lightweight task steps              |

**Typical Orchestration Patterns**

1. **Scheduled Batch**
   - EventBridge cron rule → Step Functions → Glue extract job → Glue transform job → Redshift COPY
2. **Event‑Driven ELT**
   - S3 “landing” upload event → Glue crawler (catalog) → Glue ETL job that writes Parquet to “curated” bucket → Athena query
3. **Hybrid Workflows**
   - Airflow DAG coordinating EMR Spark transforms, Lambda for metadata registration, and Redshift data loads

---

**6. Practical Scenario**

> **Customer 360 Pipeline**
>
> 1. **Extract** CRM records nightly via AWS DMS into S3 raw bucket.
> 2. **Transform** with AWS Glue: cleanse addresses, dedupe contacts, enrich with demographic lookup.
> 3. **Load** into Redshift using the COPY command.
> 4. **Orchestrate** via Step Functions: on DMS completion, trigger Glue; on Glue success, notify via SNS and refresh BI dashboards.

---

**7. Common Challenges & Best Practices**

- **Error Handling & Idempotency**
  - Use step functions’ built‑in retry/​catch; build idempotent transforms (e.g., dedupe on primary key).
- **Performance Tuning**
  - Parallelize extracts; use partition pruning in Athena/Redshift Spectrum; choose optimal file sizes (128 MB+).
- **Cost Management**
  - Use serverless (Glue 2.0, Athena) where possible; monitor with CloudWatch; tear down dev resources.
- **Monitoring & Observability**
  - Leverage CloudWatch Logs/Metrics, Glue job bookmarks, Airflow UI, and custom dashboards for SLA tracking.
