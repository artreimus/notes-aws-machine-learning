# Glue

---

## 1. What is AWS Glue?

- **Serverless**: Fully managed ETL (Extract, Transform, Load) service—no infrastructure to provision or manage.
- **Data Catalog & Discovery**: Automatic discovery and definition of table definitions and schema across various data stores.
- **Supported Data Sources**:
  - Amazon S3 (data lakes)
  - Amazon RDS
  - Amazon Redshift
  - Amazon DynamoDB
  - Most other SQL databases via JDBC
  - Custom ETL jobs and scripts
- **Execution Modes**: Jobs can be triggered on-demand, on a schedule (via Glue Scheduler or cron expressions), or in response to events (via triggers).
- **Managed Spark**: Uses Apache Spark under the hood, allowing Spark or PySpark scripts, with options to scale via DPUs (Data Processing Units).
- **Security & Monitoring**:
  - Encryption at rest (server-side) and in transit (SSL)
  - Integration with AWS KMS for customer-managed keys
  - Logs and metrics via Amazon CloudWatch; notifications via SNS

---

## 2. Glue and S3 Partitions

- **Partition Discovery**: A Glue Crawler infers table partitions based on your S3 object key structure.
- **Partition Design Considerations**:
  - If querying by time ranges: organize buckets like `s3://bucket/yyyy/mm/dd/device/`
  - If querying by device: organize buckets like `s3://bucket/device/yyyy/mm/dd/`
- **Performance**: Proper partitioning reduces data scanned and improves query performance in Athena, Redshift Spectrum, and EMR.

---

## 3. Glue Crawler & Data Catalog

- **Glue Crawler**:
  - Scans data in S3 (or other sources) to infer schema and partitions
  - Can be scheduled to run periodically
- **Glue Data Catalog**:
  - Stores table definitions, schemas, and partition metadata
  - Leaves underlying data in place (e.g., in S3)
  - Acts as a central metadata store for:
    - Amazon Athena
    - Amazon Redshift Spectrum
    - Amazon EMR (Hive, Spark)
    - Amazon QuickSight

---

## 4. Glue & Hive

- AWS Glue Data Catalog can serve as a **Hive metastore** for EMR clusters.
- Option to **import** existing Hive metastores into Glue for unified metadata management.

---

## 5. Glue ETL

- **Automatic Code Generation**: Generates Scala or Python (PySpark) code based on visual or predefined transforms.
- **Job Configuration**:
  - Event-driven, scheduled, or on-demand triggers
  - Scale via additional DPUs for Spark job throughput
  - Enable job bookmarking to track processed data and avoid reprocessing
- **Monitoring & Notifications**:
  - Error and progress metrics to CloudWatch
  - Integrate with SNS for alerting

---

## 6. Glue ETL Components & Concepts

### 6.1 DynamicFrame & DynamicRecord

- **DynamicFrame**: A distributed collection of self-describing records with schema, similar to Spark DataFrame but ETL-centric.
- **DynamicRecord**: Individual record within a DynamicFrame; carries its own schema metadata.
- **API Usage**:
  ```scala
  val source = glueContext.getCatalogSource(
    database = "githubarchive_month", tableName = "data"
  )
  val mapped = source.applyMapping(Seq(
    ("id","string","id","long"),
    ("type","string","type","string"),
    // ... more mappings ...
  ))
  ```

### 6.2 Transformations

- **Built-in Transforms**:
  - `DropFields`, `DropNullFields`
  - `Filter` (custom record filters)
  - `Join` (data enrichment)
  - `Map` (add/remove fields, lookups)
- **Machine Learning Transforms**:
  - `FindMatchesML` for fuzzy/match deduplication
- **Format Conversions**: CSV, JSON, Avro, Parquet, ORC, XML
- **Apache Spark**: Execute native Spark transforms (e.g., K-Means)
- **Interoperability**: Convert between DynamicFrame and Spark DataFrame

### 6.3 ResolveChoice

