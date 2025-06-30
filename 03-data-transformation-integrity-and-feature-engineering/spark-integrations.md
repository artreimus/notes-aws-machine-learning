# Apache Spark & AWS Integration Notes

## 1. Why integrate?

- **Apache Spark** excels at large‑scale data processing and feature engineering.
- **Amazon SageMaker** offers managed training, tuning, deployment, and MLOps, so you don’t have to build custom ML infrastructure.
- **Amazon S3** is the central, durable storage layer—Spark reads/writes directly; SageMaker automatically pulls training data and pushes model artifacts there.

---

## 2. High‑level architecture patterns

| Pattern                             | Flow                                                                                                                                                                      |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ML Training pipeline**            | Spark on EMR/Glue processes raw data → writes to S3 → `sagemaker‑pyspark` (or boto3) launches SageMaker Training Job → model artifact in S3 → register in Model Registry. |
| **Batch inference**                 | Spark reads S3 data → invokes SageMaker Batch Transform job → writes scored results to S3/Glue table.                                                                     |
| **Row‑level / real‑time inference** | Define a Spark UDF that calls a SageMaker endpoint; Spark executors fan‑out REST calls.                                                                                   |
| **Feature pipelines**               | Spark creates curated features → stores to SageMaker Feature Store (offline = S3, online = DynamoDB) using `sagemaker‑feature‑store‑pyspark`.                             |

---

## 3. Key libraries & connectors

| Library                                 | Latest stable (Jun 2025) | Purpose / Notes                                                                                        |
| --------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------ |
| `sagemaker‑pyspark`                     | 1.6.x                    | Bridges Spark DataFrames ↔ SageMaker Estimator/Transformer APIs; runs on EMR, Glue, local Spark.       |
| `SageMakerEstimator`                    | 1.6.x                    | Allows tight integration between Spark and SageMaker for several models including XGBoost. Simplifies launching SageMaker jobs from Spark. |
| `sparkmagic`                            | 0.21.x                   | Jupyter magics (`%%spark`, `%%sql`) to run Spark jobs from SageMaker Studio or EMR Notebooks via Livy. |
| `pyspark`                               | 3.5.x                    | Native Python API for Spark.                                                                           |
| `hadoop‑aws` + `aws‑java‑sdk‑bundle`    | 3.5.x                    | Enables high‑performance `s3a://` connector. Already bundled in EMR 7.x.                               |
| `awswrangler`                           | 3.10.x                   | Pandas/Spark friendly helper for S3, Glue, Redshift, Athena.                                           |
| `delta‑spark` / `iceberg‑spark‑runtime` | 3.2+                     | Table formats that bring ACID/time‑travel to S3 data lakehouses.                                       |
| `boto3` / `sagemaker` SDK               | 1.35.x / 2.226.x         | Low‑level orchestration of SageMaker jobs, endpoints, pipelines.                                       |
| `aws‑glue‑libs`                         | v4                       | Glue‑specific Spark and catalog helpers.                                                               |
| `sagemaker‑feature‑store‑pyspark`       | 0.3.x (preview)          | Write/read SageMaker Feature Store from Spark DF.                                                      |

> **Tip:** Match versions of `pyspark`, `hadoop‑aws`, and `aws‑java‑sdk‑bundle` to avoid shaded JAR conflicts.

---

## 3a. SageMakerEstimator notes

The `SageMakerEstimator` classes allow tight integration between Spark and SageMaker for several models including XGBoost, and offer the simplest solution for distributed ML from Spark. Note:

- You can't deploy SageMaker training jobs to an EMR cluster; SageMaker runs jobs on its own managed infrastructure.
- XGBoost on SageMaker requires input data in LibSVM or CSV format, not RecordIO.
- The Spark driver launches the SageMaker job; Spark executors do not participate in the training itself.

---

## 4. Configuring S3 connectivity in Spark

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
        .appName("s3-example")
        .config("fs.s3a.aws.credentials.provider",
                "com.amazonaws.auth.InstanceProfileCredentialsProvider")
        .config("fs.s3a.endpoint", "s3.amazonaws.com")
        .getOrCreate()
)
```

- Use **IAM Instance Profiles / Roles** attached to EMR, Glue, or SageMaker Studio—not static keys.
- Prefer the `s3a://` scheme for parallel, multithreaded IO.

