---
title: "Amazon Bedrock Data Automation (BDA)"
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
  - "Amazon Bedrock Data Automation (BDA)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Bedrock Data Automation (BDA)

## Overview

- BDA is a Bedrock feature for extracting structured insights from unstructured, multimodal content (documents, images, audio, video).
- It can be used standalone or as a **parser** in Bedrock Knowledge Bases RAG workflows.

## Core Concepts

- Standard output
  - Default, preconfigured insights for each modality (for example, document summaries or audio transcription).
- Custom output
  - Define the exact fields you want extracted via **blueprints**.
- Blueprints
  - Schemas/instructions that control custom extraction output.
  - You can use built-in blueprints or create your own.
- Projects
  - Bundle standard output configs and custom blueprints.
  - A project can include multiple document blueprints (up to 40) and one blueprint each for image/audio/video.

## How It Works (High Level)

1. Create a project and configure standard outputs.
2. Create or attach blueprints for custom output.
3. Submit content to BDA via API (async by default).
4. Retrieve structured outputs and use them downstream (RAG, analytics, workflows).

## API and Operation Modes

- BDA supports async processing for all modalities.
- Images can also be processed synchronously for low-latency use cases.

## Integration with Bedrock Knowledge Bases

- BDA can be selected as the parser for multimodal data ingestion in Knowledge Bases.
- This enables structured, higher-quality ingestion of complex documents and visuals for RAG.

## Use Cases

- Intelligent document processing (forms, invoices, claims).
- Media analysis (scene summaries, object/logo detection).
- Content moderation and metadata extraction.
- RAG pipelines that need structured extraction before retrieval.

## Security and Governance

- Supports KMS CMKs for encryption, PrivateLink, and resource tagging for cost/governance.

## Best Practices

- Start with standard output to validate signal quality.
- Use blueprints for domain-specific extraction requirements.
- Use projects to standardize outputs across teams and workflows.

## Exam Tips

- BDA is the Bedrock service for automating multimodal data extraction.
- Standard output = default insights; custom output = blueprint-driven extraction.
- Projects organize standard output configs + blueprints and are referenced in API calls.

## Sources

- https://aws.amazon.com/bedrock/bda/
- https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/bda-custom-output-idp.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/bda-projects.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/bda-blueprints-console.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/bda-cli-guide.html
- https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-data-automation-generally-available/
- https://aws.amazon.com/about-aws/whats-new/2025/11/bedrock-data-automation-synchronous-image-processing/
- https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-bedrock-knowledge-bases-processes-multimodal-data/
