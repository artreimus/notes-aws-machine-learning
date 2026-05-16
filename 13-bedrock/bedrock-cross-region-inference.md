---
title: "Amazon Bedrock Cross-Region Inference"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
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
  - "Amazon Bedrock Cross-Region Inference"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Bedrock Cross-Region Inference

## Overview
- Cross-Region inference routes Bedrock requests across multiple AWS Regions to handle traffic bursts and increase throughput.
- It is enabled by using **inference profiles** instead of a single regional model ARN.
- The feature is designed for **on-demand** inference (not Provisioned Throughput).

## How It Works
- You call Bedrock APIs with an inference profile ID/ARN as the `modelId`.
- Bedrock routes each request to the optimal Region in the profile, prioritizing the source Region when possible.
- The routing logic is managed by Bedrock; clients do not implement their own load balancing.

## Types of Cross-Region Inference Profiles
- Geographic
  - Routes within a chosen geography (for example, US or EU).
  - Best for data residency requirements.
- Global
  - Routes across all supported commercial Regions.
  - Maximizes throughput and availability (no geographic restriction).

## Benefits
- Higher throughput (up to ~2x in-region quota for supported on-demand use cases).
- Improved resilience during traffic spikes.
- No extra routing or data transfer charge; pricing is based on the source Region.

## Limitations and Considerations
- Not supported with Provisioned Throughput.
- You cannot pin a request to a specific Region; routing is automatic.
- Only supported for models and Regions listed in the inference profile support table.
- Data is transmitted on the AWS backbone and encrypted in transit.

## Where You Can Use It
- Bedrock runtime APIs that accept `modelId` (for example, `InvokeModel`, `Converse`).
- Other Bedrock features that accept a model identifier (for example, evaluation jobs, flows, prompt management) can also use inference profiles.

## Best Practices
- Use geographic profiles if you must keep data within a region group.
- Monitor throughput and error rates to confirm routing benefits.
- If you need strict regional processing, use a regional model directly.

## Exam Tips
- Cross-Region inference uses inference profiles and is for on-demand inference only.
- Geographic profiles keep traffic within a chosen geography; Global profiles can route anywhere.
- Pricing is based on the source Region with no added routing cost.

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-use.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-view.html
- https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-bedrock-cross-region-inference/
- https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock
