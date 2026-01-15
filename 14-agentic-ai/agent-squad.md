# Agent Squad in Amazon Bedrock

## Overview
- Agent Squad is an open-source framework (AWS Labs) for multi-agent orchestration.
- It is not a native Bedrock service, but it can use Bedrock models for routing and agent responses.
- The framework coordinates multiple specialized agents through an orchestrator and optional classifier.

## Core Building Blocks
- Orchestrator
  - The main controller that receives user input, routes to agents, and returns results.
- Classifier (Router)
  - Chooses the best agent for a request (often using a Bedrock model).
  - The default Bedrock Classifier uses structured outputs to map queries to agent types.
- Agents
  - Specialized agents with narrow scopes and tailored prompts/tools.
  - Built-in examples include Bedrock LLM Agents and Amazon Bedrock Agent wrappers.
- Memory
  - Shared context for routing and response aggregation.

## Execution Flow
1. User input arrives at the orchestrator.
2. The classifier selects an agent (or multiple agents).
3. The selected agent(s) run and return results.
4. The orchestrator aggregates and returns the final response.

## Bedrock Integration
- Bedrock Classifier
  - Uses Bedrock models (e.g., Claude) to route requests to the right agent.
- Bedrock LLM Agents
  - Use Bedrock models for agent responses.
- Amazon Bedrock Agent wrapper
  - Lets an Agent Squad member delegate to a managed Bedrock Agent.

## Multi-Agent Coordination Patterns
- Supervisor Agent (agent-as-tools)
  - A lead agent calls teammates as tools and merges outputs.
- Fan-out / fan-in
  - Parallel specialist agents with a final aggregation step.
- Map-reduce
  - Split tasks into chunks, process in parallel, then summarize.

## Use Cases
- Enterprise Q&A with specialized policy, data, and compliance agents.
- Data + action workflows (retrieve, analyze, then act).
- Domain-specific assistants with clear routing logic.

## Relationship to Bedrock Multi-Agent Collaboration
- Bedrock multi-agent collaboration is a managed feature inside Agents for Bedrock.
- Agent Squad is a self-managed, open-source framework with full control of orchestration logic.
- Use managed collaboration when you want a console-first, managed setup.
- Use Agent Squad when you need custom routing, custom agents, or bespoke orchestration.

## Tradeoffs
- Pros
  - Strong separation of concerns and higher accuracy for complex tasks.
- Cons
  - Higher orchestration complexity, latency, and cost.
  - You manage infra, routing logic, and observability.

## Exam Tips
- Agent Squad is an OSS framework, not a Bedrock managed feature.
- Bedrock multi-agent collaboration is a managed capability of Agents for Bedrock.
- Both can use Bedrock models; choose based on control vs. managed convenience.

## Sources
- https://awslabs.github.io/agent-squad/
- https://awslabs.github.io/agent-squad/general/quickstart/
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- https://aws.amazon.com/solutions/guidance/multi-agent-orchestration-on-aws
- https://awslabs.github.io/agent-squad/agents/built-in/supervisor-agent/
- https://awslabs.github.io/agent-squad/agents/built-in/amazon-bedrock-agent/
