---
title: "Amazon Bedrock Custom Model Import"
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
  - "Amazon Bedrock Custom Model Import"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Bedrock Custom Model Import

## Overview
- Custom Model Import lets you bring **customized open‑source foundation models** into Bedrock and use them via the same Bedrock inference APIs. 
- It preserves prior investments in fine‑tuning or continued pre‑training done outside Bedrock (for example in SageMaker). 
- Imported models can use Bedrock features like Guardrails, Knowledge Bases, and Agents. 

## Supported Customization Patterns
- **Fine‑tuned or continued pre‑training** on a base model (weights updated). 
- **Domain adaptation** for specific verticals or languages. 
- **Pretrained from scratch** with a custom model configuration. 

## Model and Region Support
- Supported architectures include Mistral, Mixtral, Flan, Llama (2/3/3.1/3.2/3.3, Mllama), GPTBigCode, Qwen (2/2.5/2‑VL/2.5‑VL/3), and GPT‑OSS (region‑restricted). 
- Supported Regions include eu‑central‑1, us‑east‑1, us‑east‑2, us‑west‑2 (check docs for current list). 

## Requirements
- Model files must be in **Hugging Face weights format** (for example `.safetensors` + `config.json`). 
- Models are imported from **Amazon S3** or an **Amazon SageMaker model repo**. 

## Inference and Limitations
- Imported models can be invoked via `InvokeModel` or streaming variants. 
- Batch inference and CloudFormation are not supported for imported models. 

## Workflow (High Level)
1. Prepare model weights and config in HF format.
2. Upload to S3 or point to a SageMaker model repo.
3. Create IAM role for Bedrock import job.
4. Submit `CreateModelImportJob` and monitor status.
5. Use the imported model ARN for inference.

## Best Practices
- Validate model performance in a sandbox before production use.
- Use Bedrock Evaluations to compare imported models against native FMs. 
- Apply Guardrails and monitoring to control risk.

## Exam Tips
- Custom Model Import = bring **customized open‑source models** into Bedrock.
- Requires Hugging Face weights format and S3/SageMaker hosting.
- Uses the same Bedrock inference APIs once imported. 

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-import-prereq.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-import-code-samples.html
- https://aws.amazon.com/bedrock/custom-model-import/
