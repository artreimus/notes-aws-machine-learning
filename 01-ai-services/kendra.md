---
title: "Amazon Kendra"
exam: "MLA-C01"
status: "draft"
domain:
  - "2.1"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-2"
  - "01_ai_services"
aliases:
  - "Amazon Kendra"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Kendra

## Overview

Amazon Kendra is an intelligent enterprise search service powered by machine learning (ML). It enables organizations to index, search, and retrieve unstructured and structured data from a wide variety of sources, delivering highly accurate and relevant search results. Kendra is designed to help users find information across disparate content repositories (such as file systems, intranets, databases, and applications) using natural language queries. Its ML-powered relevance ranking, natural language understanding, and easy integration make it a key tool for knowledge management and productivity in modern enterprises.

**Key Features:**

- Natural language search (understands questions, not just keywords)
- ML-powered relevance ranking
- Connectors for popular data sources (SharePoint, S3, databases, etc.)
- Faceted search and filtering
- Incremental and scheduled data sync
- Secure access control and user context awareness

**Relevance in AWS ML:**
Kendra leverages AWS's ML capabilities to provide semantic search, making it easier for users to find precise answers from large volumes of data. It is often used in conjunction with other AWS services for end-to-end ML and data workflows.

## AWS Services & Features

- **Amazon Kendra Index:** The core resource where data is indexed and searched.
- **Data Source Connectors:** Pre-built connectors for Amazon S3, SharePoint, Salesforce, RDS, databases, and more, enabling seamless ingestion of enterprise data.
- **Query API:** Allows applications to submit search queries and receive ranked results.
- **Access Control:** Integrates with AWS IAM, SAML, and other identity providers to enforce fine-grained access to search results.
- **Integration with AWS Services:**
  - **Amazon S3:** Index documents stored in S3 buckets.
  - **AWS Lambda:** Custom data source connectors and pre-processing.
  - **Amazon SageMaker:** Enhance search with custom ML models (e.g., for entity extraction).
  - **AWS CloudWatch:** Monitor Kendra usage and performance.

## Practical Application

**Common Use Cases:**

- Enterprise document and knowledge base search
- Customer support portals (self-service Q&A)
- Internal help desks and HR portals
- Research and compliance document retrieval

**Sample Architecture:**

1. Data is ingested from multiple sources (S3, SharePoint, databases) using Kendra connectors.
2. Kendra indexes the content and applies ML-powered ranking.
3. Users interact with a web/mobile app that queries Kendra using natural language.
4. Kendra returns relevant answers, documents, or passages, respecting user access permissions.
5. Usage and performance are monitored via CloudWatch.

**Example Workflow:**

- HR team uploads policy documents to S3.
- Kendra indexes the documents.
- Employees use a portal to ask questions like "What is the parental leave policy?"
- Kendra returns the most relevant answer or document section.

## Challenges & Best Practices

**Common Challenges:**

- Integrating with diverse and legacy data sources
- Ensuring data freshness and sync schedules
- Tuning search relevance for specific business needs
- Managing access control and data security

**Best Practices:**

- Use pre-built connectors where possible for reliability and support.
- Regularly update and monitor data sync schedules.
- Leverage Kendra's relevance tuning features (boosting, synonyms, etc.).
- Implement fine-grained access control using IAM and user context.
- Monitor search metrics and user feedback to continuously improve search quality.

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
