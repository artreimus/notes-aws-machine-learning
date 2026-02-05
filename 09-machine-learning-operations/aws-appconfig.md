# AWS AppConfig (Systems Manager)

## Overview
- AWS AppConfig is a service for safely deploying configuration changes and feature flags to applications.
- It reduces risk by validating configurations, rolling out changes gradually, and rolling back automatically on alarms.

## Core Building Blocks
- **Application**: Logical container for related configurations.
- **Environment**: A target stage (dev, staging, prod).
- **Configuration profile**: The configuration type and source (feature flags or freeform).
- **Configuration data**: The actual config values to deploy.
- **Deployment strategy**: Controls rollout speed and bake time.
- **Deployment**: A rollout of a configuration version to an environment.

## Configuration Types
- **Feature flags**
  - Boolean or multi‑variant flags with rules and attributes.
  - Supports segmentation/targeting via context rules.
- **Freeform configuration**
  - Arbitrary JSON or text configuration, retrieved by apps at runtime.

## Configuration Sources
- AppConfig hosted configuration store (recommended for most cases).
- Amazon S3, SSM Parameter Store, SSM Document Store, or Secrets Manager.

## Validators (Safety Check)
- **JSON Schema** validator for freeform configs.
- **Lambda** validators for freeform and feature flags.
- Validation runs before deployment to prevent invalid configs.

## Deployment Strategies
- Gradual rollout over minutes/hours to reduce blast radius.
- Can be used with **CloudWatch alarms** to trigger automatic rollback.
- Supports manual revert to previous versions if needed.

## Monitoring and Rollback
- AppConfig integrates with CloudWatch alarms for automatic rollback.
- Supports third‑party monitors via AppConfig Extensions.

## Extensions
- Extensions can push notifications to EventBridge/SNS/SQS.
- Custom extensions can integrate with external systems (e.g., Jira) or add custom rollback logic.

## GenAI/ML Use Cases
- Feature flags for model routing (A/B model selection or fallback models).
- Prompt version control (toggle prompt templates or policies).
- Safety controls (tighten guardrails by configuration instead of redeploying).
- Gradual rollout of retrieval settings or RAG parameters.

## Best Practices
- Use hosted configuration store unless you must source externally.
- Validate all configs with JSON Schema or Lambda validators.
- Roll out gradually with alarms enabled for automatic rollback.
- Keep feature flags small and composable to avoid complex rule sets.

## Exam Tips
- AppConfig is for **safe configuration deployment**, not code deployment.
- Key safety controls: validators + deployment strategies + alarms + rollback.
- Supports feature flags and freeform configurations.

## Sources
- https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html
- https://docs.aws.amazon.com/appconfig/latest/userguide/creating-feature-flags-and-configuration-data.html
- https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-validators.html
- https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-feature-flags.html
- https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying-reverting.html
- https://aws.amazon.com/about-aws/whats-new/2024/11/aws-appconfig-automatic-rollback-safety-third-party-alerts/
- https://aws.amazon.com/about-aws/whats-new/2022/07/aws-announces-appconfig-extensions/
