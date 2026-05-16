---
title: "Amazon Bedrock Agent Memory"
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
  - "Amazon Bedrock Agent Memory"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Bedrock Agent Memory

## Overview
- Agents for Amazon Bedrock can retain conversational context across sessions using **agent memory**.
- By default, an agent only keeps context within a single session; memory enables cross-session recall.
- This is distinct from **AgentCore Memory**, which is for hosting custom agents outside the managed Agents service.

## How Agent Memory Works
- Session-based context
  - Each conversation is a session identified by `sessionId`.
  - Reusing the same `sessionId` continues the same session context.
- Cross-session memory
  - When memory is enabled, Bedrock creates session summaries asynchronously after a session ends.
  - Summaries are associated with a `memoryId` that you pass to retrieve the right user’s memory.

## Configuration
- Enable memory when creating or updating an agent.
- Configure retention (storage days) and the maximum number of recent sessions to keep.
- You can view/edit the session summarization prompt used to generate memory summaries.

## Retention and Limits
- Retention duration is configurable (1–365 days).
- Old summaries are deleted after the retention window.
- Memory is summary-based, not full transcript storage.

## When to Use
- Personalization across sessions (preferences, past choices).
- Task continuity across multiple visits.
- Reducing prompt length by reusing summaries instead of raw chat history.

## Best Practices
- Use a stable `memoryId` per user or tenant.
- Keep memory retention aligned with privacy and compliance needs.
- Avoid storing sensitive data unless policy allows it.
- Use agent memory for high-level summaries, not precise audit trails.

## Exam Tips
- Agent memory is a managed feature of **Agents for Amazon Bedrock**.
- It uses session summaries for cross-session recall and is configured with retention.
- It is separate from **AgentCore Memory**, which is for custom agents.

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents-configure-memory.html
- https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_MemoryConfiguration.html
