---
title: "Amazon ElastiCache (Redis / Memcached)"
exam: "MLA-C01"
status: "draft"
domain:
  - "1.1"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-1"
  - "02_data_ingestion_and_storage"
aliases:
  - "Amazon ElastiCache (Redis / Memcached)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon ElastiCache (Redis / Memcached)

## 1. Overview

Amazon ElastiCache is a managed in-memory data store service that supports **Redis** and **Memcached**. It’s commonly used as a cache in front of databases to reduce latency and offload read traffic.

**Where it fits in ML workflows**

- Cache feature lookups (hot keys) to reduce load on DynamoDB/RDS/Aurora.
- Cache inference results for repeated queries (careful with freshness/TTL).
- Support real-time leaderboards/counters (Redis patterns), session state, rate limiting.

---

## 2. Redis vs Memcached

- **Redis**
  - Rich data structures (sets, sorted sets, hashes), persistence options, pub/sub patterns.
  - Often preferred for feature caching and real-time application patterns.
- **Memcached**
  - Simple key-value cache, generally used for straightforward caching with minimal features.

---

## 3. Scaling, HA, and Durability

- ElastiCache is primarily about **latency and throughput**, not durable storage.
- Use appropriate TTLs and design caches assuming eviction and failures can happen.

**If you need Redis-like durability:** consider purpose-built durable Redis options (separate from ElastiCache caching use cases).

---

## 4. ML Callouts

- Cache can dramatically reduce p99 latency for online inference, but requires careful invalidation (TTL/versioned keys).
- Don’t treat cache as a system of record; keep canonical data in DynamoDB/RDS/Aurora/S3.

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
