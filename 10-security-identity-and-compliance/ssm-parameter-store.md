# 🧩 AWS SSM Parameter Store

## ✅ 1. **What is AWS SSM Parameter Store?**

**SSM Parameter Store** is a feature of **AWS Systems Manager** that provides **secure, hierarchical storage** for configuration data and secrets.

You can use it to store:

- Hyperparameters
- File paths
- API endpoints
- Secret values (with encryption)
- Configurations shared across ML jobs or services

It’s tightly integrated with **SageMaker, Lambda, EC2, Step Functions**, and other AWS services.

---

## ✅ 2. **Types of Parameters**

| Parameter Type   | Description             | Use Case                              |
| ---------------- | ----------------------- | ------------------------------------- |
| **String**       | Plaintext values        | Model names, file paths, config flags |
| **StringList**   | Comma-separated strings | List of S3 paths, endpoints           |
| **SecureString** | Encrypted using AWS KMS | API keys, passwords, tokens           |

---

## ✅ 3. **Key Features of SSM Parameter Store**

| Feature                  | Description                                                   |
| ------------------------ | ------------------------------------------------------------- |
| **Hierarchical storage** | Use `/env/app/component/key` format for logical grouping      |
| **Versioning**           | Automatically tracks versions of each parameter               |
| **KMS Integration**      | Encrypt secrets with customer-managed KMS keys                |
| **Access Control**       | Fine-grained IAM control over who can read/write parameters   |
| **Auditability**         | Integrates with AWS CloudTrail for logging access and changes |

---

## ✅ 4. **Why It’s Important for ML**

| Use Case                      | Role of SSM Parameter Store                                                  |
| ----------------------------- | ---------------------------------------------------------------------------- |
| **Experiment tracking**       | Store and retrieve hyperparameters                                           |
| **Environment configuration** | Store paths, model versions, dataset URIs                                    |
| **Secure access to secrets**  | Use SecureString for API keys or DB passwords                                |
| **ML pipeline reusability**   | Dynamically inject parameters into SageMaker Pipelines or processing scripts |

---

## ✅ 5. **SSM vs Secrets Manager**

| Feature                | SSM Parameter Store                       | Secrets Manager                         |
| ---------------------- | ----------------------------------------- | --------------------------------------- |
| **Designed for**       | General config + simple secrets           | Sensitive credentials (with rotation)   |
| **Secret Rotation**    | ❌ No native rotation                     | ✅ Yes (native + custom)                |
| **Free Tier**          | ✅ Yes (standard params)                  | ❌ No (always paid)                     |
| **Max size per param** | 4 KB                                      | 64 KB                                   |
| **Use for ML**         | Hyperparams, data paths, optional secrets | Tokens, credentials, sensitive API keys |

---

## ✅ 6. **Example Usage in ML Workflows**

### 📌 Scenario: You want to run a SageMaker training job and reuse parameterized config

1. Store your config:

   ```bash
   aws ssm put-parameter \
     --name "/ml/config/learning_rate" \
     --type "String" \
     --value "0.001"
   ```

2. Retrieve in Python:

   ```python
   import boto3

   ssm = boto3.client('ssm')
   lr = ssm.get_parameter(Name='/ml/config/learning_rate', WithDecryption=False)['Parameter']['Value']
   ```

3. Use the value to configure your ML model.

---

### 📌 Store and Secure a Token

```bash
aws ssm put-parameter \
  --name "/ml/api/token" \
  --type "SecureString" \
  --value "topsecret" \
  --key-id "alias/my-kms-key"
```

Retrieve in code:

```python
ssm.get_parameter(Name='/ml/api/token', WithDecryption=True)
```

---

## ✅ 7. **Best Practices**

| Best Practice                                | Benefit                                   |
| -------------------------------------------- | ----------------------------------------- |
| **Use hierarchy** (`/env/service/component`) | Keeps config organized                    |
| **Use SecureString for sensitive data**      | Ensures secrets are encrypted at rest     |
| **Use aliases for keys (`alias/…`)**         | Easier key management                     |
| **Set IAM policies for least privilege**     | Secure access control                     |
| **Use tagging**                              | For cost allocation, environment tracking |

---

## ✅ 8. **IAM Policy Example to Read Parameters**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["ssm:GetParameter", "ssm:GetParameters"],
      "Resource": ["arn:aws:ssm:us-east-1:123456789012:parameter/ml/config/*"]
    }
  ]
}
```

Attach to the **SageMaker execution role** or Lambda/EC2 role.

---

## ✅ 9. **Common ML Scenarios with Parameter Store**

| Scenario                                                         | Benefit                                         |
| ---------------------------------------------------------------- | ----------------------------------------------- |
| Run multiple training jobs with different parameters             | Dynamically read values per job                 |
| Share config across notebooks, pipelines, and processing scripts | Centralized config store                        |
| Protect sensitive environment variables in production models     | Use SecureString with KMS                       |
| Automate parameter injection into CI/CD pipelines                | Make deployments reproducible and parameterized |

---

## ✅ 10. **Limitations & Considerations**

| Limitation                               | Note                                                       |
| ---------------------------------------- | ---------------------------------------------------------- |
| Max 4 KB per parameter                   | For larger values, store in S3                             |
| SecureStrings don’t rotate automatically | Use Secrets Manager if rotation is needed                  |
| Throughput limits                        | Standard: 40 TPS, Advanced: 1000 TPS                       |
| Cost                                     | Standard params are free. Advanced params have extra cost. |

---

## ✅ 11. **Integration with Other AWS Services**

| Service                        | Integration                                                    |
| ------------------------------ | -------------------------------------------------------------- |
| **SageMaker**                  | Retrieve parameters in notebooks, training jobs, and pipelines |
| **Lambda**                     | Load secrets/config from Parameter Store                       |
| **Step Functions**             | Inject config parameters into workflow steps                   |
| **Glue**                       | Retrieve job parameters dynamically                            |
| **CloudFormation / Terraform** | Parameter injection during deployment                          |

---

## ✅ 12. **Pricing Overview**

- **Standard parameters**: Free
- **Advanced parameters**: ~$0.05 per parameter/month
- **SecureString (with KMS)**: ~$0.05 per 10,000 API calls + KMS usage

💡 **Use Standard + SecureString for cost-effective secret management** (if rotation isn’t required).

---

## ✅ 13. **Recommended Resources**

### 📘 AWS Docs

- [AWS SSM Parameter Store Guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [SecureString Parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-about.html)
- [Parameter Store Best Practices](https://docs.aws.amazon.com/systems-manager/latest/userguide/best-practices-parameter-store.html)

### 🧪 Tutorials & Labs

- 🧪 [SSM Parameter Store Hands-on Lab](https://catalog.us-east-1.prod.workshops.aws/workshops/3b57e3b2-5c4c-4e6f-8e76-6d688b842fa2)
- 🧪 [Using Parameter Store with SageMaker Pipelines](https://github.com/aws-samples/sagemaker-pipelines-with-parameter-store)

### 📺 Videos

- 🎥 [Parameter Store Deep Dive – AWS](https://www.youtube.com/watch?v=NmqgGwDdFy8)

---
