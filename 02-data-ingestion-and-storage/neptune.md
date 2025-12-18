# Amazon Neptune

## 1. Overview

Amazon Neptune is a managed **graph database** designed for workloads where the primary value comes from **relationships**. It supports common graph query approaches (property graphs and RDF-style graphs).

**Where it fits in ML workflows**

- Build and query **knowledge graphs** for enrichment and feature creation.
- Relationship-driven use cases: **fraud ring detection**, **recommendations**, entity resolution, and influence/propagation analysis.

---

## 2. Core Concepts

- Graphs are modeled as **nodes/vertices** (entities) and **edges** (relationships).
- Queries often involve **multi-hop traversals** (friends-of-friends, shared devices, shared payment instruments), which are awkward/expensive to implement in key-value stores.

---

## 3. ML-Relevant Patterns

- Generate graph-based features (e.g., neighborhood counts, PageRank-style scores, shared-attribute connectivity) and store them in a feature store or DynamoDB for online serving.
- Use Neptune when **online relationship queries** are needed for real-time decisions; export snapshots/derived features to S3 for offline training.

---

## 4. When to Choose Neptune vs DynamoDB

- Choose **Neptune** when you need **graph traversals** and relationship-centric querying.
- Choose **DynamoDB** for low-latency key-based lookups; it can store adjacency lists, but it doesn’t provide graph query semantics.

