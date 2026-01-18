# Agents for Amazon Bedrock

## Overview
- Managed service to build AI agents that orchestrate multi-step tasks.
- Agents combine a foundation model with **action groups** (APIs/Lambda) and **knowledge bases** (RAG) to answer questions and take actions.
- Bedrock handles orchestration, reasoning steps, and tool invocation.

## Core Concepts
- Agent
  - A managed runtime configuration with instructions, a model, and optional tools.
- Action groups
  - Define actions an agent can take (often via Lambda) using OpenAPI or function schemas.
- Knowledge bases
  - Attached data sources the agent can query during orchestration.
- Orchestration
  - The agent decides whether to call an action group, query a knowledge base, or respond.
- Alias and versioning
  - Create versions and route production traffic via aliases.
- Traces
  - Orchestration traces show action selection, inputs, outputs, and rationale.

## How It Works (High Level)
1. User request enters the agent.
2. Orchestration model selects action groups or knowledge bases as needed.
3. Actions run (Lambda/API) or KB retrieval happens.
4. The agent synthesizes a final response.

## Common Use Cases
- Customer support agents that retrieve policy data and trigger workflows.
- IT helpdesk automation (diagnose → lookup → execute actions).
- Business process flows that require RAG + tool invocation.

## Best Practices
- Keep action groups narrowly scoped with clear schemas.
- Associate a knowledge base only when RAG is required.
- Use aliases to promote tested versions safely.
- Review orchestration traces to debug and tune prompts.

## Exam Tips
- Agents for Bedrock is a **managed** agent service.
- Action groups define tools (often Lambda-backed), knowledge bases provide RAG.
- Orchestration is managed by Bedrock and can be traced.

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents-how.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create.html
- https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_OrchestrationTrace.html
- https://aws.amazon.com/blogs/aws/agents-for-amazon-bedrock-is-now-available-with-improved-control-of-orchestration-and-visibility-into-reasoning
