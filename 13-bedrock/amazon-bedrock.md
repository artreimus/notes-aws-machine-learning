# Amazon Bedrock (deep dive notes)

## 1) What it is

Amazon Bedrock is a **fully managed AWS service** that gives you access to a variety of **foundation models (FMs)**—from Amazon and multiple third-party providers—through a **unified set of APIs**, plus “production glue” for building GenAI apps: **guardrails, agents, retrieval (knowledge bases), evaluations, prompt management, model customization, and private networking**.

### What makes Bedrock different (useful mental frame)

Think of Bedrock as:

- **A model router** (many providers, one general interface for chat-style apps)
- **A governance layer** (policy, logging, quotas, enterprise controls)
- **An application platform** for common GenAI patterns (agents, RAG, evaluations, prompt lifecycle)

## 2) Key concepts and glossary

- **Foundation model (FM):** Large pre-trained model that can generate text/images/video or embeddings.
- **Model ID:** Region-agnostic identifier you pass to runtime APIs.
- **On-demand throughput:** Default pay-per-use inference capacity.
- **Provisioned Throughput:** Reserved/dedicated capacity for predictable performance.
- **Custom model:** Model produced by Bedrock customization (fine-tune / continued pre-training / reinforcement fine-tuning / distillation).
- **Imported model:** A model you bring into Bedrock via Custom Model Import.
- **Inference parameters:** Controls for generation randomness/length (e.g., temperature, top_p, maxTokens, stop sequences).
- **Guardrails:** Policy layer that evaluates and filters prompts/responses for safety & privacy.
- **Agents:** Managed orchestration that plans, calls tools/APIs, and optionally uses a knowledge base.

## 3) Architecture: control plane vs runtime plane

A practical way to organize Bedrock in your head:

### A) Control plane (configure/manage)

Used when you are **setting things up**:

- Model access and permissions
- Agents (create, configure action groups, aliases)
- Guardrails (create, configure policies)
- Prompt management (store prompts, versions)
- Customization jobs (fine-tune / continued pre-training / reinforcement fine-tune / distill)
- Model import jobs
- Provisioned Throughput purchase/management
- Evaluation jobs

### B) Runtime plane (invoke)

Used when your application is **serving traffic**:

- Invoke models (single prompt or messages)
- Stream outputs
- Count tokens
- Apply guardrails
- Async invoke (for supported workloads)

## 4) Model access and lifecycle

### 4.1 Requesting model access

Before you can use many FMs, you typically **request access** in the Bedrock console (“Model access”). AWS exposes controls tied to provider/product IDs, and IAM policies can restrict who can request or use particular models.

### 4.2 Model discovery

You’ll usually do one of these:

- Use the console to browse providers/base models.
- Use APIs/SDKs to list models and inspect capabilities (modalities, streaming support, deprecation status).

### 4.3 Regions and model availability

Not every model is available in every region. Always treat **region + model ID** as a pair and build fallback logic (or an explicit allowlist) in production.

## 5) Inference APIs (the “how do I call the model?” layer)

Bedrock has **two main styles** of calling LLMs:

### 5.1 Converse / ConverseStream (recommended for chat-style apps)

Use this for “messages in, messages out” conversational interfaces.

- Benefits: **more consistent** request structure across models that support messages.
- You can still pass **model-specific** parameters when needed.

### 5.2 InvokeModel / InvokeModelWithResponseStream (direct invocation)

Use this for:

- Non-chat prompts
- Modalities that vary heavily by provider/model
- Embeddings requests (depending on model)

### 5.3 Other runtime operations you should know exist

- **CountTokens:** Estimate token usage before invoking.
- **ApplyGuardrail:** Evaluate/filter content with a guardrail.
- **StartAsyncInvoke / GetAsyncInvoke / ListAsyncInvokes:** For supported asynchronous invocations.
- **(Advanced) bidirectional streaming operation:** Exists for certain use cases/models.

