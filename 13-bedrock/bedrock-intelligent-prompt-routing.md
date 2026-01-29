# Amazon Bedrock Intelligent Prompt Routing

## Overview
- Intelligent Prompt Routing (IPR) provides a single serverless endpoint that routes requests between **models within the same family** to optimize response quality and cost.
- It predicts response quality per request and selects the best model given your routing criteria.
- It is generally available (GA) as of April 22, 2025.

## How It Works (High Level)
1. You choose a model family and configure a prompt router (or use a default router).
2. For each request, Bedrock analyzes the prompt and predicts response quality for each model.
3. The router selects the best model based on quality and cost criteria and forwards the request.
4. The response includes which model was used.

## Default vs. Configured Routers
- **Default routers**: preconfigured, ready to use for supported model families.
- **Configured routers**: you choose **two models from the same family** and set routing criteria (response quality difference) plus a fallback model.

## Routing Criteria and Fallback Model
- You set a **fallback model** as a baseline.
- **Response quality difference** determines when to switch away from the fallback model.
  - Example: if the higher‑quality model is only marginally better, route to the fallback for lower cost.

## Supported Model Families (Examples)
- Anthropic Claude (Haiku, Haiku 3.5, Sonnet 3.5 v1/v2)
- Meta Llama (3.1 8B/70B, 3.2 11B/90B, 3.3 70B)
- Amazon Nova (Nova Lite, Nova Pro)
- Always verify the current supported models/regions in the documentation.

## Considerations and Limitations
- Optimized for English prompts.
- Routing decisions are not customized to your app’s historical performance data.
- Best for general workloads; specialized domains may still need custom routing.

## When to Use
- Cost optimization with minimal quality loss for mixed complexity queries.
- A single endpoint that adapts between a smaller and larger model.
- Scenarios where you want to avoid building your own classifier/semantic router.

## Exam Tips
- Intelligent Prompt Routing routes **within a model family**.
- Default routers are prebuilt; configured routers let you pick two models and a routing threshold.
- It is a Bedrock feature, not a standalone service.

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-intelligent-prompt-routing-generally-available/
- https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-bedrock-intelligent-prompt-routing-preview/
- https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PromptRouterSummary.html
