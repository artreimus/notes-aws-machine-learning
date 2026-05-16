---
title: "Amazon Lookout For Vision"
exam: "MLA-C01"
status: "legacy"
domain:
  - "2.1"
service:
  - "Amazon Lookout for Vision"
tags:
  - "aws"
  - "mla-c01"
  - "ai-services"
  - "legacy"
aliases:
  - "Amazon Lookout For Vision"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Lookout For Vision

## Exam Relevance

Lifecycle-aware note: AWS General Reference lists Amazon Lookout for Vision in full shutdown as of October 31, 2025.

## When To Use

- Use only to understand historical computer-vision quality inspection references.
- For current visual inspection, prefer SageMaker AI image models, Rekognition Custom Labels if appropriate, or custom CV pipelines.

## Core Concepts

- Was a managed computer vision service for visual defect/anomaly detection.
- No longer accessible after the shutdown date.

## AWS Services And Features

- Amazon Lookout for Vision
- Amazon SageMaker AI
- Amazon Rekognition

## Implementation Patterns

- Historical: images -> project/dataset -> model -> defect detection.
- Current: labeled image dataset -> SageMaker image classification/object detection or Rekognition Custom Labels pattern.

## Tradeoffs And Pitfalls

- Full shutdown means it is not a current service choice.
- Do not confuse with Amazon Rekognition, which remains in scope.

## Exam Triggers

- Visual defect detection with shutdown caveat points to Lookout for Vision only historically.
- Face/object/text/image analysis APIs point to Rekognition.

## Related Notes

- [[rekognition]]
- [[image-classification-tensorflow]]
- [[object-detection-tensorflow]]


## Sources

- https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html
- https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/API_DeleteDataset.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
