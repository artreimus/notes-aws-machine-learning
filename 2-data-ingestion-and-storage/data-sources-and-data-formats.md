## Common Data Sources

When building ETL/ELT pipelines, your raw data may originate from many different places. Understanding each source’s characteristics helps you choose the right connector, handle authentication, and ensure data quality.

| Source Type                     | Interface / Protocol                                                           | Characteristics & Considerations                                                                                                                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Relational Databases**        | **JDBC** (Java Database Connectivity)<br>**ODBC** (Open Database Connectivity) | • JDBC is Java‑based, platform‑independent, but requires Java client libraries.<br>• ODBC is language‑agnostic but driver‑dependent per platform.<br>• Typical use: batch extracts from Oracle, MySQL, SQL Server, PostgreSQL. |
| **SaaS & Web Services**         | **RESTful APIs**, **SOAP**                                                     | • HTTP/HTTPS endpoints returning JSON, XML, or CSV payloads.<br>• Must manage rate limits, auth (API keys, OAuth), pagination.                                                                                                 |
| **Flat Files & Object Storage** | Local/Network file systems, Amazon S3, HDFS                                    | • Plain‑text logs (e.g., Apache, application logs) or exported CSVs.<br>• Files arrive via SFTP, manual drop, or event notifications (S3 PUT events).                                                                          |
| **Streaming Platforms**         | **Apache Kafka** / **MSK**, **Amazon Kinesis Data Streams**                    | • High‑throughput, low‑latency event streams.<br>• Consumers use partition/offset bookmarks; must handle ordering, backpressure.                                                                                               |
| **NoSQL & Document Stores**     | Native drivers (e.g., MongoDB, DynamoDB)                                       | • Semi‑structured JSON documents or key/value pairs.<br>• Often used for clickstream, user profiles, session data.                                                                                                             |

---

## Common Data Formats

| Format       | Description                                                                                            | Pros                                                                                     | Cons                                                                                   | Common Systems                          |
| ------------ | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------- |
| **CSV**      | Comma‑separated (or other delimiter) text file where each row is a record and each value is a field.   | • Human‑readable & editable<br>• Universally supported<br>• Easy import/export           | • No native schema enforcement<br>• Inefficient storage & parsing at scale             | RDBMS imports/exports, pandas, AWS Glue |
| **JSON**     | Text‑based, hierarchical key/value format that can represent nested objects and arrays.                | • Flexible schema<br>• Human‑readable<br>• Great for semi‑structured data                | • Can be verbose (larger file size)<br>• Parsing overhead for deep nesting             | REST APIs, NoSQL DBs, Lambda            |
| **Avro**     | Binary format that bundles each record with its JSON‑defined schema for compact, self‑describing data. | • Compact, fast serialization<br>• Schema evolution support<br>• Excellent for streaming | • Not human‑readable<br>• Requires schema registry or shared schema files              | Kafka/MSK, Spark, Flink, Hadoop         |
| **Parquet**  | Columnar binary file format optimized for analytics, storing data by column chunks rather than rows.   | • Highly efficient compression & I/O<br>• Selective column reads → faster queries        | • Write performance can be slower for small jobs<br>• Not ideal for row‑by‑row updates | Spark, Hive, Redshift Spectrum, Athena  |
| **ORC**      | Optimized Row Columnar format, a columnar storage format for Hadoop ecosystem.                         | • High compression<br>• Fast read performance<br>• Efficient for analytics               | • Not human‑readable<br>• Less widely supported than Parquet outside Hadoop            | Hive, Spark, Amazon Athena, EMR         |
| **RecordIO** | Binary format for serializing records, commonly used in ML pipelines.                                  | • Efficient for streaming and batch ML<br>• Simple structure<br>• Supported by SageMaker | • Not human‑readable<br>• Limited ecosystem outside ML tooling                         | Amazon SageMaker, MXNet                 |

---

### Usage Patterns & Tips

1. **When to use JDBC vs. ODBC**

   - If your ETL code is Java‑native, JDBC avoids extra layers.
   - For Python, .NET or other languages, ODBC (via appropriate drivers) or language‑specific connectors (e.g., psycopg2 for PostgreSQL) may be more convenient.

2. **Choosing file formats**

   - **Small, ad‑hoc datasets** → CSV for its simplicity.
   - **Config files or lightweight data exchange** → JSON for readability and nested structures.
   - **High‑volume, schema‑evolving streams** → Avro to co‑locate schema with data.
   - **Analytical queries over large tables** → Parquet for column‑pruning and compression.

3. **Combining sources & formats**
   - A typical pipeline might extract JSON payloads from REST APIs, store them raw in S3, then transform and write out partitioned Parquet tables for fast, cost‑effective analytics via Athena or Redshift Spectrum.
