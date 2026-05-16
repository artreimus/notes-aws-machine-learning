---
title: "Prompt Caching in Amazon Bedrock"
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
  - "Prompt Caching in Amazon Bedrock"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Prompt Caching in Amazon Bedrock

## Overview
- Prompt caching reduces inference cost and latency by reusing cached prompt prefixes across requests.
- It is useful when a large, static prefix (system instructions, few-shot examples, or shared context) is reused frequently.
- Bedrock stores internal model state for cached prefixes so repeated inputs skip recomputation.

## How It Works
- You mark contiguous prompt prefixes as cache points (cache checkpoints).
- On the first request, Bedrock computes the prefix and writes it to cache.
- On subsequent requests with the exact same prefix, Bedrock reads from cache and skips recomputing those tokens.
- Cache hits reduce input token processing cost and latency for the cached section.

## Key Concepts
- Cache checkpoint
  - A marker for the prompt prefix that should be cached.
- Prefix matching
  - Cache hits require an exact match on the cached prefix tokens.
- TTL
  - Cached prefixes expire after a short time (5 minutes) and reset on cache hits.

## Where It Fits
- Chatbots with long system prompts or shared policy content.
- RAG apps that repeatedly include the same instructions and examples.
- Code assistants with long static context files.
- Agent workflows that reuse large, stable prompts across turns.

## Supported Models (Examples)
- Anthropic Claude 3.5 Haiku, Claude 3.7 Sonnet.
- Amazon Nova Micro, Nova Lite, Nova Pro (and related Nova family models where supported).
- Always confirm availability per region and model in the latest Bedrock docs.

## API Usage (Conceptual)
- Use the Bedrock Converse API and add `cachePoint` blocks to the `messages` list to mark cached prefixes.
- Cache points should cover only stable, reusable content.
- Dynamic content (user input, current question) should come after the cached prefix.

## Costs and Metrics
- Cache reads are billed at a reduced rate; cache writes can be billed differently than standard input tokens.
- Use the response `usage` fields and CloudWatch metrics to track:
  - Cache read input tokens.
  - Cache write input tokens.
- Expect best savings when the cached prefix is large and reused frequently.

## Best Practices
- Put static content first and mark it as the cache prefix.
- Keep cached content identical between requests to maximize hit rate.
- Use caching when repeated long prompts dominate token usage.
- Monitor cache hits/misses to validate ROI.

## Limitations and Gotchas
- Only supported models can use prompt caching.
- Cache hits require exact prefix matches; small changes break reuse.
- Short prefixes might not meet per-model minimum token thresholds for caching.
- Cache TTL is short; workloads with infrequent requests may not benefit.

## Exam Tips
- Prompt caching is a Bedrock feature to reduce latency and cost for repeated prompt prefixes.
- It is enabled via cache checkpoints in the Converse API and requires supported models.
- The cached prefix must be identical across requests to achieve cache hits.

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html
- https://aws.amazon.com/bedrock/prompt-caching/
- https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-general-availability-prompt-caching/
- https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock
- https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_CachePointBlock.html
