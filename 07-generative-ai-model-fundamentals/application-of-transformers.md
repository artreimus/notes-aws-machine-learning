---
title: "Application Of Transformers"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "2.1"
service:
  - "Amazon Bedrock"
  - "Amazon Q Developer"
tags:
  - "aws"
  - "mla-c01"
  - "transformers"
  - "generative-ai"
aliases:
  - "Application Of Transformers"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Application Of Transformers

## Knowledge Relevance

Transformer application note for understanding current AWS generative AI services and updated Amazon Q Developer naming.

## When To Use

- Use transformers for language, text classification, summarization, translation, code assistance, embeddings, and multimodal foundation model tasks.
- Use Bedrock for managed foundation model access and Amazon Q Developer for AWS/code assistant workflows.

## Core Concepts

- Transformers use self-attention to model token relationships.
- Encoder, decoder, and encoder-decoder variants suit different tasks.
- CodeWhisperer capabilities were renamed/moved into Amazon Q Developer.

## AWS Services And Features

- Amazon Bedrock
- Amazon Q Developer
- Amazon SageMaker AI

## Implementation Patterns

- Application need -> choose FM/API/service -> apply prompt/RAG/fine-tuning/evaluation pattern.

## Tradeoffs And Pitfalls

- Do not use old CodeWhisperer naming as the current service name.
- Transformers are architecture concepts; Bedrock/Q/SageMaker are AWS service surfaces.

## Decision Triggers

- AWS coding assistant now points to Amazon Q Developer.
- Foundation model hosting/API points to Bedrock.

## Related Notes

- [[amazon-q]]
- [[amazon-bedrock]]
- [[transformer-architecture]]


## Sources

- https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/service-rename.html
- https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
