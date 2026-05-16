---
title: "Strands Agents in Amazon Bedrock"
exam: "MLA-C01"
status: "supplemental"
domain:
  - "supplemental"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "14_agentic_ai"
aliases:
  - "Strands Agents in Amazon Bedrock"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Strands Agents in Amazon Bedrock

## Overview
- Strands Agents is an open-source, code-first SDK from AWS for building agentic AI applications.
- It is model-first: the LLM drives planning, tool calls, and reasoning loops.
- It integrates with Amazon Bedrock for model inference, but runs in your own environment (not a managed Bedrock Agent).

## What Strands Agents Is (and Is Not)
- Is
  - A flexible SDK for custom agent orchestration, tools, and multi-agent patterns.
  - Available in Python and TypeScript.
- Is not
  - A managed service like Agents for Amazon Bedrock.
  - A console-first configuration workflow.

## Core Concepts
- Agent
  - LLM configuration + system prompt + tool definitions + runtime limits.
- Tools
  - Functions or API wrappers with structured schemas to enable safe tool calling.
- Memory
  - Conversation history plus optional external stores for long-term context.
- Orchestration
  - A loop that runs tool selection, execution, and response synthesis with step limits.
- Observability
  - Logs and traces for tool calls, model responses, and errors.

## Bedrock Integration
- Models
  - Supports Bedrock foundation models that can do tool use and streaming (e.g., Claude, Amazon Nova).
- Knowledge
  - Can call Bedrock Knowledge Bases via tools for RAG workflows.
- Guardrails
  - Use Bedrock Guardrails at inference time or add custom validation in tools.
- Security
  - Use IAM roles and least privilege for Bedrock and any tool-backed AWS services.

## Deployment Options
- Self-hosted environments (local, containers, Lambda, ECS, etc.).
- Amazon Bedrock AgentCore Runtime supports running open-source agent frameworks such as Strands Agents in a managed serverless runtime.

## When to Use Strands Agents
- You need custom orchestration or non-standard control flow.
- You want full control over tools, retries, timeouts, and multi-agent patterns.
- You are building outside the managed Bedrock Agents runtime but still want Bedrock models.

## Tradeoffs
- Pros
  - High flexibility, easy integration with custom tools and services.
- Cons
  - You manage infrastructure, monitoring, and scaling.
  - More engineering effort compared with managed Agents for Bedrock.

## Exam Tips
- Strands Agents is an OSS SDK that can use Bedrock models, not a managed Bedrock Agent feature.
- Use it when you need custom orchestration or multi-agent workflows beyond managed Bedrock Agents.
- Know that Bedrock AgentCore Runtime can host open-source agent frameworks like Strands.

## Sources
- https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/strands-agents.html
- https://strandsagents.com/latest/documentation/docs/
- https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/
- https://strandsagents.com/latest/documentation/docs/user-guide/deploy/deploy_to_bedrock_agentcore/
