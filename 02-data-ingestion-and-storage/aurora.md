# Amazon Aurora

## 1. Overview

Amazon Aurora is a managed relational database engine compatible with **MySQL** and **PostgreSQL**, designed for cloud scale. It emphasizes high throughput, fast failover, and decoupled storage/compute.

**Where it fits in ML workflows**

- High-throughput OLTP source for features and labels.
- Provides read replicas and (optionally) global deployments for distributed applications feeding ML systems.

---

## 2. Key Capabilities

- **Compatibility:** MySQL- and PostgreSQL-compatible endpoints and tooling.
- **Read scaling:** multiple read replicas for read-heavy workloads.
- **Fast failover / HA:** designed for rapid recovery and availability.
- **Serverless option (Aurora Serverless):** capacity scales automatically for variable workloads (useful for spiky dev/test or intermittent apps).
- **Global Database (Aurora Global Database):** low-latency global reads and cross-region disaster recovery.
- **Analytics integration:** commonly paired with S3/Glue/Redshift patterns to offload training and analytics workloads.

---

## 3. ML-Relevant Patterns

- Use **read replicas** for feature extraction queries to avoid impacting OLTP traffic.
- Periodically snapshot/replicate datasets to S3 for reproducible training sets.
- For global apps, use global database patterns to keep inference-enrichment data close to users while maintaining DR posture.

---

## 4. Security & Operations

- VPC isolation, security groups, encryption at rest/in transit.
- Automated backups and snapshots; monitoring via CloudWatch.
- Combine with Secrets Manager for credential rotation and application integration.

---

## 5. Aurora vs RDS (Decision Points)

- Choose **Aurora** when you want:
  - Higher throughput and faster failover characteristics for MySQL/PostgreSQL-compatible workloads.
  - Serverless or global database options.
- Choose **RDS** when you need:
  - A specific engine not provided by Aurora (e.g., Oracle/SQL Server).
  - A simpler managed setup for standard relational workloads.
