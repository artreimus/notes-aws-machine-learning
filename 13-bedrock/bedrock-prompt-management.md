---
title: "Amazon Bedrock Prompt Management"
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
  - "Amazon Bedrock Prompt Management"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Bedrock Prompt Management

## Overview
- Prompt Management is a Bedrock feature to create, test, version, and reuse prompts in a governed way.
- Prompts are stored in your AWS account with metadata, versions, and optional model configurations.
- Stored prompts can be invoked directly via Bedrock Runtime APIs and reused in Flows and Agents.

## Why It Matters
- Centralizes prompt engineering for teams and reduces prompt drift.
- Enables safe promotion using versions and comparisons.
- Improves reuse across apps, agents, and flows without duplicating prompt text.

## Core Concepts
- Prompt
  - A reusable prompt definition that can include system instructions, messages, tools, and variables.
- Variable
  - Template placeholders (for example, `{{customer_name}}`) that are filled at runtime.
- Prompt variant
  - Alternative prompt configurations for side-by-side comparison.
- Draft vs. version
  - Draft is editable; versions are immutable snapshots used in production.

## Key Capabilities
- Prompt builder in the console for composing prompts and configuring models.
- Compare variants across models or configurations.
- Create and manage versions with rollbacks.
- Store custom metadata (author, team, department).
- Optional prompt optimization to improve clarity or conciseness.
- KMS encryption options for stored prompts.

## How It Fits with Other Bedrock Features
- Amazon Bedrock Flows
  - Use prompt nodes that reference stored prompts.
- Agents for Amazon Bedrock
  - Reuse prompts for agent instructions and tool configuration.
- Runtime APIs
  - Invoke stored prompts via `Converse` or `InvokeModel` using the prompt identifier.

## Lifecycle
1. Create a prompt (draft) in the console or via `CreatePrompt`.
2. Test the prompt with variables and model settings.
3. Compare variants or refine the draft.
4. Create a version for production use.
5. Invoke the version from applications using runtime APIs.

## Operational Notes
- Versioning supports safe promotion and rollback.
- The prompt identifier is used in runtime invocations.
- Some runtime fields are fixed by the stored prompt definition, so runtime overrides can be restricted.

## Best Practices
- Keep prompts modular and reusable across flows and agents.
- Use variables instead of hard-coded values.
- Capture metadata for ownership and audit trails.
- Test against multiple models before publishing a version.

## Exam Tips
- Prompt Management is a Bedrock feature for prompt lifecycle management (create, test, version, reuse).
- Stored prompts can be invoked directly via Bedrock Runtime APIs.
- Prompts integrate with Flows and Agents and support versioning for safe deployment.

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-test.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-view.html
- https://aws.amazon.com/bedrock/prompt-management/
- https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga
- https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-bedrock-prompt-management-available/
