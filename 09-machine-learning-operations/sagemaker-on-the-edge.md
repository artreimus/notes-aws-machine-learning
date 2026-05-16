---
title: "SageMaker On The Edge"
exam: "MLA-C01"
status: "supplemental"
domain:
  - "3.1"
service:
  - "Amazon SageMaker AI"
  - "AWS IoT Greengrass"
tags:
  - "aws"
  - "mla-c01"
  - "supplemental"
  - "edge"
aliases:
  - "SageMaker On The Edge"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SageMaker On The Edge

## Exam Relevance

Supplemental edge-deployment context. Use for historical/adjacent knowledge only; AWS IoT Greengrass is out-of-scope for MLA-C01 and SageMaker Edge Manager is EOL.

## When To Use

- Use this note only when reviewing edge deployment tradeoffs.
- For current MLA-C01 focus, connect edge optimization back to SageMaker Neo/model optimization and deployment constraints.

## Core Concepts

- SageMaker Edge Manager is EOL and no longer accessible.
- AWS IoT Greengrass V2 can be a replacement context for edge application management but is out-of-scope for MLA-C01.
- ONNX and runtime-specific optimization matter for edge portability.

## AWS Services And Features

- SageMaker Neo
- AWS IoT Greengrass V2
- ONNX

## Implementation Patterns

- Historical Edge Manager flow -> replace with device/runtime-specific deployment pattern and Greengrass V2 where appropriate.

## Tradeoffs And Pitfalls

- Do not spend primary exam time on Greengrass.
- Do not describe Edge Manager as active.
- Edge constraints include memory, CPU/GPU, connectivity, update, and security model.

## Exam Triggers

- Edge Manager term should trigger EOL caveat.
- Greengrass term should trigger out-of-scope caveat.

## Related Notes

- [[sagemaker-neo]]
- [[greengrass]]
- [[out-of-scope-services]]


## Sources

- https://docs.aws.amazon.com/sagemaker/latest/dg/edge-eol.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-out-of-scope-services.html
