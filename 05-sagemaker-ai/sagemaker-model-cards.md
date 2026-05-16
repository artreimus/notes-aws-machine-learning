---
title: "SageMaker Model Cards"
exam: "MLA-C01"
status: "draft"
domain:
  - "2.2"
  - "3.1"
  - "4.1"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-2"
  - "domain-3"
  - "domain-4"
  - "05_sagemaker_ai"
aliases:
  - "SageMaker Model Cards"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SageMaker Model Cards

## Overview

Amazon SageMaker Model Cards provide a standardized, centralized way to document machine learning (ML) models throughout their lifecycle. Model cards capture essential details such as intended use, training and evaluation data, performance metrics, ethical considerations, and risk assessments. This documentation helps ensure transparency, governance, and compliance, which are increasingly important in regulated industries and for responsible AI practices.

Model cards are especially relevant for organizations that need to track model lineage, support audits, and communicate model details to stakeholders, including data scientists, business leaders, and compliance teams.

## AWS Services & Features

- **Amazon SageMaker Model Cards**: A feature within SageMaker that allows users to create, manage, and share model cards directly from the SageMaker Studio UI or via the SageMaker API/SDK.
- **SageMaker Model Registry**: Integrates with model cards to associate documentation with registered models, supporting model governance and deployment workflows.
- **SageMaker Studio**: Provides a visual interface for creating and editing model cards, making it easier for teams to collaborate and maintain documentation.

**Key Features:**

- Predefined templates for consistent documentation
- Integration with SageMaker Model Registry
- Support for custom fields and attachments (e.g., evaluation reports, diagrams)
- Versioning and audit trails

## Practical Application

### Example Scenario

A financial services company develops a credit risk prediction model. To comply with regulatory requirements, the team creates a SageMaker Model Card documenting:

- Model purpose and intended use
- Training and evaluation datasets
- Performance metrics (e.g., ROC AUC, accuracy)
- Fairness and bias assessments
- Limitations and ethical considerations

The model card is linked to the model in the SageMaker Model Registry, ensuring that any deployment or audit references the latest documentation.

### Typical Workflow

1. Train and evaluate a model in SageMaker.
2. Register the model in the Model Registry.
3. Create a model card using the SageMaker Studio UI or SDK, filling in required sections.
4. Attach relevant artifacts (e.g., evaluation reports, diagrams).
5. Update the model card as the model evolves or is re-evaluated.

## Challenges & Best Practices

### Challenges

- **Incomplete Documentation**: Teams may overlook important details, leading to gaps in compliance or understanding.
- **Keeping Model Cards Updated**: As models are retrained or updated, documentation can become outdated.
- **Sensitive Information**: Care must be taken not to include confidential or personally identifiable information (PII) in model cards.

### Best Practices

- **Standardize Documentation**: Use the provided templates and require completion of all relevant sections.
- **Automate Updates**: Integrate model card creation and updates into CI/CD pipelines where possible.
- **Review Regularly**: Schedule periodic reviews of model cards, especially for models in production.
- **Access Control**: Use AWS IAM policies to restrict who can view or edit model cards.

## Sources

- https://docs.aws.amazon.com/sagemaker/
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
