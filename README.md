---
title: "AWS Certified Machine Learning Engineer - Associate (MLA-C01) Study Notes"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "all"
service:
  - "AWS Certification"
tags:
  - "aws"
  - "mla-c01"
  - "readme"
aliases:
  - "MLA-C01 Study Notes"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Certified Machine Learning Engineer - Associate (MLA-C01) Study Notes

This vault is an exam-first study system for AWS Certified Machine Learning Engineer - Associate (MLA-C01). It combines AWS service notes, machine learning concepts, SageMaker AI workflows, Bedrock/gen AI patterns, and operational/security guidance.

## Current Exam Facts

| Item | Value |
| --- | --- |
| Exam code | MLA-C01 |
| Duration | 130 minutes |
| Question count | 65 questions |
| Passing score | 720 |
| Domain 1 | Data Preparation for Machine Learning, 28% |
| Domain 2 | ML Model Development, 26% |
| Domain 3 | Deployment and Orchestration of ML Workflows, 22% |
| Domain 4 | ML Solution Monitoring, Maintenance, and Security, 24% |

## How This Vault Is Organized

| Folder | Purpose |
| --- | --- |
| `00-exam-guide/` | Official exam overview, domain maps, scope checklists, and study roadmap |
| `01-ai-services/` | AWS AI and ML application services |
| `02-data-ingestion-and-storage/` | Data sources, streaming, storage, lake, warehouse, and database services |
| `03-data-transformation-integrity-and-feature-engineering/` | Data transformation, Glue, Spark, quality, feature engineering, and integrity topics |
| `04-model-training-tuning-and-evaluation/` | Training, tuning, metrics, model selection, and evaluation concepts |
| `05-sagemaker-ai/` | Amazon SageMaker AI capabilities for build, train, tune, deploy, and govern workflows |
| `06-sagemaker-built-in-algorithms/` | SageMaker AI built-in algorithms and algorithm selection notes |
| `07-generative-ai-model-fundamentals/` | Foundation model and transformer fundamentals |
| `08-building-gen-ai-apps-with-bedrock/` | Bedrock application scenarios that link to canonical Bedrock notes |
| `09-machine-learning-operations/` | MLOps, orchestration, CI/CD, deployment, cost, and observability |
| `10-security-identity-and-compliance/` | IAM, network isolation, encryption, governance, compliance, and data protection |
| `11-machine-learning-best-practices/` | Responsible AI, Well-Architected guidance, A2I, and human review |
| `12-sql/` | SQL support material for Athena, Redshift, Glue, and analytics tasks |
| `13-bedrock/` | Canonical Amazon Bedrock feature notes |
| `14-agentic-ai/` | Supplemental agent framework notes |
| `common/` | Cross-cutting ML fundamentals |

## Study Paths

- Fast exam review: start with `00-exam-guide/exam-overview.md`, then review each domain map.
- SageMaker AI path: use `05-sagemaker-ai/`, `06-sagemaker-built-in-algorithms/`, and Domain 2/3 guide notes.
- Data preparation path: use `02-data-ingestion-and-storage/`, `03-data-transformation-integrity-and-feature-engineering/`, and Domain 1.
- Bedrock/gen AI path: use `13-bedrock/` first, then `08-building-gen-ai-apps-with-bedrock/` for scenarios.
- Security and operations path: use `09-machine-learning-operations/`, `10-security-identity-and-compliance/`, and Domain 4.

## Note Status Legend

| Status | Meaning |
| --- | --- |
| `reviewed` | Verified against current AWS docs and mapped to exam tasks |
| `draft` | Useful and normalized, but not yet promoted to the fully reviewed set |
| `stale` | Needs source refresh before exam study use |
| `legacy` | AWS service or feature is no longer available to new customers, has no new releases, or is in shutdown/sunset status |
| `supplemental` | Useful background but not a primary current MLA-C01 study target |
| `out-of-scope` | Listed out of scope by the current AWS MLA-C01 guide |

## How To Add Or Update A Note

1. Start from `NOTE_TEMPLATE.md`.
2. Use current AWS service names, such as Amazon SageMaker AI and Amazon Managed Service for Apache Flink.
3. Add frontmatter with `title`, `exam`, `status`, `domain`, `service`, `tags`, `aliases`, `last_verified`, and `source_type`.
4. Include these sections: `Exam Relevance`, `When To Use`, `Core Concepts`, `AWS Services And Features`, `Implementation Patterns`, `Tradeoffs And Pitfalls`, `Exam Triggers`, `Related Notes`, and `Sources`.
5. Cite official AWS docs first. Use blogs, whitepapers, or third-party sources only when AWS docs are insufficient.
6. Mark lifecycle caveats clearly. Do not delete legacy notes unless the repo owner asks for that cleanup.

## Validation Checks

Run the repo validator first:

```bash
python3 scripts/validate_notes.py
```

Use strict section checks when intentionally migrating inherited notes to the full `NOTE_TEMPLATE.md` layout:

```bash
python3 scripts/validate_notes.py --strict-sections
```

Useful focused spot checks:

```bash
rg --files-without-match '^# ' -g '*.md'
rg --files-without-match '^(## )?(Sources|References|Additional Resources)\b' -g '*.md'
rg -n 'Elastic Inference|Training Compiler|Data Pipeline|Amazon Forecast|AWS AppConfig|AWS IoT Greengrass|AWS Shield|Amazon DataZone|Kinesis Data Analytics|Studio Classic|Edge Manager|CodeWhisperer|Glue Elastic Views' -g '*.md'
rg -n 'TODO|needs-verification|source_type: "needs-verification"' -g '*.md' --glob '!README.md' --glob '!PLAN_NOTES_IMPROVEMENT.md'
```

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-out-of-scope-services.html
