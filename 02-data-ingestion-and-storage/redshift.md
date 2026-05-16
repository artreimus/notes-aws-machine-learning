---
title: "Amazon Redshift, Redshift ML, Redshift Serverless, and Redshift Data API"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "draft"
domain:
  - "1.1"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "02_data_ingestion_and_storage"
aliases:
  - "Amazon Redshift, Redshift ML, Redshift Serverless, and Redshift Data API"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Redshift, Redshift ML, Redshift Serverless, and Redshift Data API

## Overview

### Amazon Redshift

Amazon Redshift is AWS's fully managed, petabyte-scale cloud data warehouse service. It enables fast query performance using columnar storage, massively parallel processing (MPP), and advanced compression. Redshift is designed for online analytic processing (OLAP) workloads, supporting complex queries across large datasets, and integrates seamlessly with the AWS analytics and ML ecosystem.

### Redshift ML

Redshift ML brings machine learning directly to your data warehouse by allowing you to create, train, and deploy ML models using SQL commands. It leverages Amazon SageMaker under the hood, abstracting the complexity of ML infrastructure and making predictive analytics accessible to SQL users.

### Redshift Serverless

Redshift Serverless allows you to run and scale analytics without managing data warehouse infrastructure. You pay for the compute used per query or per workload, making it ideal for variable or unpredictable workloads.

### Redshift Data API

The Redshift Data API enables you to access Redshift clusters and serverless endpoints using HTTPS, without the need for persistent database connections or drivers. It's ideal for serverless applications, automation, and integration with AWS Lambda, Step Functions, and more.

---

## AWS Services & Features

### Amazon Redshift

- **Columnar Storage**: Optimized for analytical queries.
- **Massively Parallel Processing (MPP)**: Distributes queries across multiple nodes for high performance.
- **Spectrum**: Query exabytes of data directly in S3 without loading it into Redshift.
- **Concurrency Scaling**: Automatically adds capacity to handle spikes in query load.
- **RA3 Nodes & Managed Storage**: Decouples compute and storage for flexible scaling.
- **Data Sharing**: Securely share live data across Redshift clusters and accounts.
- **Security**: VPC, encryption at rest/in transit, IAM integration, audit logging.
- **Integration**: Works with AWS Glue, S3, SageMaker, Kinesis, and more.

### Redshift ML

- **SQL-Based ML**: Create, train, and deploy ML models using familiar SQL syntax.
- **SageMaker Integration**: Uses SageMaker Autopilot for model selection and training.
- **Supported Tasks**: Regression, binary/multiclass classification, and custom models.
- **Inference in SQL**: Run predictions directly in your SELECT statements.
- **Model Explainability**: Generate feature importance explanations for predictions.

### Redshift Serverless

- **No Cluster Management**: Instantly provisioned endpoints.
- **Pay-per-Use**: Billed for compute used (RPU-hours).
- **Seamless Scaling**: Automatically adjusts resources for workload demands.
- **Integrated Security**: IAM, VPC, encryption, and audit logging.

### Redshift Data API

- **HTTPS Access**: Query Redshift from applications without JDBC/ODBC drivers.
- **Stateless**: No need to manage persistent connections.
- **Integration**: Works with Lambda, Step Functions, SDKs, and automation tools.
- **IAM Authentication**: Secure, fine-grained access control.

---

## Practical Application

### Amazon Redshift

- **Data Warehousing**: Centralize and analyze data from multiple sources (S3, RDS, DynamoDB, on-premises).
- **Business Intelligence**: Power dashboards and analytics tools (e.g., Tableau, QuickSight).
- **Data Lake Integration**: Use Redshift Spectrum to query S3 data lakes.
- **ML-Driven Analytics**: Integrate with Redshift ML for predictive insights.

**Sample Architecture:**

- Data ingested into S3 → ETL with Glue → Loaded into Redshift → BI/ML workloads.

### Redshift ML

- **Predictive Analytics**: Churn prediction, demand forecasting, fraud detection, etc., directly in SQL.
- **Operational ML**: Embed predictions in dashboards, reports, or downstream applications.
- **Model Lifecycle**: Train, deploy, and update models without leaving Redshift.

#### Example: Training, Inference, and Explainability in Redshift ML

**1. Training a Model**

```sql
CREATE MODEL churn_model
FROM (SELECT age, tenure, monthly_spend, is_churn FROM customers)
TARGET is_churn
FUNCTION my_churn_predict
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
SETTINGS (S3_BUCKET 'my-redshift-ml-bucket');
```

- `CREATE MODEL`: Trains a model using the specified data and target column.
- `FUNCTION`: The name of the SQL function for inference.
- `IAM_ROLE`: Grants Redshift permission to use SageMaker and S3.
- `SETTINGS`: Additional options (e.g., S3 bucket for artifacts).

**2. Running Inference**

```sql
SELECT customer_id, my_churn_predict(age, tenure, monthly_spend) AS predicted_churn
FROM customers
WHERE region = 'US';
```

- Calls the generated function to predict churn for each customer.

**3. Explaining Predictions**

```sql
SELECT customer_id, my_churn_predict_explain(age, tenure, monthly_spend) AS explanation
FROM customers
WHERE customer_id = 123;
```

- Returns feature importance for the prediction (requires model explainability to be enabled during training).

### Redshift Serverless

- **Ad Hoc Analytics**: Run analytics without provisioning clusters.
- **Burst Workloads**: Handle unpredictable or spiky workloads efficiently.
- **Dev/Test Environments**: Quickly spin up isolated environments for experimentation.

### Redshift Data API

- **Serverless App Integration**: Query Redshift from Lambda, Step Functions, or web apps.
- **Automation**: Run scheduled queries, ETL jobs, or reporting tasks without managing connections.
- **CI/CD Pipelines**: Integrate Redshift queries into deployment workflows.

---

## Challenges & Best Practices

### Amazon Redshift

- **Data Distribution & Sort Keys**: Poor key design can lead to performance bottlenecks. Analyze query patterns and use distribution/sort keys wisely.
- **Vacuum & Analyze**: Regularly run VACUUM and ANALYZE to maintain performance.
- **Concurrency**: Use concurrency scaling and workload management (WLM) to handle spikes.
- **Cost Management**: Monitor usage, leverage RA3 nodes, and use Reserved Instances for predictable workloads.
- **Security**: Always use encryption, VPC, and IAM best practices.

### Redshift ML

- **Data Preparation**: Clean, impute, and normalize data before training.
- **Model Complexity**: Autopilot may not always select the best model for complex tasks; consider custom models if needed.
- **Resource Usage**: Training large models can impact Redshift performance; monitor and schedule accordingly.
- **Explainability**: Enable explainability if you need feature importance, but note it may increase training time.

### Redshift Serverless

- **Cost Spikes**: Monitor usage to avoid unexpected costs from bursty workloads.
- **Resource Limits**: Be aware of quotas and scaling limits.

### Redshift Data API

- **Latency**: Slightly higher latency than direct connections; not ideal for high-frequency, low-latency workloads.
- **Timeouts**: Long-running queries may require polling for results.

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
