---
title: "AWS Well-Architected Generative AI Lens"
exam: "MLA-C01"
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
  - "AWS Well-Architected Generative AI Lens"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Well-Architected Generative AI Lens

## Overview
- The Generative AI Lens extends the AWS Well-Architected Framework with guidance specific to generative AI workloads. 
- It covers the full lifecycle: scoping, model selection, customization, integration, deployment, and continuous improvement. 
- It applies the six Well-Architected pillars to generative AI: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. 

## Scope and Audience
- Applies to workloads using Amazon Bedrock foundation models or customer-managed models on Amazon SageMaker AI. 
- Intended for architects, developers, ML engineers, security, and business leaders. 

## What the Lens Emphasizes
- Responsible AI practices and shared responsibility across model producers, providers, and consumers. 
- Architectural considerations unique to GenAI, such as prompt engineering, RAG, and agentic workflows. 
- Continuous improvement through monitoring, evaluation, and iteration. 

## Six Pillars (GenAI Focus)
- **Operational excellence**: consistent output quality, lifecycle management, observability. 
- **Security**: protect endpoints, control data access, mitigate harmful outputs. 
- **Reliability**: handle failures, ensure throughput, enable distributed inference. 
- **Performance efficiency**: optimize model latency, retrieval performance, and scaling. 
- **Cost optimization**: model selection, prompt efficiency, vector store and agent cost controls. 
- **Sustainability**: reduce compute and storage footprint across training and inference. 

## How to Use It
- Use the lens in the AWS Well-Architected Tool to review and improve GenAI architectures. 
- The lens is available in the Well-Architected Lens Catalog and can be imported as a custom lens. 

## Relationship to Other Lenses
- Complements the Machine Learning Lens for traditional ML workloads. 
- Works alongside the Responsible AI Lens released in 2025 for governance and risk controls. 

## Exam Tips
- The Generative AI Lens is an AWS Well-Architected Framework lens, not a service.
- It applies the six pillars to GenAI-specific architecture and lifecycle decisions.
- It explicitly includes responsible AI considerations for GenAI workloads. 

## Sources
- https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html
- https://aws.amazon.com/about-aws/whats-new/2025/04/well-architected-generative-ai-lens/
- https://aws.amazon.com/blogs/architecture/announcing-the-updated-aws-well-architected-generative-ai-lens/
- https://aws.amazon.com/about-aws/whats-new/2025/11/new-aws-well-architected-lenses-ai-ml-workloads
- https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html
