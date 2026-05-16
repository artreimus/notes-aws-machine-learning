---
title: "Bedrock RAG Decision Guide"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "2.1"
  - "3.1"
  - "4.1"
service:
  - "Amazon Bedrock"
tags:
  - "aws"
  - "mla-c01"
  - "bedrock"
  - "rag"
aliases:
  - "Bedrock RAG Decision Guide"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Bedrock RAG Decision Guide

## Knowledge Relevance

Decision guide for Bedrock RAG, chunking, vector store selection, pre-retrieval filtering, and evaluation.

## When To Use

- Use RAG when answers must be grounded in private or frequently changing knowledge.
- Use Knowledge Bases for managed ingestion/retrieval/generation workflows.
- Use custom RAG when retrieval, orchestration, or ranking needs exceed managed defaults.

## Core Concepts

- RAG quality depends on source documents, chunking, embedding model, vector store, filters, prompts, citations, and evaluation.
- S3 Vectors can integrate with Bedrock Knowledge Bases as an S3-native vector store option.
- Pre-retrieval filtering narrows candidate context before retrieval/generation.

## AWS Services And Features

- Bedrock Knowledge Bases
- Amazon S3 Vectors
- OpenSearch Service
- Aurora PostgreSQL pgvector
- Bedrock Evaluations

## Implementation Patterns

- Documents -> chunking -> embeddings/vector store -> retrieval/filtering -> generation -> citation/evaluation.

## Tradeoffs And Pitfalls

- RAG does not guarantee correctness.
- Poor chunking or missing metadata reduces retrieval quality.
- Evaluate faithfulness, citation coverage, correctness, and harmfulness.

## Decision Triggers

- Private corpus Q&A points to RAG.
- Need managed retrieval/generation points to Bedrock Knowledge Bases.
- Need exact unchanged repeated prompt prefix points to prompt caching, not RAG.

## Related Notes

- [[bedrock-knowledge-base]]
- [[chunking-strategies]]
- [[pre-retrieval-knowledge-base]]
- [[optimizing-vector-store-and-embeddings]]


## Sources

- https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-bedrock-kb.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
