---
title: "Amazon Kinesis Video Streams"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "1.1"
  - "2.1"
service:
  - "Amazon Kinesis Video Streams"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "media"
  - "streaming"
aliases:
  - "Amazon Kinesis Video Streams"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Kinesis Video Streams

## Exam Relevance

In-scope media streaming service for ingesting live video/audio/time-serialized data into AWS.

## When To Use

- Use for live video ingestion from devices into AWS.
- Use when applications need real-time or batch-oriented video analytics.
- Use with Rekognition Video or custom ML processing when video frames need analysis.

## Core Concepts

- Fully managed service for live video streams.
- Stores and encrypts media data for configured retention.
- Supports real-time frame access and historical processing.

## AWS Services And Features

- Amazon Kinesis Video Streams
- Amazon Rekognition
- Amazon S3
- Amazon EC2

## Implementation Patterns

- Camera/device -> Kinesis Video Stream -> consumer application -> Rekognition/custom model -> alert or storage.

## Tradeoffs And Pitfalls

- Kinesis Video Streams is source-agnostic but application logic still owns downstream analytics.
- Do not confuse with Kinesis Data Streams for generic records.

## Exam Triggers

- Live video stream ingestion points to Kinesis Video Streams.
- Generic event stream processing points to Kinesis Data Streams or Flink.

## Related Notes

- [[rekognition]]
- [[kinesis-data-streams]]
- [[managed-service-for-apache-flink]]


## Sources

- https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
