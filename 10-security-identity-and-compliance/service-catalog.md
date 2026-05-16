---
title: "AWS Service Catalog"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.2"
  - "4.3"
service:
  - "AWS Service Catalog"
tags:
  - "aws"
  - "mla-c01"
  - "domain-4"
  - "governance"
aliases:
  - "AWS Service Catalog"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Service Catalog

## Knowledge Relevance

Governed self-service catalog for approved AWS infrastructure and application templates.

## When To Use

- Use when teams need to launch approved infrastructure without direct broad permissions.
- Use for standardized ML environments, notebooks, or pipeline templates.
- Use portfolios, products, constraints, and IAM access to govern launches.

## Core Concepts

- Administrators create portfolios and products.
- End users launch provisioned products they are allowed to access.
- Constraints standardize regions, instance types, tags, and other controls.

## AWS Services And Features

- AWS Service Catalog
- AWS CloudFormation
- IAM
- AWS Organizations

## Implementation Patterns

- Admin publishes SageMaker project/environment template -> grants portfolio access -> data scientist launches approved product.

## Tradeoffs And Pitfalls

- Service Catalog governs infrastructure templates; it does not run ML jobs by itself.
- Product versions and constraints need lifecycle management.

## Decision Triggers

- Approved IT service catalog, self-service with guardrails, and provisioned products point to Service Catalog.
- Infrastructure as code template alone points to CloudFormation/CDK.

## Related Notes

- [[cloud-formation]]
- [[cloud-development-kit]]
- [[organizations]]


## Sources

- https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
