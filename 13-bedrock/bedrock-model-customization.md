---
title: "Amazon Bedrock Model Customization (Fine-tuning, Continued Pre-training, LoRA)"
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
  - "Amazon Bedrock Model Customization (Fine-tuning, Continued Pre-training, LoRA)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Bedrock Model Customization (Fine-tuning, Continued Pre-training, LoRA)

## Overview
- Bedrock supports **model customization** to improve performance on your domain or task. 
- Two primary supervised paths are **fine-tuning** (labeled data) and **continued pre-training** (unlabeled data). 
- Bedrock also offers **reinforcement fine-tuning (RFT)** for some Amazon Nova models, using reward-based feedback instead of large labeled datasets. 

## 1) Fine-tuning (Supervised)
- Use labeled input/output pairs to specialize a model for a task or style. 
- Best when you have a clear mapping from inputs to desired outputs (classification, summarization, tone/brand alignment).

## 2) Continued Pre-training (Unsupervised)
- Use unlabeled domain data to expand a model’s knowledge in a specific area. 
- Dataset format uses JSONL with **input-only** records (no labels). 
- Common for proprietary corpora, internal documents, or domain terminology.

## 3) Reinforcement Fine-tuning (RFT)
- Uses reward signals to teach models what a “good” response looks like. 
- Reduces the need for large labeled datasets by learning from feedback rules or judges. 

## 4) LoRA (Parameter-efficient fine-tuning)
- For Amazon Nova RFT training, the official training container supports **LoRA** and **full-rank** training. 
- LoRA reduces compute requirements by updating a smaller set of parameters, but you should confirm model and region availability per the RFT documentation. 

## Dataset Preparation (Key Differences)
- **Fine-tuning**: labeled prompt/completion or task-specific formats. 
- **Continued pre-training**: unlabeled input-only JSONL. 

## Workflow (High Level)
1. Choose a supported model and customization method. 
2. Prepare training (and optional validation) datasets in JSONL. 
3. Create IAM role and submit a customization job (console or API). 
4. Monitor job outputs, evaluate, and deploy the custom model. 

## Supported Models and Regions
- Supported models and regions vary by customization type; always check the **supported models** list. 
- Bedrock also lets you **import** custom models trained elsewhere via Custom Model Import. 

## Best Practices
- Start with prompt management and RAG; fine-tune only if needed.
- Use continued pre-training for knowledge gaps, supervised fine-tuning for behavior/style gaps.
- Evaluate before and after customization using Bedrock evaluations. 

## Exam Tips
- **Fine-tuning** = labeled data for task-specific performance. 
- **Continued pre-training** = unlabeled data to improve domain knowledge. 
- **LoRA** is supported in Amazon Nova RFT training container (parameter-efficient). 
- Always check supported models/regions before planning customization. 

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-supported.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/dataset-prep-continued-pretraining.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-submit.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/reinforcement-fine-tuning.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/nova-rft.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html
