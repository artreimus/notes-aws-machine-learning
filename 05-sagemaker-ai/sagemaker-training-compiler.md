---
title: "SageMaker Training Compiler"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "legacy"
domain:
  - "2.2"
service:
  - "Amazon SageMaker AI"
tags:
  - "aws"
  - "mla-c01"
  - "sagemaker"
  - "legacy"
aliases:
  - "SageMaker Training Compiler"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# SageMaker Training Compiler

## Knowledge Relevance

Legacy SageMaker optimization feature. Keep for historical context and exam caveat recognition, but do not emphasize as a current optimization path.

## When To Use

- Use only for understanding old training optimization references.
- Prefer current distributed training, compiler/framework-native optimization, instance selection, and training-data/input-mode optimization for new designs.

## Core Concepts

- Training Compiler optimized supported deep learning workloads in SageMaker DLCs.
- AWS states there are no new releases or versions and existing DLCs no longer receive patches or updates for this feature.
- It is incompatible with some distributed training paths and should not be the first current answer.

## AWS Services And Features

- Amazon SageMaker AI
- SageMaker Distributed Data Parallel
- SageMaker Model Parallelism

## Implementation Patterns

- Historical: estimator with compiler config -> optimized training job on supported GPU DLC.
- Current: choose suitable instances, distributed libraries, mixed precision, checkpointing, and data/input optimization.

## Tradeoffs And Pitfalls

- Legacy/no-new-release status is the key exam caveat.
- Do not combine with SMDDP as a current best-practice answer.
- Security patch status matters for old DLCs.

## Decision Triggers

- Training Compiler wording should trigger legacy caveat.
- Large model scaling points to distributed training/model parallelism instead.

## Related Notes

- [[training-compiler]]
- [[sagemaker-training-techniques]]
- [[sagemaker-model-parallelism]]


## Sources

- https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler-enable.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
