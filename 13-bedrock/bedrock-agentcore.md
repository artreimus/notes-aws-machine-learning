---
title: "Amazon Bedrock AgentCore"
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
  - "Amazon Bedrock AgentCore"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Bedrock AgentCore

## Overview
- AgentCore is a set of managed services to **host, secure, and scale** agentic applications.
- It is framework-agnostic and supports any model provider; Bedrock models are optional.
- It complements (not replaces) Agents for Amazon Bedrock.

## Core Services
- AgentCore Runtime
  - Secure, serverless hosting for agents and tools.
  - Session isolation via microVMs and support for long-running workloads.
  - Supports multiple protocols (HTTP, MCP, A2A).
- AgentCore Gateway
  - A managed connectivity layer that turns APIs/Lambda into MCP-compatible tools.
  - Supports OpenAPI, Smithy, and Lambda inputs.
  - Provides inbound and outbound authentication for tools.
- AgentCore Identity
  - Workload identities for agents with inbound and outbound auth.
  - Integrates with IAM and OAuth/JWT identity providers.
  - Centralizes credential management and token storage.
- AgentCore Memory
  - Managed memory for short-term and long-term context.
  - Enables durable, cross-session personalization and summaries.

## Runtime Capabilities (Highlights)
- Framework-agnostic hosting for agents built with LangGraph, CrewAI, Strands, or custom code.
- Model flexibility (Bedrock or non-Bedrock providers).
- Protocol support via HTTP, MCP, and A2A contracts.
- Session isolation per user with dedicated microVMs.
- Supports bidirectional streaming for interactive experiences.

## Gateway Highlights
- Converts existing services into tools without custom MCP servers.
- Centralized tool discovery and routing through gateway endpoints.
- One place to manage tool auth and access policies.

## Identity and Memory Highlights
- Identity provides workload identities and OAuth-based access to third-party tools.
- Memory supports short-term session context and long-term summaries across sessions.

## Observability (AgentCore Resources)
- CloudWatch metrics and logs for runtime, memory, and gateway resources.
- Optional tracing and spans for deeper diagnostics.

## When to Use AgentCore
- You want to host custom agents or tools outside the Bedrock Agents managed runtime.
- You need secure identity management for tool access.
- You need managed memory for persistent context across sessions.
- You need a managed tool gateway for MCP-compatible tools.

## Relationship to Other Bedrock Features
- Agents for Bedrock: managed agent service with built-in orchestration and action groups.
- AgentCore: infrastructure layer to host **your** agent code and tools.

## Exam Tips
- AgentCore is about **runtime, identity, memory, and tool connectivity** for agent apps.
- It is framework-agnostic and not limited to Bedrock models.
- Use AgentCore when you need hosting, identity, memory, or a tool gateway for custom agents.

## Sources
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/configure-memory.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-service-contract.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html