### 5.4 Data handling note (important nuance)

Bedrock’s runtime docs state that Bedrock doesn’t store the content you provide for model inference beyond what’s needed to generate the response.
However:

- If you enable **Model invocation logging**, prompts/responses _can_ be captured to CloudWatch Logs and/or S3 (you are opting into storage for observability/compliance).

## 6) Inference parameters (controlling generation)

Bedrock supports common knobs, but **valid ranges and exact fields vary by model**.

### 6.1 The “big three”

- **temperature:** Higher = more randomness/creativity; lower = more deterministic.
- **top_p (nucleus sampling):** Restricts sampling to a probability mass.
- **maxTokens (or equivalent):** Upper bound on generated tokens.

Practical rule: in many model families, you typically tune **temperature OR top_p** (not both aggressively).

### 6.2 Stop sequences

Use stop sequences to prevent the model from continuing into unwanted formats (e.g., stopping at `\n\nUser:` or `</final>` markers).

### 6.3 Token budgeting

Build systems that are token-aware:

- Count tokens for inputs and expected output.
- Truncate/summarize conversation history.
- Use retrieval to bring only relevant context.

## 7) Token counting and quotas

### 7.1 CountTokens API

CountTokens returns the token count that would be used for an inference request (useful for cost/limit estimation and guardrails).

### 7.2 Quotas and token “burn-down”

Bedrock enforces quotas that commonly include:

- **TPM (tokens per minute)**
- **TPD (tokens per day)**
  These may differ by model and can be increased for some limits via Service Quotas.

Production implication: you need **backpressure** strategies:

- Queueing / rate limiting
- Model fallback
- Request shaping (smaller context)

## 8) Provisioned Throughput (predictable capacity)

When you need consistent latency/throughput, Bedrock offers **Provisioned Throughput**.

Key ideas:

- You purchase capacity either **by tokens** or **by model units**, depending on the model.
- You can associate provisioned throughput with certain resources (for example, via routing configurations / aliases in some agent setups).

When to use:

- Spiky but business-critical traffic
- Low-latency interactive workloads
- Quota pressure on on-demand throughput

## 9) Prompt management (prompt lifecycle as a first-class object)

Prompt management lets you create/store reusable prompts with:

- Variables (template parameters)
- A selected model + inference parameter settings
- Versioning and metadata (useful for teams)

Use cases:

- Keeping prompts consistent across services
- A/B testing prompt variants (in a controlled way)
- Governance (who changed what, when)

## 10) Guardrails (safety + privacy policy layer)

Bedrock Guardrails provides configurable safeguards you can apply across models and across features.

### 10.1 What guardrails can do (typical categories)

- **Harmful content filtering** (policy-based)
- **Sensitive information / PII detection and masking** (including regex-based custom patterns)
- **Topic restrictions / denied categories** (depending on configuration)

### 10.2 Where guardrails can be applied

- Direct model inference
- Agents
- Knowledge base queries

Practical design pattern:

- Use guardrails for **both input and output**.
- Treat guardrail failures as structured events: log, notify, and provide user-safe responses.

## 11) Agents (managed tool-using orchestration)

Agents for Amazon Bedrock let you create an agent that:

- Uses an FM for reasoning/planning
- Calls **action groups** (your APIs/tools)
- Optionally uses a **knowledge base** for retrieval
- Supports build-time configuration and runtime invocation

Key constructs you’ll see:

- **Action groups:** Grouped tool/API endpoints the agent can call.
- **Aliases / versions:** A production practice for stable deployments and safe updates.
- **Routing configuration:** Where you can point an alias to specific resources/capacity.

Design note:

- Agents are great when you need _multi-step tool use_ with managed ops.
- For tightly controlled flows or deterministic logic, many teams still combine agents with explicit orchestration code.

## 12) Model customization

Bedrock supports several customization approaches. Which ones you can use depends on the model.

### 12.1 Fine-tuning

