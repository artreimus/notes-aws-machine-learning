---
title: "AWS Direct Connect"
exam: "MLA-C01"
status: "reviewed"
domain:
  - "1.1"
  - "4.3"
service:
  - "AWS Direct Connect"
tags:
  - "aws"
  - "mla-c01"
  - "networking"
  - "security"
aliases:
  - "AWS Direct Connect"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Direct Connect

## Exam Relevance

Private network connectivity service for linking on-premises networks to AWS without relying only on the public internet path.

## When To Use

- Use for dedicated network connectivity from on-premises to AWS.
- Use when predictable bandwidth, private connectivity, or hybrid data transfer is required.
- Use public, private, or transit virtual interfaces depending on the target.

## Core Concepts

- Connections terminate at Direct Connect locations.
- Virtual interfaces provide access to public AWS services, VPCs, or transit gateways.
- BGP and VLAN tagging are required.

## AWS Services And Features

- AWS Direct Connect
- Amazon VPC
- Amazon S3
- Transit Gateway

## Implementation Patterns

- On-prem data center -> Direct Connect -> VPC/private VIF -> private ML data transfer.
- On-prem data source -> public VIF -> public AWS services such as S3 without internet provider path.

## Tradeoffs And Pitfalls

- Direct Connect is not encrypted by default at layer 3; add VPN/MACsec where needed.
- Setup lead time and partner/location availability matter.
- Use Site-to-Site VPN when dedicated connectivity is unnecessary.

## Exam Triggers

- Dedicated private physical connection points to Direct Connect.
- Encrypted tunnel over internet points to Site-to-Site VPN.

## Related Notes

- [[vpc]]
- [[private-ml-networking]]
- [[s3]]


## Sources

- https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
