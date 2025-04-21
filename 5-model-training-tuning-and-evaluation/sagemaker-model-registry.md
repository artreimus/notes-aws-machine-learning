### 1. Service Name

**Amazon SageMaker Model Registry**

---

### 2. Category

- **Machine Learning → Model Management**

---

### 3. Overview

A **central catalog** for managing machine learning models within SageMaker. It tracks model versions, metadata, approval status, and stage transitions (e.g., “Pending”, “Approved”, “Rejected”, “Archived”). Acts as the source of truth for which model artifacts are production‑ready and supports integration into CI/CD pipelines for automated deployment.

---

### 4. Key Features

- **Model Package Groups**  
  Logical grouping of related model versions (e.g., all versions of “ImageClassifier”).
- **Versioning**  
  Each model package gets an immutable version, with metadata (training job, metrics, container image).
- **Approval Workflows**  
  Track and enforce manual approval before deployment. Statuses include:  
  | Status | Meaning |
  |-----------|-------------------------------------------------|
  | Pending | Newly registered; awaiting review |
  | Approved | Cleared for deployment |
  | Rejected | Not suitable for production |
  | Archived | Superseded or retired versions |
- **Metadata & Model Cards**  
  Attach free‑form key/value metadata, tags, and link to a SageMaker Model Card describing intended use, limitations, bias analysis.
- **Event Notifications**  
  Emits EventBridge events (e.g., `ModelPackageGroupNotification`) on registration or status change.
- **Integration into Pipelines**  
  Use with SageMaker Pipelines, CodePipeline, or custom Lambda functions to automate approval, deployment, and rollback.
- **Access Control**  
  IAM policies to grant fine‑grained permissions on model groups, model packages, and associated actions.

---

### 5. Common Use Cases

- **Governance & Compliance**  
  Enforce manual review before production rollout.
- **CI/CD for ML**  
  Automate promotion of models from staging to production via pipelines.
- **Collaboration & Sharing**  
  Provide a shared registry of vetted models across teams.
- **Audit Trails**  
  Maintain history of model versions, metrics, and approval decisions.

---

### 6. How It Works (Architecture)

1. **Register Model**  
   After training, call `CreateModelPackage` (or use the SageMaker SDK) to register a new model package in a Model Package Group.
2. **EventBridge Trigger**  
   Model Registry emits an event on creation or status update.
3. **Approval Workflow**
   - **Manual**: A reviewer sees a notification, then calls `UpdateModelPackage` to set status to Approved/Rejected.
   - **Automated**: A Lambda function or Pipeline step auto‑approves based on custom criteria.
4. **Deployment**  
   Downstream CI/CD uses the Approved status to retrieve the model artifact and deploy via SageMaker Endpoints, Batch Transform, or inference pipelines.
5. **Promotion & Retirement**  
   New versions can be approved and old ones archived.

---

### 7. Integration with Other AWS Services

- **SageMaker Pipelines**: `RegisterModel` & `ModelStep` for automated model registration and promotion.
- **EventBridge**: React to registry events for notifications or automated logic.
- **Lambda & SNS**: Orchestrate human‑in‑the‑loop approvals or notifications.
- **AWS CodePipeline**: Build full CI/CD workflows around model registration and deployment.
- **Parameter Store / Secrets Manager**: Store model URIs or deployment configuration tied to approved versions.

---

### 8. Pricing Model

- **Model Artifacts Storage**: Billed at standard S3 rates for storing container images and artifacts.
- **API Calls & Metadata**: No additional charge for using the registry APIs or storing metadata.
- **Pipeline Integration**: Standard SageMaker Pipeline and Lambda charges apply.

---

### 9. Security & Compliance

- **IAM Controls**: Grant `sagemaker:CreateModelPackage`, `UpdateModelPackage`, `ListModelPackages`, etc., scoped to specific Model Package Groups.
- **Encryption**: Artifacts in S3 can be encrypted with SSE‑S3 or SSE‑KMS.
- **VPC Endpoints**: Keep all registry traffic within your VPC.

---

### 10. Best Practices

- **Use Model Cards** to capture context, intended use, and limitations.
- **Automate Approval** only when certain metrics (e.g., accuracy threshold) are met; otherwise require manual review.
- **Tag Model Packages** with environment (`dev`/`staging`/`prod`), team owner, and audit identifiers.
- **Archive Old Versions** to keep registry clean and reduce confusion.
- **Enforce Least Privilege** in IAM policies to ensure only appropriate roles can approve or deploy models.

---

### 11. Limitations

- **Tabular Only**: Works with any model artifact, but lacks first‑class support for non‑tabular pipelines (e.g., streaming).
- **Manual Approval Latency**: Human‑in‑the‑loop steps can slow down CI/CD.
- **No Built‑In Rollback**: You must orchestrate rollback logic in your pipelines.

---

### 12. CLI / SDK Examples

**Register a Model Package**

```bash
aws sagemaker create-model-package \
  --model-package-name ImageClassifier-v1 \
  --model-package-group-name ImageClassifierGroup \
  --inference-specification '{
     "Containers": [{"Image":"123456789012.dkr.ecr...","ModelDataUrl":"s3://bucket/model.tar.gz"}],
     "SupportedContentTypes":["image/png"],
     "SupportedResponseMIMETypes":["application/json"]
   }'
```

**Update Approval Status**

```bash
aws sagemaker update-model-package \
  --model-package-name ImageClassifier-v1 \
  --model-approval-status Approved \
  --approval-description "Meets performance and bias criteria"
```

---

### 13. Exam‑Focused Quick Tips

- **Model Package Group** = namespace for versions.
- **Approval Statuses**: Pending → Approved/Rejected → Archived.
- **EventBridge Integration**: Registry emits events on registration & status change.
- **SageMaker Pipelines** provides `RegisterModel` step to register and transition model stages automatically.
- **Model Cards** can be linked for governance and bias auditing.
