---
title: "OpenSearch vector search: layers and tradeoffs"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
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
  - "OpenSearch vector search: layers and tradeoffs"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# OpenSearch vector search: layers and tradeoffs

Below is a “stack view” of OpenSearch vector search. Each row is a **choice at a different layer** (you can mix-and-match: e.g., **faiss + hnsw + on_disk**).

> Ratings (Low/Med/High) are **relative**. Real numbers depend on: vectors count (N), dimension (d), filters/selectivity, shard count, hardware (RAM/SSD), and tuning parameters.

## Layer table

| Layer                            | Option                                                 |                             RAM / memory needs |                    Speed (latency) |                               Recall | Advantages                                                                  | Cons / gotchas                                                             | Best when                                                 |
| -------------------------------- | ------------------------------------------------------ | ---------------------------------------------: | ---------------------------------: | -----------------------------------: | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Search mode**                  | **Approximate k-NN (ANN)**                             | Med → High (depends on index + representation) |                  **Fast** at scale |                       High (tunable) | Scales to large N; controllable quality/latency tradeoff                    | Requires tuning; approximate by design                                     | Default for RAG at medium/large scale                     |
| **Search mode**                  | **Exact k-NN (brute force)**                           |         Low extra index RAM (no ANN structure) |                **Slow** as N grows |                          **Perfect** | True nearest neighbors; good for QA/validation; ok if candidate set is tiny | Latency grows linearly with candidates; costly at scale                    | Small corpora, very selective filters, offline evaluation |
| **ANN engine (library)**         | **lucene**                                             | Med (index structures live in Lucene segments) |                               Fast |                                 High | Tight integration with Lucene; often strong with filtering/hybrid           | Typically fewer method families than Faiss; meaningfully version-dependent | Filter-heavy RAG + hybrid lexical/vector                  |
| **ANN engine (library)**         | **faiss**                                              |             Med → Low (with compression modes) |                               Fast |                       High (tunable) | Multiple method families; mature quantization/compression options           | More knobs/complexity; IVF needs training                                  | Big N; memory pressure; you want IVF/quantization         |
| **ANN engine (library)**         | **nmslib (legacy/deprecated)**                         |                                            Med |                               Fast |                                 High | Backward compatibility                                                      | Deprecated; avoid new deployments                                          | Only for maintaining older clusters                       |
| **Index method (ANN algorithm)** | **HNSW**                                               |                       **Higher** (graph edges) |                      **Very fast** |              **Very high** (tunable) | Great general-purpose ANN; strong recall/latency                            | RAM-heavy; build/merge cost can be noticeable                              | Most RAG systems where RAM is acceptable                  |
| **Index method (ANN algorithm)** | **IVF** (Faiss)                                        |                            **Lower** (usually) |                Fast (esp. large N) |                       High (tunable) | Partition-first search; good for very large corpora                         | Requires training; tuning `nlist/nprobe` matters a lot                     | Huge N where HNSW RAM is too expensive                    |
| **Vector representation**        | **Float vectors (FP32)**                               |                                    **Highest** |                           Baseline |                                 High | Best fidelity; simplest pipeline                                            | Expensive RAM/storage                                                      | When quality matters and you can afford memory            |
| **Vector representation**        | **Quantized / compressed floats** (e.g., FP16, PQ, SQ) |                                          Lower |            Often faster cache-wise |             Slightly lower (tunable) | Big memory savings; sometimes faster due to cache                           | Quality tradeoff; more tuning complexity                                   | Large N; tight RAM budgets                                |
| **Vector representation**        | **Binary vectors (Hamming)**                           |                                 **Much lower** |                               Fast |             Varies (model-dependent) | Very compact; fast bitwise distance                                         | Requires binary embeddings/hashing; different quality regime               | Cost-sensitive deployments with binary embeddings         |
| **Serving/storage mode**         | **In-memory vectors**                                  |                                           High |                 **Lowest latency** |                                 High | Best latency; fewer IO surprises                                            | RAM cost can dominate                                                      | Latency-sensitive RAG                                     |
| **Serving/storage mode**         | **Disk-based vector search** (`on_disk`)               |                                 **Lowest RAM** | **Higher latency** (SSD dependent) | High (often with oversample+rescore) | Enables much larger corpora on same RAM                                     | IO sensitivity; tail latency; tuning needed                                | When RAM is the bottleneck and SSD is good                |
| **Query-time strategy**          | **Oversample + rescore**                               |                     Med (temporary candidates) |                    Slightly higher |                               Higher | Improves recall/quality under compression/disk                              | More compute; higher latency                                               | Anytime you use quantization/disk and care about quality  |

---

## Practical “starter recipes”

### 1) Balanced default RAG (filters + decent RAM)

- **Engine:** lucene (or faiss)
- **Method:** HNSW
- **Vectors:** float (or mild quantization)
- **Tuning:** moderate `ef_search` (raise until recall is good enough)

### 2) Big corpus, RAM constrained

- **Engine:** faiss
- **Method:** IVF (or HNSW + compression)
- **Mode:** `on_disk` and/or binary quantization
- **Tuning:** `nprobe` (IVF) + oversample/rescore

### 3) Tiny filtered subsets (strong metadata filters)

- **Mode:** exact brute force after a filter
- **Note:** Only works if the filtered candidate pool stays small

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain1.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