Train on labeled instruction/response pairs to adapt a base model to your task.

### 12.2 Continued pre-training

“Keep training” on domain text to bias the model toward your domain language and knowledge.

### 12.3 Reinforcement fine-tuning

Feedback-driven optimization using reward signals (useful when you can formalize what “good” means).

### 12.4 Distillation

Train a smaller model to mimic a larger model (often used to reduce latency/cost).

Operational realities:

- Customization jobs can take hours.
- Data prep and evaluation are usually the bottleneck, not the button-click.

## 13) Custom Model Import (bring your own customized models)

Bedrock can import certain customized open-source models via **model import jobs** (S3 as the source). After import completes, you can invoke the imported model through runtime APIs.

Use case:

- You already customized a model outside Bedrock and want Bedrock’s managed serving + governance.

## 14) Evaluations (measure what matters)

Bedrock evaluations can assess:

- Foundation models (base/custom/imported)
- Knowledge bases and RAG workflows
- Potentially external sources/models (depending on workflow)

Common patterns:

- **Automatic evaluations** with built-in metrics and datasets.
- **LLM-as-a-judge** evaluations (use one model to score another) for quality dimensions that are hard to measure with classic metrics.

Best practice:

- Define success metrics per use case (helpfulness, factuality, refusal quality, safety, latency, cost).
- Keep a fixed evaluation suite so regressions are detectable.

## 15) Observability and operations

### 15.1 Model invocation logging

Bedrock can log invocation metadata and (optionally) model input/output to:

- CloudWatch Logs
- S3

Use cases:

- Debugging prompts and failures
- Compliance/audit needs
- Creating derived metrics (e.g., refusal rate, PII detection rate)

### 15.2 Monitoring token/throughput

Track:

- Request rate
- Latency (p50/p95/p99)
- Tokens per request
- TPM/TPD consumption
- Error types (throttling, validation, access denied, model errors)

## 16) Networking & data protection

### 16.1 Private connectivity with AWS PrivateLink

You can create **interface VPC endpoints** to reach Bedrock privately from your VPC (no public internet path required).

### 16.2 Encryption

Typical enterprise stance:

- TLS in transit
- KMS-backed encryption at rest for any logs/artifacts stored in AWS services you control (S3, CloudWatch, etc.)

### 16.3 Data handling pitfalls

- Turning on invocation logging can store prompts/responses; treat that as sensitive data.
- Apply least privilege IAM; separate roles for dev/test/prod.

## 17) Cost model (how you get billed)

Costs depend on the capability:

- **On-demand inference:** Typically billed by input/output tokens (or per-image/per-video for some modalities).
- **Provisioned Throughput:** Billed by reserved capacity/time commitment.
- **Customization/evaluations:** Billed based on training/eval resources and usage.

Cost control levers:

- Reduce tokens (better chunking, better retrieval, tighter prompts)
- Use smaller/faster models where adequate
- Cache responses for repetitive queries
- Use provisioned throughput only when it pays for itself in reliability/latency

## 18) Practical best practices (things that save you in production)

### 18.1 Model selection

- Start with 2–3 candidate models and evaluate on your task.
- Keep at least one fallback model for quota/availability issues.

### 18.2 Prompting

- Keep system instructions stable and minimal.
- Structure outputs with schemas when possible.
- Use Prompt Management for lifecycle discipline.

### 18.3 RAG (even if you’ll cover it separately)

- Prefer retrieval for fresh/enterprise knowledge.
- Be strict about citations or grounding in retrieved context.

### 18.4 Safety

- Apply guardrails on both input/output.
- Log safety events and iterate on policies.

### 18.5 Quotas and resilience

- Implement retries with jitter on throttling.
- Implement rate limiting per tenant/user.
- Use token counting and request shaping.

## 19) Troubleshooting cheat sheet

- **AccessDenied on invocation** → missing `bedrock:InvokeModel` / model access not granted.
- **Validation errors** → wrong request sche
