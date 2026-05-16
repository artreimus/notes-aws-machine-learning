---
title: "Token-Level Redaction in Amazon Bedrock (Guardrails)"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
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
  - "Token-Level Redaction in Amazon Bedrock (Guardrails)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Token-Level Redaction in Amazon Bedrock (Guardrails)

## Overview
- Bedrock implements token-level redaction through **Guardrails sensitive information filters**.
- When configured to **Mask**, the service replaces detected sensitive spans with placeholder tokens like `{NAME}` or `{EMAIL}`. 
- This applies to both **input prompts** and **model responses**, enabling pre- and post-redaction. 

## How Redaction Works
- Sensitive information detection is **context-dependent** and probabilistic (ML-based). 
- When the policy action is **Mask**, the output replaces detected spans with PII type tokens (for example `{EMAIL}`). 
- You can also choose **Block** to stop the request/response entirely. 
- **Detect** mode is available to evaluate guardrail behavior without blocking or masking. 

## What Can Be Redacted
- Built-in PII types (e.g., name, email, address, phone, etc.). 
- Custom sensitive patterns via **regex**. 
- Detection works across **natural language and code** (comments, string literals, variable names). 

## Where It Fits
- Customer support summaries (mask user PII in transcripts). 
- Compliance workflows that require removal of identifiers before storage or downstream use.
- RAG systems where retrieved text may include sensitive fields.

## Practical Notes
- Guardrails apply to model prompts and responses (excluding reasoning content blocks). 
- Use **Mask** for safe redaction; use **Block** for strict zero‑tolerance policies. 

## Exam Tips
- Token-level redaction in Bedrock is implemented via Guardrails **sensitive information filters**.
- **Mask** replaces detected spans with placeholder tokens; **Block** rejects the content. 
- Redaction can apply to both input and output in the same invocation. 

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-harmful-content-handling-options.html
- https://aws.amazon.com/bedrock/guardrails/
