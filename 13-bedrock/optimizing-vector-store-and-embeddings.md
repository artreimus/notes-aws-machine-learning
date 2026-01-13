## Optimizing vector store and embeddings (Amazon Bedrock Knowledge Bases context)

When RAG feels “meh”, it is usually not the LLM. It is the geometry you built underneath it: how you chunked, embedded, indexed, and searched. Bedrock Knowledge Bases is helpful because it standardizes the ingestion flow (chunk → embed → write to vector index) ([AWS Documentation][1]), but you still control the two biggest levers:

1. **Embedding choices** (model, dimensions, vector type, distance metric)
2. **Vector store and index configuration** (algorithm, parameters, filtering, compression, capacity)

Below is a practical, deep guide that matches how Bedrock KB actually behaves and what the underlying stores (OpenSearch, pgvector, S3 Vectors, etc.) can do.

---

## 1) Embeddings: choosing the right representation

### Pick an embedding model that matches your data and language

Bedrock Knowledge Bases supports several embedding model families (Titan, Cohere, plus multimodal options). The supported-models page also spells out vector types and supported dimensions. ([AWS Documentation][2])

Key takeaways from AWS’s supported list:

- **Titan Embeddings G1 (text)**: floating-point, **1536 dims** ([AWS Documentation][2])
- **Titan Text Embeddings V2**: floating-point **or binary**, **256 / 512 / 1024 dims** ([AWS Documentation][2])
- **Cohere Embed (English / Multilingual)**: floating-point or binary, **1024 dims** ([AWS Documentation][2])
- **Multimodal embeddings** exist too (Titan Multimodal Embeddings G1, Cohere multimodal). ([AWS Documentation][2])

Practical heuristics:

- If you are mostly **English**, Cohere English or Titan V2 are common picks.
- If you are truly **multilingual**, Cohere multilingual is the safer default.
- If your corpus includes images, diagrams, scanned PDFs, consider **multimodal embeddings** plus a parsing strategy that preserves meaning (tables, figures).

### Dimensions: bigger is not always better

Titan V2’s multiple dimensions (256/512/1024) are there because dimension is a trade between:

- **Quality / recall** (often improves with more dimensions)
- **Cost** (storage, memory, and search time grow with dimension)
- **Index feasibility** (more dims can force you into heavier infra sooner)

Bedrock KB setup guidance explicitly reminds you that your vector store’s dimension must match the embedding model, and Titan V2 can be 256 or 512 too. ([AWS Documentation][3])

Rule of thumb:

- Start with **512** (Titan V2) when you want a strong balance.
- Use **256** when you have massive scale and you can tolerate a bit less semantic nuance.
- Use **1024+** when accuracy is king and your infra budget agrees.

### Floating-point vs binary embeddings

Binary embeddings can slash memory and cost, but they are not universally supported by every vector store.

Two gotchas from AWS docs:

- Only **Amazon OpenSearch Serverless and Amazon OpenSearch Managed** clusters are called out as vector stores that support **storing binary vectors**. ([AWS Documentation][4])
- If you use **S3 Vectors** with Bedrock KB, it supports **floating-point vectors only**. ([AWS Documentation][5])

So the decision tree is basically:

- Want **binary embeddings** → you are strongly pushed toward **OpenSearch**.
- Want **cheapest durable storage** and semantic search is enough → **S3 Vectors**, but floating-point only. ([AWS Documentation][5])

### Distance metric: cosine vs Euclidean

Most modern text embeddings behave well with **cosine similarity**. Some systems also use Euclidean distance with normalized vectors. Bedrock KB setup docs recommend Euclidean for floating-point embeddings in at least one setup path. ([AWS Documentation][3])
In practice: pick the metric your store and embedding model documentation suggests, then validate with retrieval evaluation (more on that below).

---

## 2) Chunking, because embeddings do not rescue bad segmentation

Bedrock KB ingests by chunking first, then embedding those chunks and writing them to the vector index. ([AWS Documentation][1])

Optimization lens:

- Smaller chunks improve pinpoint recall but can lose context and increase vector count.
- Larger chunks preserve context but can dilute similarity and increase hallucination risk.

One very practical constraint: **S3 Vectors metadata limits** can bite you with hierarchical chunking.