---

## 5. Launching a SageMaker Training Job from Spark (`sagemaker‑pyspark`)

```python
from sagemaker_pyspark import SageMakerEstimator
from sagemaker.inputs import TrainingInput

iris_s3 = "s3://my-bucket/iris.csv"

estimator = SageMakerEstimator(
    training_image="763104351884.dkr.ecr.us-east-1.amazonaws.com/xgboost:1.7-1",
    role="arn:aws:iam::123456789012:role/MySageMakerRole",
    train_instance_count=1,
    train_instance_type="ml.m5.xlarge",
    sagemaker_input_options={
        "train": TrainingInput(iris_s3, content_type="text/csv")
    },
    schema={
        "features": "vector",
        "label": "double"
    }
)

model = estimator.fit(df)  # df is a Spark DataFrame
```

**How it works**

- The Spark **driver** downloads a small wrapper JAR → calls SageMaker API.
- Executors don’t participate in training; resources are in the separate SageMaker cluster.

---

## 6. Batch Transform or Endpoint inference from Spark

```python
from sagemaker_pyspark import SageMakerTransformer

transformer = SageMakerTransformer(
    model_name=model.model_name,
    instance_count=2,
    instance_type="ml.m5.large",
    transform_output_path="s3://my-bucket/batch-out/",
)

transformer.transform(inputDF)  # inputDF = Spark DataFrame
```

For real‑time endpoints:

```python
from pyspark.sql.functions import udf
import boto3, json, base64

runtime = boto3.client("sagemaker-runtime")

def invoke_endpoint(payload):
    resp = runtime.invoke_endpoint(
        EndpointName="my-endpoint",
        ContentType="application/json",
        Body=json.dumps(payload)
    )
    return json.loads(resp["Body"].read())

endpoint_udf = udf(invoke_endpoint, returnType="string")
scored_df = raw_df.withColumn("prediction", endpoint_udf("features"))
```

---

## 7. Using Sparkmagic inside SageMaker Studio

```bash
# In a Jupyter cell
%%spark
spark.range(10).show()
```

- Requires a **SparkMagic** kernel or “**Data Wrangler**” image.
- Back‑end cluster options: EMR (via Livy), Glue interactive sessions, or local Spark within Studio.
- Good for ad‑hoc visualization and joining data from multiple sources.

---

## 8. Best practices & tips

1. **Keep roles minimal** – separate EMR/Glue role from SageMaker execution role.
2. **Partition S3 writes** (e.g., `dt=2025-06-23`) to maximize parallelism.
3. **Use EMR Serverless/Glue 4.0** for on‑demand, cost‑efficient Spark without cluster ops.
4. **Cache small lookup tables** in Spark broadcast variables to avoid repeated S3 fetches.
5. **Monitor cost** – `sagemaker.Estimator(spot=True)` or managed Spot Training can cut 50–70%.
6. **Artifact sharing** – Register models in SageMaker Model Registry; reference them by ARN in downstream Spark pipelines.
7. **Version pinning** – Pin exact JAR/Python versions in `requirements.txt` and EMR `--packages` to avoid runtime surprises.

---

## 9. Troubleshooting

| Symptom                                         | Likely Cause                                                 | Fix                                                                      |
| ----------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `java.lang.NoSuchMethodError` involving AWS SDK | Version clash between `hadoop‑aws` and `aws‑java‑sdk‑bundle` | Align both to Spark’s minor version (e.g., 3.5.0) or use EMR’s built‑ins |
| `403 AccessDenied` on S3                        | Missing IAM permission or using default Hadoop S3n scheme    | Attach correct role; switch S3 path to `s3a://`                          |
| Slow write throughput                           | Small output files or no multipart upload                    | Set `spark.sql.files.maxPartitionBytes`, `fs.s3a.fast.upload` → `true`   |

---

## 10. Further reading & reference links

- AWS Blog – _Train machine learning models at scale with Apache Spark and Amazon SageMaker_ (2025‑01‑15)
- GitHub – [https://github.com/aws/sagemaker-spark](https://github.com/aws/sagemaker-spark)
- GitHub – [https://github.com/jupyter-incubator/sparkmagic](https://github.com/jupyter-incubator/sparkmagic)
- EMR Best Practices Guide – _Optimizing S3A performance_ (updated 2024‑11)
