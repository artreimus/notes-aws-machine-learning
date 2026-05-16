---
title: "Amazon CloudFront"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "3.1"
  - "4.2"
service:
  - "Amazon CloudFront"
tags:
  - "aws"
  - "mla-c01"
  - "networking"
  - "cdn"
aliases:
  - "Amazon CloudFront"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon CloudFront

## Knowledge Relevance

CDN service for low-latency delivery and caching in ML and generative AI applications that serve static or dynamic web content.

## When To Use

- Use to cache static content or dynamic application content close to users.
- Use with S3, API Gateway, ALB, or custom origins.
- Use signed URLs/cookies and origin access controls for private content.

## Core Concepts

- Distributions define origins and cache behavior.
- Edge locations reduce latency and improve availability.
- Cache TTL and invalidations control freshness.

## AWS Services And Features

- Amazon CloudFront
- Amazon S3
- Amazon API Gateway
- AWS WAF

## Implementation Patterns

- Web app assets in S3 -> CloudFront distribution -> users.
- Gen AI UI -> CloudFront -> API Gateway backend -> Bedrock/SageMaker.

## Tradeoffs And Pitfalls

- CloudFront does not train, host, or evaluate models.
- Bad cache settings can serve stale generated or user-specific content.
- Private content requires signed access or origin controls.

## Decision Triggers

- Global edge caching and static/dynamic content acceleration point to CloudFront.
- Private network link to AWS points to Direct Connect or VPN.

## Related Notes

- [[api-gateway]]
- [[s3]]
- [[direct-connect]]


## Sources

- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
