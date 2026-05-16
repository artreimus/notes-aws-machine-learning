---
title: "Responsible AI in AWS (Bedrock + SageMaker)"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "draft"
domain:
  - "4.3"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-4"
  - "11_machine_learning_best_practices"
aliases:
  - "Responsible AI in AWS (Bedrock + SageMaker)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Responsible AI in AWS (Bedrock + SageMaker)

## Overview
- AWS defines responsible AI across eight dimensions: fairness, explainability, privacy and security, safety, controllability, veracity and robustness, governance, and transparency. 
- The AWS Responsible AI Lens provides best-practice guidance and design principles for building AI systems responsibly. 

## Policy and Governance Baseline
- The AWS Responsible AI Policy applies to AI/ML services and includes explicit prohibitions (for example, disinformation or privacy violations). 
- The Responsible AI Lens emphasizes narrowly defined use cases, responsible-by-design development, and science-based practices. 

## Core AWS Tools by Lifecycle Stage

### 1) Data and Training (SageMaker)
- **SageMaker Clarify** supports bias detection (pre- and post-training) and model explainability, plus bias drift and feature attribution drift monitoring for deployed models. 
- **SageMaker Model Monitor** detects data quality, model quality, bias drift, and feature attribution drift, and integrates with Clarify for bias monitoring. 

### 2) Evaluation (Bedrock)
- **Bedrock Evaluations** supports automatic, human, and LLM-as-a-judge evaluations for models and RAG workflows. 
- RAG evaluation can assess retrieval quality and end-to-end generation metrics, including responsible AI metrics like harmfulness and answer refusal. 

### 3) Safety and Content Controls (Bedrock)
- **Bedrock Guardrails** provides configurable safeguards such as content filters and denied topics to filter harmful content. 
- Guardrails also support sensitive information (PII) redaction and prompt attack detection, and can be applied across workflows using the ApplyGuardrail API. 
- **Automated Reasoning checks** in Guardrails uses formal verification to validate responses and detect hallucinations for policy compliance. 

### 4) Monitoring and Governance (SageMaker)
- **Model Monitor** produces alerts for quality and bias drift to trigger retraining or remediation. 
- **SageMaker Model Cards** provide standardized documentation for intended use, risk ratings, training details, and evaluation results. 

### 5) Transparency (AWS-wide)
- **AWS AI Service Cards** document intended use, limitations, and responsible AI design choices for AWS AI services. 

## Bedrock vs. SageMaker: How They Complement
- **Bedrock** focuses on model selection, evaluation, and safety guardrails for generative AI, including RAG evaluation and Guardrails. 
- **SageMaker** focuses on bias detection, explainability, model monitoring, and governance artifacts for traditional ML and custom models. 

## Practical Checklist
- Define a narrow use case and document risk assumptions. 
- Use Clarify for bias/explainability and Model Monitor for drift in production. 
- Evaluate models and RAG pipelines with Bedrock evaluations before release. 
- Apply Guardrails for safety, PII redaction, and prompt attack mitigation. 
- Publish model documentation using Model Cards and review AI Service Cards for AWS services used. 

## Exam Tips
- Responsible AI in AWS is not one service, it is a **policy + best-practice framework + tooling** across Bedrock and SageMaker. 
- Guardrails, Automated Reasoning checks, and Bedrock Evaluations are the core Bedrock safety and evaluation controls. 
- Clarify, Model Monitor, and Model Cards are the core SageMaker responsible AI and governance tools. 

## Sources
- https://aws.amazon.com/ai/responsible-ai/
- https://aws.amazon.com/ai/responsible-ai/policy/
- https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/design-principles.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html
- https://aws.amazon.com/bedrock/guardrails/
- https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-model-evaluation-llm-as-a-judge/
- https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-rag-evaluation-generally-available/
- https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-mlops.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html
- https://aws.amazon.com/about-aws/whats-new/2024/12/aws-ai-service-cards-advance-responsible-generative-ai/
