# Multi‑LLM Routing Strategies on AWS (Bedrock)

## Source
- Blog: “Multi‑LLM routing strategies for generative AI applications on AWS” (Apr 9, 2025)
  - https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/

## Why Multi‑LLM
- A single model rarely optimizes for every task, domain, latency, or cost constraint.
- Multi‑LLM routing lets you match each request to the most appropriate model.

## Common Multi‑LLM Scenarios
- **Multiple task types**: generation, summarization, classification, extraction.
- **Multiple complexity levels**: simple vs. complex queries within the same task.
- **Multiple domains**: finance, legal, HR, operations with domain‑tuned models.
- **SaaS tiering**: smaller models for basic tiers, specialized models for premium tiers.

## Routing Strategies

### 1) Static Routing
- Separate UI components or endpoints per task.
- Simple to implement and modular.
- Less flexible when tasks evolve (new UI component required).

### 2) Dynamic Routing
Single entry point, routing happens behind the scenes.

#### LLM‑assisted routing
- A classifier LLM decides the route.
- Strong at fine‑grained classification, but adds cost and latency.
- Requires tuning and monitoring as tasks change.

#### Semantic routing
- Uses embeddings and similarity search against reference prompts.
- Efficient, scalable to many task categories.
- Requires a high‑coverage reference set and extra infra (vector DB + embeddings).

#### Hybrid routing
- Semantic routing for coarse category → classifier LLM for fine decisions.
- Balances scalability with precision.

## AWS Implementation Options

### Built‑in: Bedrock Intelligent Prompt Routing
- A single serverless endpoint routes within a **model family** (Claude or Llama).
- Uses prompt matching and model understanding to pick the best model for cost/quality.
- Blog claims up to **30% cost reduction** without quality loss.
- Example: Claude Sonnet vs. Haiku; Llama 70B vs. 8B.

### Custom Routing
- Build your own classifier or semantic router if you:
  - Use models outside Bedrock (SageMaker, EKS, third‑party APIs).
  - Need custom routing logic beyond model‑family routing.

#### Example architecture (LLM‑assisted routing)
- API Gateway → Lambda → classifier LLM → target LLM.
- Classifier chooses domain (e.g., history vs. math) and routes accordingly.

## Design Considerations
- Latency vs. accuracy trade‑off for classifier LLMs.
- Embedding coverage and maintenance for semantic routing.
- Cost control with intelligent routing + smaller models.
- Observability for routing decisions and per‑model outcomes.

## Exam Tips
- **Static routing** = multiple UI components/endpoints.
- **Dynamic routing** = classifier LLM, semantic routing, or hybrid.
- **Bedrock Intelligent Prompt Routing** supports routing within **Claude** or **Llama** families.