- With S3 Vectors, you can attach up to **1 KB custom metadata** and **35 metadata keys per vector**. ([AWS Documentation][5])
- AWS warns that very high token counts with **hierarchical chunking** can exceed metadata size limits because parent-child relationships and hierarchical context are stored as non-filterable metadata. ([AWS Documentation][5])

So if you are using S3 Vectors, keep hierarchical chunking reasonable, or prefer simpler chunking strategies when your docs are massive.

---

## 3) Vector store choice: match the store to the workload

### Option A: Amazon S3 Vectors (Bedrock KB integration)

S3 Vectors is positioned as cost-effective, durable vector storage integrated into the Bedrock KB workflow, with warm latency as low as ~100 ms in AWS’s description. ([AWS Documentation][5])
Important limitations:

- **Semantic search only**, no hybrid search. ([AWS Documentation][5])
- **Metadata limits** (1 KB custom metadata, 35 keys). ([AWS Documentation][5])
- **Floating-point only**, no binary. ([AWS Documentation][5])

Use it when:

- Your corpus is huge and storage cost dominates.
- You can live without hybrid retrieval and ultra-low latency.
- You do not need complex metadata filtering.

### Option B: OpenSearch (Managed or Serverless)

OpenSearch is often the “enterprise default” when you need:

- Tight latency
- Higher query throughput
- More knobs (ANN algorithm parameters, quantization, hybrid patterns)
- Binary vector support (relevant if you use binary embeddings). ([AWS Documentation][4])

**ANN algorithm tuning (HNSW basics)**
AWS highlights the classic HNSW parameters:

- `m` controls graph connectivity
- `ef_construction` affects index build quality and time
- `ef_search` affects recall vs latency at query time ([Amazon Web Services, Inc.][6])

Practical tuning loop:

1. Fix embeddings and chunking.
2. Sweep `ef_search` first (this is the “recall knob” you can turn without reindexing in many setups).
3. Only then adjust `m` and `ef_construction` if you need a better index, accepting slower builds and bigger memory.
4. For index-level changes (like `m`, `ef_construction`, IVFFlat `lists`), plan to **recreate the index** to realize the optimization.

**Compression and cost controls**
OpenSearch is also pushing cost optimization via quantization and related techniques to reduce memory footprint for vector workloads. ([Amazon Web Services, Inc.][7])
And as of late 2025, AWS introduced an “auto-optimize” approach for OpenSearch vector databases to help pick index configurations without weeks of expert tuning. ([Amazon Web Services, Inc.][8])

### Option C: Aurora PostgreSQL with pgvector

Aurora + pgvector is attractive when you want:

- SQL + transactions + vector search in one system
- Familiar operational model (Postgres)
- Strong metadata filtering and joins

Index choice matters a lot:

- **IVFFlat**: inverted file, good when tuned well; build is usually cheaper than graph indexes.
- **HNSW**: graph-based ANN, often excellent recall/latency for read-heavy use cases.

AWS has a deep dive on IVFFlat and HNSW performance tradeoffs for pgvector indexing. ([Amazon Web Services, Inc.][9])
They also published strategies for maximizing HNSW indexing and searching performance on Aurora/RDS. ([Amazon Web Services, Inc.][10])
And AWS notes ongoing pgvector support improvements in Aurora releases. ([Amazon Web Services, Inc.][11])

Practical tuning heuristics for pgvector:

- If ingestion and reindex speed matters a lot, start with **IVFFlat**, tune `lists` and `probes`.
- If you are mostly read-heavy and want strong recall at low latency, **HNSW** is often the endgame, then tune `ef_search` for recall/latency tradeoff, and pick graph build settings that your ingestion pipeline can tolerate. ([Amazon Web Services, Inc.][9])

---

## 4) “Make it fast and accurate” workflow that actually works

### Step 1: Lock in evaluation before tuning

You cannot tune vector retrieval by vibes. Build a small evaluation set:

- 50 to 200 real user questions
- Expected “gold” sources (doc + section) or at least “must contain” facts
- Metrics: recall@k, MRR (mean reciprocal rank), latency p50/p95, and answer correctness

### Step 2: Tune in the right order

1. **Chunking**: fix gross failures first (chunks too big, too small, or broken by formatting).
2. **Embedding model + dimensions**: pick the best cost/quality point (Titan V2 512 is a common sweet spot).
3. **Search knobs**:

   - OpenSearch: sweep `ef_search`, then consider `m` and `ef_construction`. ([Amazon Web Services, Inc.][6])
   - pgvector: choose IVFFlat vs HNSW and tune the ANN knobs described in AWS’s pgvector posts. ([Amazon Web Services, Inc.][9])

