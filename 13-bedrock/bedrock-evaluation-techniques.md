---
title: "Evaluation Techniques in Amazon Bedrock"
exam: "MLA-C01"
status: "draft"
domain:
  - "2.1"
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
  - "13_bedrock"
aliases:
  - "Evaluation Techniques in Amazon Bedrock"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Evaluation Techniques in Amazon Bedrock

## Overview
- Bedrock provides multiple evaluation approaches to compare models, prompts, and RAG pipelines.
- Techniques span automatic metrics, LLM-as-a-judge, and human evaluation, plus RAG-specific evaluation.

## Core Evaluation Techniques

### 1) Programmatic (Automatic) Evaluation
- Uses built-in datasets and classic metrics (accuracy, robustness, toxicity, etc.).
- Best for fast, repeatable baseline comparisons across models or prompt variants.

### 2) LLM-as-a-Judge
- Uses a separate evaluator model to score the generator model’s outputs.
- Useful for subjective quality dimensions such as correctness, completeness, helpfulness, and tone.
- Supports custom metrics via custom judge prompts and rating scales.

### 3) Human Evaluation
- Human reviewers score outputs for subjective or brand-specific criteria.
- Used for safety, tone, policy alignment, or high-stakes quality checks.

### 4) RAG Evaluation (Retrieval)
- Measures how good retrieval is: context relevance, coverage, and recall.
- Useful for tuning chunking, embeddings, and retrieval parameters.

### 5) RAG Evaluation (Retrieve and Generate)
- End-to-end evaluation of the full RAG workflow output.
- Includes faithfulness (hallucination detection), correctness, and completeness.

## Metrics (Common Examples)
- **Correctness, completeness, relevance** for answer quality.
- **Faithfulness** to detect hallucinations in RAG outputs.
- **Helpfulness and tone** for human-aligned quality.
- **Toxicity/harmfulness** for safety review.

## Datasets
- Built-in datasets for standard tasks (summarization, QA, classification).
- Custom prompt datasets to reflect your real workload and edge cases.

## Workflow (Typical)
1. Choose evaluation type (model or RAG).
2. Select dataset (built-in or custom).
3. Pick evaluation technique (programmatic, LLM judge, human).
4. Run evaluation job and review results.
5. Compare across models, prompts, or configurations.

## Best Practices
- Use custom datasets that mirror production inputs.
- Combine automated metrics with judge-based evaluation for balanced signals.
- Keep a fixed evaluation suite for regression detection.
- Re-evaluate when you change models, prompts, or retrieval settings.

## Exam Tips
- Bedrock supports automatic, LLM-as-judge, and human evaluation techniques.
- RAG evaluation is split into retrieval-only and retrieve-and-generate.
- LLM-as-judge is for subjective quality dimensions that classic metrics miss.

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-tasks.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html
- https://aws.amazon.com/bedrock/evaluations/
