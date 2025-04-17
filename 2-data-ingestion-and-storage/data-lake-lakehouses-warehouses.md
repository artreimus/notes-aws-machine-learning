**Data Warehouses**

**Definition & Purpose**  
A **data warehouse** is a centralized, **schema‑on‑write** repository optimized for analytical querying over large volumes of **structured** data. Data from operational systems is **extracted**, **transformed** (cleaned, conformed, aggregated) and **loaded** (ETL) into a star or snowflake schema. The warehouse serves read‑heavy workloads—OLAP, reporting, BI dashboards and pre‑computed analytics.

**Core Architecture Components**

1. **Ingestion Layer**
   - Batch connectors (AWS DMS, AWS Glue)
   - Data validation, cleansing & conforming
2. **Storage & Schema**
   - Star or snowflake schemas
   - Columnar storage for fast aggregations
3. **Query Engine**
   - Optimized for complex joins, window functions, aggregations
   - Data marts and materialized views for performance
4. **Access & Security**
   - IAM roles, VPC endpoints, encryption (KMS, SSL/TLS)
5. **Monitoring & Management**
   - Workload management (WLM, concurrency scaling)
   - Performance dashboards

**AWS Example**

- **Amazon Redshift**: MPP columnar, Spectrum for external queries, RA3 nodes with managed storage

---

**Data Lakes**

**Definition & Purpose**  
A **data lake** is a centralized, **schema‑on‑read** repository that ingests **raw** data—structured, semi‑structured, and unstructured—in its native formats. It supports ELT: you **extract** and **load** first, then **transform** later for specific analytics, ML, or exploration.

**Core Architecture Components**

1. **Ingestion Zone**
   - S3 “landing” buckets; streaming via Kinesis Firehose, MSK
2. **Storage Layer**
   - Amazon S3 with lifecycle policies (Glacier, Intelligent‑Tiering)
3. **Metadata & Governance**
   - AWS Glue Data Catalog / Lake Formation
4. **Processing & Transformation**
   - AWS Glue ETL, EMR, Lambda, Glue Elastic Views
   - Athena, Redshift Spectrum for SQL-on-S3
5. **Serving & Consumption**
   - Curated zones; ML feature stores; OpenSearch for logs; BI tools

**AWS Example**

- **S3 + Glue + Athena**: raw JSON → Glue crawler → Athena queries or parquet conversion

---

**Data Lakehouses**

**Definition & Purpose**  
A **lakehouse** combines the low‑cost, scalable storage of a data lake with the performance and transactional integrity of a data warehouse. It supports both **schema‑on‑write** (for curated, high‑performance tables) and **schema‑on‑read** (for raw data exploration), unifying ETL and ELT patterns.

**Core Architecture Components**

1. **Unified Storage**
   - Data in S3 using open formats (Parquet, ORC) with transaction logs (Delta Lake, Apache Hudi, Iceberg)
2. **Metadata & Transactions**
   - Lake Formation for access controls; open‑table formats for ACID guarantees
3. **Query Engine & Compute**
   - Redshift Spectrum, Athena, EMR Spark, or specialized engines (Databricks Runtime)
4. **Governance & Optimization**
   - Schema enforcement, versioning, compaction & indexing
5. **Workloads Supported**
   - BI/reporting, ad‑hoc SQL, real‑time analytics, ML training & serving

**AWS Example**

- **Lake Formation + S3 + Redshift Spectrum**: raw zone + curated tables in S3 → Lake Formation catalogs & secures them → Redshift Spectrum queries with warehouse‑grade performance

---

**Key Comparisons**

| Aspect           | Data Warehouse       | Data Lake                           | Data Lakehouse                                 |
| ---------------- | -------------------- | ----------------------------------- | ---------------------------------------------- |
| **Schema**       | On write (fixed)     | On read (flexible)                  | Both: on write for curated, on read for raw    |
| **Data Types**   | Structured only      | All types                           | All types                                      |
| **Ingestion**    | ETL                  | ELT                                 | ELT + managed transforms                       |
| **Transactions** | ACID                 | None                                | ACID via open‑table formats                    |
| **Query Model**  | SQL‑optimized        | SQL via Athena/Spectrum; custom     | SQL via multiple engines; real‑time & batch    |
| **Cost Profile** | Higher TCO           | Low storage, pay‑per‑query compute  | Moderate; optimizes storage & compute          |
| **Flexibility**  | Rigid schema changes | Highly flexible                     | Flexible with curated performance zones        |
| **Use Cases**    | BI, dashboards       | Exploratory analytics, ML, archives | Unified analytics & ML, single-copy governance |

---

**Choosing the Right Architecture**

- **Data Warehouse**
  - Predefined, stable schemas; stringent SLAs on query latency; primary BI/reporting use.
- **Data Lake**
  - Heterogeneous data at scale; exploratory analytics; cost‑efficient archival.
- **Data Lakehouse**
  - Need both rapid BI performance and ML/ELT flexibility on the same data platform.
