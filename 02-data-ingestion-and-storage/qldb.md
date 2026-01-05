# Amazon QLDB (Quantum Ledger Database)

## 1. Overview

Amazon QLDB is a managed **ledger database** that maintains an **immutable** record of changes. It’s designed for use cases that require a verifiable history of updates.

**Where it fits in ML workflows**

- Maintain an auditable history of “ground truth” business events (e.g., decisions, approvals, overrides) that might be used to create labels or evaluate model outcomes.
- Support compliance/audit requirements for data lineage and change tracking around ML-relevant records.

---

## 2. Core Concepts

- A ledger stores data with a **journal** of changes.
- The key idea is **append-only history** with the ability to verify that records weren’t altered.

---

## 3. ML-Relevant Patterns

- Use QLDB as the authoritative audit trail for decision events, then extract curated datasets to S3/warehouse for training and analysis.
- Keep online serving features in DynamoDB/feature store; use QLDB for compliance-grade history when required.

---

## 4. When to Choose QLDB vs DynamoDB

- Choose **QLDB** when immutability and verifiable history are requirements.
- Choose **DynamoDB** when you need flexible, low-latency key-based access and don’t require ledger semantics (Streams can provide change capture, but not ledger verification).

