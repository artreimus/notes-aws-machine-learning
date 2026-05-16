---
title: "AWS Organizations"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
status: "reviewed"
domain:
  - "4.2"
  - "4.3"
service:
  - "AWS Organizations"
tags:
  - "aws"
  - "mla-c01"
  - "domain-4"
  - "governance"
  - "multi-account"
aliases:
  - "AWS Organizations"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# AWS Organizations

## Knowledge Relevance

Multi-account governance and consolidated billing service for AWS environments.

## When To Use

- Use to centrally manage accounts, organizational units, policies, and consolidated billing.
- Use service control policies for guardrails across accounts/OUs.
- Use with CloudTrail, Config, Macie, and Cost Explorer for central governance.

## Core Concepts

- Accounts are natural boundaries for permissions, security, costs, and workloads.
- OUs group accounts.
- SCPs restrict maximum available permissions.
- Consolidated billing gives one bill across accounts.

## AWS Services And Features

- AWS Organizations
- Service Control Policies
- AWS Cost Explorer
- AWS Config
- AWS CloudTrail

## Implementation Patterns

- Security OU + workload OUs -> SCP guardrails -> central logging/security/cost accounts.
- Consolidated billing -> Cost Explorer views grouped by linked accounts and tags.

## Tradeoffs And Pitfalls

- SCPs do not grant permissions; they set guardrails.
- Management account should be protected and used sparingly.
- Separate workload accounts reduce blast radius.

## Decision Triggers

- Multi-account governance, OUs, SCPs, and consolidated billing point to Organizations.
- Approved product catalog points to Service Catalog.

## Related Notes

- [[aws-config]]
- [[service-catalog]]
- [[aws-cost-management-for-ml]]


## Sources

- https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
