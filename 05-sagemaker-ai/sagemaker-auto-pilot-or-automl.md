## 1. Service Name

**Amazon SageMaker Autopilot**

---

## 2. Category

- **Machine Learning → AutoML**
- Built on top of **Amazon SageMaker**

---

## 3. Overview

SageMaker Autopilot is AWS’s managed **AutoML** service. Given a tabular dataset and a target column, it will automatically:

1. Profile and preprocess your data
2. Select suitable algorithms
3. Tune hyperparameters
4. Generate and rank candidate models
5. Produce a deployable model and a Jupyter notebook you can inspect or customize

---

## 4. Key Features

- **No‑code wizard**: Point‑and‑click in SageMaker Studio or via CLI/SDK
- **Algorithm selection**: Chooses from LinearLearner, XGBoost, deep networks, tree ensembles (via AutoGluon)
- **Hyperparameter tuning**: Built‑in HPO with up to 100 trials
- **Ensembling**: Optional stacked ensembles of multiple algorithms
- **Model leaderboard**: Ranked list of top candidates with metrics
- **Notebook export**: Full recipe of data prep, feature engineering, algorithm code
- **Explainability**: Integrates with SageMaker Clarify for feature attribution (SHAP values)
- **Human‑in‑the‑loop**: Override defaults, inject custom data transforms or algorithms

---

## 5. Supported Problem Types

- **Binary Classification**
- **Multi‑Class Classification**
- **Regression**

---

## 6. Workflow Steps

1. **Data source**: Point to CSV or Parquet on S3 (tabular data).
2. **Define target**: Choose the column to predict.
3. **Select mode**:
   - **HPO Mode** – hyperparameter optimization
   - **Ensemble Mode** – trains multiple model types then stacks them
   - **Auto Mode** – below 100 MB → Ensemble; above 100 MB → HPO
4. **Launch job**: Autopilot profiles schema, splits data, runs trials.
5. **View leaderboard**: Compare models by validation metric.
6. **Export notebook**: Review or tweak data prep, algorithms, and deploy.
7. **Deploy & monitor**: Spin up an endpoint, integrate with Clarify for bias/fairness.

---

## 7. Training Modes Comparison

| Mode              | Algorithms                                  | Trials    | Search Strategy          | When AWS Chooses It      |
| ----------------- | ------------------------------------------- | --------- | ------------------------ | ------------------------ |
| **HPO Mode**      | LinearLearner, XGBoost, MLP                 | Up to 100 | Bayesian (>100 MB) or    | Manual or Auto (>100 MB) |
|                   |                                             |           | Multi‑fidelity (<100 MB) |                          |
| **Ensemble Mode** | AutoGluon family: ensembles of trees & nets | 10        | Parallel model training  | Manual or Auto (<100 MB) |
| **Auto Mode**     | HPO or Ensemble as above                    | Depends   | Based on data size       | Default if size known    |

**Note:** If Autopilot can’t determine your dataset size (e.g. hidden in VPC, manifest files, >1,000 objects), Auto Mode defaults to **HPO**.

---

## 8. Input Data Requirements & Limits

- **Formats**: CSV or Parquet
- **Schema**: Tabular with a single target column
- **Size**:
  - ≤ 100 MB → Ensemble by default
  - > 100 MB → HPO by default
- **URI constraints**:
  - If S3 bucket is in a VPC or uses manifests/over 1,000 objects, defaults to HPO

---

## 9. Integration with SageMaker Clarify

- **Why**: Expose feature‑level biases and contribution.
- **How**: Generates SHAP‑based feature attributions per prediction.
- **Use case**: Detect unwanted bias (e.g., protected attributes influencing outcome).

---

## 10. Pricing Model

- Billed for all underlying **training instances** used by each candidate model/trial.
- Costs vary by instance type, number of trials, and total runtime.
- **Tip**: Limit max trials or choose Ensemble (10 trials) to control spend.

---

## 11. Security & Permissions

- **IAM** roles/policies control access to S3, SageMaker, and output resources.
- Data in transit encrypted via TLS; at rest via S3/KMS.
- VPC integration available for private networking.

---

## 12. Best Practices

- **Inspect the notebook** before deploying — don’t treat it as a black box.
- Use **Clarify** to audit feature importance and mitigate bias.
- Adjust **MaxRuntime**, **MaxJobs**, and **ParallelJobs** to fit budget.
- For highly skewed or large datasets, consider custom tuning outside Autopilot.
- Clean and pre‑process data (missing values, outliers) to improve AutoML results.

---

## 13. Limitations & Caveats

- Only handles tabular CSV/Parquet data.
- Black‑box ensembling makes deep debugging harder (though notebook helps).
- “Auto” mode decisions depend on successful dataset size detection.
- Not suited for time‑series forecasting, computer vision, or NLP tasks.

---

## 14. CLI/SDK Example

```bash
aws sagemaker create-auto-ml-job \
  --auto-ml-job-name my-autopilot-job \
  --input-data-config file://input-config.json \
  --output-data-config file://output-config.json \
  --auto-ml-job-config '{
    "CompletionCriteria": { "MaxRuntimePerTrainingJobInSeconds": 3600 },
    "SecurityConfig": { "VolumeKmsKeyId": "arn:aws:kms:..." }
  }' \
  --role-arn arn:aws:iam::123456789012:role/SageMakerRole
```

Where **input-config.json** points to your S3 CSV/Parquet and specifies the target column.

---

## 15. Exam‑Focused Quick Tips

- **“Auto” mode**: ≤ 100 MB → Ensemble; > 100 MB → HPO.
- **HPO** uses **Bayesian** (large data) or **Multi‑fidelity** (small data) under the hood.
- **Ensemble mode** runs 10 diverse models via AutoGluon and stacks them.
- **Always export the notebook** to understand data prep and guard against bias.
- **Clarify integration**: SHAP‑based feature attribution for fairness and transparency.
