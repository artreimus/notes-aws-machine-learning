---
title: "Bedrock Application Patterns"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "2.1"
  - "3.1"
service:
  - "Amazon Bedrock"
tags:
  - "aws"
  - "mla-c01"
  - "bedrock"
  - "generative-ai"
aliases:
  - "Bedrock Application Patterns"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Bedrock Application Patterns

## Exam Relevance

Canonical pattern note for common Amazon Bedrock application designs without duplicating every Bedrock feature note.

## When To Use

- Use for choosing between direct model invocation, RAG, agents, flows, guardrails, evaluation, and prompt management patterns.
- Use as a map into the canonical `13-bedrock` notes.

## Core Concepts

- Direct invocation handles simple prompt/response tasks.
- RAG uses Knowledge Bases/vector stores for grounded answers.
- Agents use tools/action groups for task execution.
- Guardrails and evaluation control risk and quality.

## AWS Services And Features

- Amazon Bedrock
- Bedrock Knowledge Bases
- Bedrock Agents
- Bedrock Flows
- Bedrock Guardrails
- Bedrock Evaluations

## Implementation Patterns

- Prompt app -> prompt management -> Converse API -> guardrails -> evaluation.
- Enterprise Q&A -> Knowledge Base/RAG -> citations -> guardrails -> model evaluation.

## Tradeoffs And Pitfalls

- Do not use agents for simple static prompt workflows.
- RAG quality depends on ingestion, chunking, retrieval, and evaluation.
- Guardrails reduce risk but do not prove correctness.

## Exam Triggers

- Grounded enterprise Q&A points to RAG/Knowledge Bases.
- Tool use and task execution point to Agents.
- Prompt versioning points to Prompt Management.

## Related Notes

- [[amazon-bedrock]]
- [[bedrock-knowledge-base]]
- [[bedrock-agents]]
- [[bedrock-guardrails]]


## Sources

- https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
