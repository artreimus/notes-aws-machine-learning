---
title: "Claude Agentic AI on AWS"
scope: "AWS Machine Learning and AI"
status: "supplemental"
domain:
  - "supplemental"
service:
  - "Anthropic Claude"
  - "Amazon Bedrock"
  - "Amazon Bedrock AgentCore"
tags:
  - "aws"
  - "agentic-ai"
  - "claude"
  - "bedrock"
  - "mcp"
aliases:
  - "Claude Agents on AWS"
  - "Claude Tool Use on AWS"
last_verified: "2026-05-16"
source_type: "official-docs"
---

# Claude Agentic AI on AWS

## Knowledge Relevance

Supplemental note for current Claude capabilities that influence AWS agentic architectures. MLA-C01 may mention Bedrock and foundation models, but detailed Claude model/version features move faster than the exam guide.

## When To Use

- Use Claude models for reasoning-heavy, coding, analysis, long-context, multimodal, and tool-using agent workflows.
- Use Claude through Amazon Bedrock when AWS governance, IAM, VPC-style architecture, Bedrock Guardrails, Knowledge Bases, or Bedrock Agents are central.
- Use Claude Platform on AWS or the Claude API when first-party Claude features are needed and are not exposed through Bedrock.
- Use extended thinking for complex reasoning tasks where extra latency and token cost are justified.

## Core Concepts

- Current Claude docs position Opus 4.7 as the most capable generally available Claude model for complex tasks and agentic coding.
- Claude model availability and IDs differ across Claude API, Claude Platform on AWS, Amazon Bedrock, Vertex AI, and Microsoft Foundry.
- Amazon Bedrock documentation lists Claude 3.7 and Claude 4-family support for extended thinking, including Claude Opus 4.5, Sonnet 4.5, Haiku 4.5, Sonnet 4, Opus 4, and Claude 3.7 Sonnet.
- Extended thinking uses a thinking budget and can work with tool use, but it increases latency and cost and has feature compatibility rules.
- The Claude API MCP connector can connect to remote MCP servers without a separate MCP client, but current docs state it is not currently available on Amazon Bedrock or Vertex AI.
- Amazon Bedrock prompt caching supports a 1-hour TTL option for select Claude 4.5 models, useful for long-running agentic workflows.

## AWS Services And Features

- Amazon Bedrock model invocation for Claude
- Claude in Amazon Bedrock
- Bedrock Agents with Claude-compatible foundation models
- Bedrock Knowledge Bases for RAG with Claude generation
- Bedrock prompt caching for select Claude models
- Bedrock AgentCore for hosting custom Claude-powered agents

## Implementation Patterns

- Bedrock managed agent: app -> Agents for Bedrock -> Claude model -> action groups/knowledge base -> trace.
- Custom Claude agent on AWS: app -> AgentCore Runtime -> Claude API or Bedrock Claude model -> MCP/tools -> memory/evals/observability.
- RAG with Claude: data source -> Bedrock Knowledge Base -> retrieve/rerank -> Claude generation -> citation/evaluation.
- Long-running agent: stable system prompt/tools -> prompt cache -> repeated tool/retrieval turns -> trace/evaluate.

## Tradeoffs And Pitfalls

- Do not assume every Claude API feature is available through Amazon Bedrock.
- Do not hard-code generic model aliases for production without checking provider versioning and deprecation policy.
- Extended thinking is best for complex tasks, not every chat turn.
- Tool use with thinking has constraints, including limitations around forced tool choice.
- Prompt caching helps repeated prefixes and long-running agents, but cache TTL and pricing vary by model and provider.
- MCP connector data-retention and ZDR eligibility must be checked before using it for sensitive workloads.

## Decision Triggers

- "Claude + AWS governance" points to Amazon Bedrock.
- "Claude + first-party MCP connector" points to Claude API / Claude Platform documentation, not Bedrock.
- "Complex reasoning with traceable thinking budget" points to extended thinking.
- "Stable long context across agent steps" can point to prompt caching plus memory, depending on requirements.
- "Private data grounded answers" points to RAG/Knowledge Bases with Claude as the generation model.

## Related Notes

- [[amazon-bedrock]]
- [[bedrock-agents]]
- [[bedrock-agentcore]]
- [[bedrock-rag-decision-guide]]
- [[model-context-protocol-mcp]]
- [[agentic-rag-patterns]]

## Sources

- https://platform.claude.com/docs/en/about-claude/models/overview
- https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
- https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
- https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html
- https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-bedrock-one-hour-duration-prompt-caching/
