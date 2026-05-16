---
title: "Amazon Bedrock AgentCore"
scope: "AWS Machine Learning and AI"
status: "supplemental"
domain:
  - "supplemental"
service:
  - "Amazon Bedrock AgentCore"
tags:
  - "aws"
  - "13_bedrock"
aliases:
  - "Amazon Bedrock AgentCore"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Bedrock AgentCore

## Knowledge Relevance

Supplemental current Bedrock note for production agentic AI. AgentCore is useful for architecture decisions around custom agent deployment, tool access, memory, identity, monitoring, and evaluation.

## When To Use

- Use AgentCore when you need to deploy and operate custom agents securely at production scale.
- Use AgentCore when open-source agent frameworks or non-Bedrock models must run with AWS-grade identity, memory, tool governance, observability, and evaluations.
- Use Agents for Amazon Bedrock instead when a managed Bedrock agent with action groups and knowledge bases is enough.

## Core Concepts

- AgentCore is a modular platform to build, deploy, and operate agents using any framework and foundation model.
- It works with frameworks such as CrewAI, LangGraph, LlamaIndex, Google ADK, OpenAI Agents SDK, and Strands Agents.
- It supports models inside and outside Amazon Bedrock, including Anthropic Claude, Amazon Nova, Meta Llama, Mistral, OpenAI, and Google Gemini.
- It supports protocols such as MCP and A2A.

## Core Services
- AgentCore Runtime
  - Secure, serverless hosting for agents and tools.
  - Fast cold starts, extended runtime support, session isolation, built-in identity, and support for multimodal/multi-agent workloads.
  - Supports multiple protocols (HTTP, MCP, A2A).
- AgentCore Gateway
  - A managed connectivity layer that turns APIs/Lambda into MCP-compatible tools.
  - Can connect to existing MCP servers and popular enterprise integrations.
  - Provides inbound and outbound authentication for tools.
- AgentCore Identity
  - Workload identities for agents with inbound and outbound auth.
  - Integrates with IAM and OAuth/JWT identity providers.
  - Centralizes credential management and token storage.
- AgentCore Memory
  - Managed memory for short-term and long-term context.
  - Enables durable, cross-session personalization and summaries.
- AgentCore Browser
  - Fully managed browser runtime for web navigation, form filling, and information extraction.
- AgentCore Code Interpreter
  - Isolated sandbox for code execution in agent workflows.
- AgentCore Observability
  - Tracing, debugging, and performance monitoring for production agents.
- AgentCore Evaluations
  - Automated quality assessment over sessions, traces, and spans.
- AgentCore Policy
  - Deterministic control over tool access and action boundaries.
- AgentCore Registry
  - Catalog for agents, MCP servers, tools, skills, and custom resources.

## AWS Services And Features

- AgentCore Runtime
- AgentCore Memory
- AgentCore Gateway
- AgentCore Identity
- AgentCore Browser
- AgentCore Code Interpreter
- AgentCore Observability
- AgentCore Evaluations
- AgentCore Policy
- AgentCore Registry

## Implementation Patterns

- Custom framework agent -> AgentCore Runtime -> AgentCore Gateway/MCP tools -> Identity/Policy -> Observability/Evaluations.
- Multi-agent platform -> shared Registry -> approved tools and MCP servers -> governed runtime deployments.
- Context-aware assistant -> Memory for session and durable context -> RAG/tool calls -> evaluated traces.

## Tradeoffs And Pitfalls

- AgentCore does not remove the need for agent design, tool schema quality, least privilege, or evaluation datasets.
- Browser and Code Interpreter tools are powerful but require sandbox, audit, and cost controls.
- Registry improves discoverability, but unsafe tools still require review and policy enforcement.
- Use AgentCore for custom agents; use Bedrock Agents for managed orchestration when it fits.

## Relationship to Other Bedrock Features
- Agents for Bedrock: managed agent service with built-in orchestration and action groups.
- AgentCore: infrastructure layer to host **your** agent code and tools.

## Decision Triggers

- AgentCore is about **runtime, identity, memory, and tool connectivity** for agent apps.
- It is framework-agnostic and not limited to Bedrock models.
- Use AgentCore when you need hosting, identity, memory, or a tool gateway for custom agents.

## Related Notes

- [[bedrock-agentcore-production-patterns]]
- [[bedrock-agents]]
- [[bedrock-multi-agent-collaboration]]
- [[model-context-protocol-mcp]]
- [[agentic-ai-current-innovation-map]]
- [[strands-ai]]

## Sources
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/configure-memory.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-service-contract.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html