- Handles schema ambiguities (e.g., columns with multiple types):
  - `make_cols`: create separate columns per type
  - `cast`: cast to a single type
  - `make_struct`: nest types in a struct
  - `project`: project all values to a single type

### 6.4 Catalog Updates in ETL

- **Partition & Schema Updates**:
  - Use crawler or script options (`enableUpdateCatalog`, `partitionKeys`, `updateBehavior`, `setCatalogInfo`) to add partitions, update schemas, or create new tables
- **Limitations**:
  - S3 sources only
  - Supported formats: JSON, CSV, Avro, Parquet (with special handling)
  - No nested schema updates

---

## 7. Development Endpoints

- **Purpose**: Iterative ETL script development in notebooks (Zeppelin, SageMaker, PyCharm).
- **Setup**: Endpoint in a VPC; access via:
  - Apache Zeppelin (local or EC2)
  - SageMaker notebooks
  - Remote IDEs (e.g., PyCharm)
- **Networking**: Use Elastic IPs and security groups for secure access

---

## 8. Running Glue Jobs

- **Scheduling**:
  - Time-based (cron syntax)
  - Event-driven (CloudWatch Events to Lambda, SNS, Step Functions)
- **Job Bookmarks**:
  - Track processed data for incremental runs
  - Works with S3 sources and JDBC sources (for new rows only)
- **Post-Run Actions**:
  - Emit CloudWatch Events on success/failure
  - Trigger downstream workflows (Lambda, Step Functions, Kinesis, EC2)

---

## 9. Cost Model

- **GLUE Crawler & ETL**: Billed per second
- **Data Catalog**: First 1 million objects and accesses free
- **Development Endpoints**: Charged per minute of usage

---

## 10. Anti-Patterns & Streaming

- **Anti-Pattern**: Mixing multiple ETL engines (e.g., Hive/Pig vs. Glue Spark). If non-Spark engines are needed, consider AWS Data Pipeline with EMR.
- **Streaming Support** (April 2020+): Serverless streaming ETL on Spark Structured Streaming consuming from Kinesis or Kafka, with in-flight transformation and output to S3 or other stores.

---

## 11. AWS Glue Studio

- **Visual ETL**: Drag-and-drop job designer for complex DAGs
- **Supported Sources**: S3, Kinesis, Kafka, JDBC
- **Features**:
  - Partitioning support
  - Job dashboards with run metrics and logs

---

## 12. AWS Glue Data Quality

- **Rule Definitions**: Manual or auto-suggested data quality rules
- **Integration**: Embed quality checks in ETL jobs
- **Execution**: Use Data Quality Definition Language (DQDL)
- **Reporting**: Output results to CloudWatch or fail jobs on rule violations

---

## 13. AWS Glue DataBrew

- **Visual Data Prep**: No-code UI for data cleansing and transformation
- **Recipes**: Sequence of transformation steps (over 250 pre-built operations)
- **Integrations**: Input from S3, Redshift, Snowflake, databases; output to S3
- **Security**: SSL in transit, IAM policies, KMS for encryption
- **Sample Action**:
  ```json
  {
    "RecipeAction": {
      "Operation": "NEST_TO_MAP",
      "Parameters": {
        "sourceColumns": ["age", "weight_kg", "height_cm"],
        "targetColumn": "columnName",
        "removeSourceColumns": "true"
      }
    }
  }
  ```

### 13.1 Handling PII in DataBrew

- **Profile Jobs**: Enable PII statistics detection
- **Transformations**:
  - Substitution: `REPLACE_WITH_RANDOM_*`
  - Shuffling: `SHUFFLE_ROWS`
  - Encryption: deterministic (`DETERMINISTIC_ENCRYPT`) or probabilistic (`ENCRYPT`)
  - Decryption: `DECRYPT`
  - Removal: `DELETE`, `NULLIFY`
  - Masking: `MASK_CUSTOM`, `MASK_DATE`, `MASK_DELIMITER`, `MASK_RANGE`
  - Hashing: `CRYPTOGRAPHIC_HASH`

---

_End of notes._