4. **Metadata filtering**: only add complex filters once base recall is good, because filters can reduce recall if your metadata is incomplete or inconsistent.
5. **Reranking**: once retrieval recall is decent, reranking can significantly improve top-1 relevance without changing your vector store. (Bedrock KB supports reranking models depending on Region). ([AWS Documentation][2])

### Step 3: Watch for store-specific constraints

- S3 Vectors: watch metadata limits, and remember semantic-only search. ([AWS Documentation][5])
- Binary embeddings: ensure your chosen store supports them, with OpenSearch being the main one explicitly called out by Bedrock KB docs. ([AWS Documentation][4])

---

## 5) Bedrock KB setup details that affect optimization

### Your schema must support what Bedrock writes

When you bring your own vector store, Bedrock expects fields for:

- embeddings vector field
- text chunk field
- Bedrock-managed metadata fields ([AWS Documentation][4])

And the vector index dimension must match the embedding model dimension you chose. ([AWS Documentation][3])

### Keep stores isolated per KB when possible

AWS recommends creating a separate vector store per knowledge base for easier synchronization and management (not strictly “performance”, but it prevents operational foot-guns that turn into performance incidents). ([AWS Documentation][5])

---

## Cheat sheet: common optimization plays

- **Need cheaper storage at scale, can live with semantic-only** → S3 Vectors ([AWS Documentation][5])
- **Need ultra-low latency, lots of knobs, maybe binary vectors** → OpenSearch ([AWS Documentation][4])
- **Need SQL joins, transactional metadata, strong filtering** → Aurora pgvector ([Amazon Web Services, Inc.][9])
- **Overspending on vector storage** → reduce dims (Titan V2 512 or 256), consider compression/quantization where supported ([Amazon Web Services, Inc.][7])
- **Low recall** → increase chunk quality, increase `ef_search` (OpenSearch HNSW), consider reranking ([Amazon Web Services, Inc.][6])

If you keep the tuning order disciplined, you end up with a system that is faster, cheaper, and less hallucination-prone, which is a rare triple win in this universe.

[1]: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html?utm_source=chatgpt.com 'How content chunking works for knowledge bases'
[2]: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html 'Supported models and Regions for Amazon Bedrock knowledge bases - Amazon Bedrock'
[3]: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html 'Prerequisites for using a vector store you created for a knowledge base - Amazon Bedrock'
[4]: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html?utm_source=chatgpt.com 'Prerequisites for using a vector store you created for a ...'
[5]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-bedrock-kb.html 'Using S3 Vectors with Amazon Bedrock Knowledge Bases - Amazon Simple Storage Service'
[6]: https://aws.amazon.com/blogs/big-data/choose-the-k-nn-algorithm-for-your-billion-scale-use-case-with-opensearch/?utm_source=chatgpt.com 'Choose the k-NN algorithm for your billion-scale use case ...'
[7]: https://aws.amazon.com/blogs/big-data/cost-optimized-vector-database-introduction-to-amazon-opensearch-service-quantization-techniques/?utm_source=chatgpt.com 'Introduction to Amazon OpenSearch Service quantization ...'
[8]: https://aws.amazon.com/blogs/big-data/auto-optimize-your-amazon-opensearch-service-vector-database/?utm_source=chatgpt.com 'Auto-optimize your Amazon OpenSearch Service vector ...'
[9]: https://aws.amazon.com/blogs/database/optimize-generative-ai-applications-with-pgvector-indexing-a-deep-dive-into-ivfflat-and-hnsw-techniques/?utm_source=chatgpt.com 'Optimize generative AI applications with pgvector indexing'
[10]: https://aws.amazon.com/blogs/database/accelerate-hnsw-indexing-and-searching-with-pgvector-on-amazon-aurora-postgresql-compatible-edition-and-amazon-rds-for-postgresql/?utm_source=chatgpt.com 'Accelerate HNSW indexing and searching with pgvector on ...'
[11]: https://aws.amazon.com/about-aws/whats-new/2023/10/amazon-aurora-postgresql-pgvector-v0-5-0-hnsw-indexing/?utm_source=chatgpt.com 'Amazon Aurora PostgreSQL now supports pgvector v0.5.0 ...'
