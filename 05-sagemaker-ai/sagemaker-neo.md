---
title: "SageMaker Neo"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "3.1"
service:
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "sagemaker"
  - "deployment"
aliases:
  - "SageMaker Neo"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SageMaker Neo

## Exam Relevance

SageMaker model optimization note. Neo remains optimization context, but Edge Manager references must be treated as historical.

## When To Use

- Use Neo when optimizing trained models for supported target hardware/runtime environments.
- Use for model compilation/optimization context before deployment to target devices or instances.
- Use Edge Manager only as historical/EOL context.

## Core Concepts

- Neo optimizes model artifacts for target deployment environments.
- SageMaker Edge Manager was no longer accessible after April 26, 2024.
- For edge deployment context, consider ONNX/runtime-specific optimization and AWS IoT Greengrass V2, noting Greengrass is out-of-scope for MLA-C01.

## AWS Services And Features

- SageMaker Neo
- Amazon SageMaker AI
- ONNX
- AWS IoT Greengrass V2 (out-of-scope edge context)

## Implementation Patterns

- Train model -> Neo compile/optimize for target -> deploy to target runtime.

## Tradeoffs And Pitfalls

- Do not describe Edge Manager as an active service.
- Edge deployment detail is supplemental for MLA-C01 unless tied to deployment optimization.
- Validate model framework/operator support before relying on compilation.

## Exam Triggers

- Compile model for target hardware points to Neo.
- Edge Manager wording points to EOL caveat.

## Related Notes

- [[sagemaker-on-the-edge]]
- [[deployment-mode-decision-guide]]


## Sources

- https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
