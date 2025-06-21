# Amazon EC2 Instance Types Overview

Amazon EC2 offers a wide variety of instance types optimized for different use cases. Here's a categorized summary of the main EC2 instance families, along with their capabilities in terms of **CPU**, **GPU**, and **Memory** (as of mid-2025):

---

### 🖥️ **General Purpose**

Balanced CPU, memory, and networking for a broad range of workloads.

| Instance Family                            | CPU            | Memory        | GPU | Use Case                           |
| ------------------------------------------ | -------------- | ------------- | --- | ---------------------------------- |
| **t4g**, **t3**, **t3a**                   | Up to 8 vCPUs  | Up to 32 GiB  | ❌  | Burstable workloads                |
| **m7g**, **m6g**, **m5**, **m5a**, **m5n** | Up to 96 vCPUs | Up to 384 GiB | ❌  | Web servers, app servers, dev/test |

---

### ⚙️ **Compute Optimized**

High-performance CPU for compute-intensive workloads.

| Instance Family                            | CPU            | Memory        | GPU | Use Case                          |
| ------------------------------------------ | -------------- | ------------- | --- | --------------------------------- |
| **c7g**, **c6g**, **c6i**, **c5**, **c5n** | Up to 96 vCPUs | Up to 192 GiB | ❌  | HPC, batch processing, ad serving |

---

### 💾 **Memory Optimized**

High memory-to-vCPU ratio for large in-memory data sets.

| Instance Family                     | CPU             | Memory          | GPU | Use Case                      |
| ----------------------------------- | --------------- | --------------- | --- | ----------------------------- |
| **r7g**, **r6g**, **r6i**, **r5**   | Up to 128 vCPUs | Up to 1,024 GiB | ❌  | In-memory DBs, SAP HANA       |
| **x2idn**, **x2iedn**               | Up to 128 vCPUs | Up to 4,096 GiB | ❌  | High-performance DBs          |
| **u-6tb1.metal**, **u-12tb1.metal** | 448 vCPUs       | 6–12 TiB        | ❌  | SAP HANA, scale-up memory DBs |

---

### 🧠 **Accelerated Computing**

GPU-powered instances for ML, AI, graphics, and HPC.

| Instance Family        | CPU             | Memory        | GPU                          | Use Case                     |
| ---------------------- | --------------- | ------------- | ---------------------------- | ---------------------------- |
| **p5**, **p4**, **p3** | Up to 96 vCPUs  | Up to 1.1 TiB | ✔️ (NVIDIA A100, V100, etc.) | ML/DL training               |
| **inf2**               | Up to 192 vCPUs | Up to 768 GiB | ✔️ (AWS Inferentia2)         | ML inference                 |
| **trn1**               | Up to 192 vCPUs | Up to 768 GiB | ✔️ (AWS Trainium)            | ML model training            |
| **g5**                 | Up to 96 vCPUs  | Up to 768 GiB | ✔️ (NVIDIA A10G)             | ML inference, graphics       |
| **f1**                 | Up to 64 vCPUs  | Up to 976 GiB | ✔️ (FPGA)                    | Custom hardware acceleration |

---

### 🗄️ **Storage Optimized**

Optimized for high-throughput and low-latency storage.

| Instance Family           | CPU             | Memory          | GPU | Use Case                     |
| ------------------------- | --------------- | --------------- | --- | ---------------------------- |
| **i4i**, **i3**, **i3en** | Up to 128 vCPUs | Up to 1,024 GiB | ❌  | NoSQL DBs, file storage      |
| **d3**, **d3en**          | Up to 48 vCPUs  | Up to 512 GiB   | ❌  | Data warehousing, HDFS       |
| **im4gn**, **is4gen**     | Up to 64 vCPUs  | Up to 512 GiB   | ❌  | NVMe SSD-optimized workloads |

---

### Notes:

- **Graviton-based instances** (e.g., m7g, c7g, r7g) use ARM CPUs and offer better price-performance in many workloads.
- **GPU-based instances** (p\*, g\*, inf2) are priced higher and designed for heavy ML, graphics, or scientific computing.
