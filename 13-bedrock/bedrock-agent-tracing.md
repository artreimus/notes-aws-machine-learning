---
title: "Agent Tracing in Amazon Bedrock"
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
  - "Agent Tracing in Amazon Bedrock"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Agent Tracing in Amazon Bedrock

## Overview

- Agent tracing lets you follow an agent’s step-by-step orchestration: what it decided, which action groups or knowledge bases it called, and how it formed the final response. 
- Tracing is enabled per invocation by setting `enableTrace` to `true` in `InvokeAgent`. 

## Why It Matters

- Debugging: Identify where the agent made a wrong decision or used the wrong tool.
- Observability: Understand the reasoning and inputs/outputs at each step.
- Governance: Support auditability and troubleshooting for production agents.

## How to Enable Tracing

- In the **InvokeAgent** request, set `enableTrace` to `true`. 
- Traces are returned in the response stream alongside chunks of the agent’s output. 

## What the Trace Contains

- Metadata: agent ID, alias ID, version, session ID, and optional collaborator name (for multi-agent collaboration). 
- Orchestration details: which action group or knowledge base was invoked, with inputs and outputs.
- Rationale: the reasoning behind the agent’s choice of action or retrieval step. 

## Where It Appears

- **InvokeAgent** streaming response includes `trace` events next to `chunk` output. 
- Each trace event shows the step-by-step path from user input to final response. 

## Related Observability

- CloudWatch provides metrics for Bedrock Agents such as invocations, latency, and token usage. 
- Tracing is for step-level reasoning, while CloudWatch metrics track performance trends. 

## Best Practices

- Turn on tracing during development and debugging.
- Log traces for troubleshooting, but protect sensitive data.
- Combine traces with CloudWatch metrics to diagnose both logic and performance issues.

## Exam Tips

- Tracing is enabled with `enableTrace` in `InvokeAgent`.
- Trace events show action group and knowledge base usage plus reasoning.
- CloudWatch metrics are separate from tracing and focus on performance signals. 

## Sources

- https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html
- https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents-invoke-agent.html
- https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-bedrock-agents-metrics-cloudwatch/
