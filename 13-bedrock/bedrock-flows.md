# Prompt Flows (Amazon Bedrock Flows)

## Overview

- Prompt Flows was the preview name; the feature is now generally available as **Amazon Bedrock Flows**.
- It provides a visual, node-based builder to orchestrate multi-step generative AI workflows.
- Flows connect prompts, foundation models, knowledge bases, guardrails, and other AWS services into a single workflow.

## Why It Matters

- Lets teams build complex prompt chains and routing logic without heavy orchestration code.
- Speeds iteration with console-based testing and tracing.
- Supports versioning and aliases for safe promotion to production.

## Core Concepts

- Flow
  - A directed graph of nodes (steps) and connections.
- Node
  - A unit of work such as a prompt, model call, knowledge base query, or tool integration.
- Expressions
  - Map inputs/outputs between nodes to control data flow.
- Version and alias
  - Publish immutable versions and point aliases to the version you want to run.

## Lifecycle

1. Create
   - Build a flow in the Bedrock console or via the `CreateFlow` API.
2. Test
   - Run test inputs in the console and view per-node outputs with trace view.
3. Publish
   - Create an immutable version for production.
4. Deploy
   - Create an alias and invoke it from your application using `InvokeFlow`.

## Execution and Tracing

- Use the `InvokeFlow` API to run a flow and stream outputs.
- Enable tracing to view node-by-node inputs, outputs, and execution paths.
- Traces help debug routing, prompt chaining, and node errors.

## Integrations

- Prompts and foundation models for inference steps.
- Knowledge bases for RAG nodes.
- Guardrails attached to prompt or knowledge base nodes for safety.
- AWS services (for example, Lambda or Lex) to embed business logic and workflows.

## Typical Use Cases

- Multi-step customer support flows (classify → retrieve → draft → validate).
- Report generation pipelines with structured post-processing.
- Data-enrichment flows that combine retrieval and summarization.

## Considerations

- Flows are best for deterministic, well-defined pipelines.
- Complex dynamic reasoning or long multi-turn dialog may still need Agents.
- Costs and latency scale with the number of nodes and model calls.

## Exam Tips

- Prompt Flows is now called Amazon Bedrock Flows.
- It is a visual, node-based workflow builder with versioning and aliases.
- Invoked via `InvokeFlow` and supports tracing and guardrails at node level.

## Sources

- https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html
- https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateFlow.html
- https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeFlow.html
- https://aws.amazon.com/bedrock/flows/
- https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-bedrock-flows-new-capabilities/
- https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-flows-is-now-generally-available-with-enhanced-safety-and-traceability
- https://aws.amazon.com/blogs/machine-learning/streamline-generative-ai-development-in-amazon-bedrock-with-prompt-management-and-prompt-flows-preview
