---
title: "Amazon Bedrock Knowledge Bases (deep dive notes)"
exam: "MLA-C01"
status: "draft"
domain:
  - "2.1"
  - "3.1"
  - "4.1"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-2"
  - "domain-3"
  - "domain-4"
  - "13_bedrock"
aliases:
  - "Amazon Bedrock Knowledge Bases (deep dive notes)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Bedrock Knowledge Bases (deep dive notes)

Amazon Bedrock Knowledge Bases is AWS’s **managed Retrieval-Augmented Generation (RAG)** capability. You connect your private data (unstructured docs, multimodal files, or structured tables), Bedrock handles ingestion + indexing, and at runtime it retrieves relevant information and (optionally) generates a grounded answer with **citations/source attribution**.

It’s easiest to think of Knowledge Bases as two related products under one name:

1. **Knowledge base with a vector store (unstructured / multimodal RAG)**

- Your content is parsed → chunked → embedded → stored in a vector index.
- Queries are embedded and used to retrieve semantically similar chunks.

2. **Knowledge base with a structured data store (NL→SQL retrieval)**

- No embeddings required.
- Bedrock translates natural-language questions into SQL, executes via a query engine, and returns results (optionally summarized).

---

## 1) Core mental model: the managed RAG pipeline

### A. Ingestion & indexing (offline / sync job)

For **vector-store** knowledge bases, ingestion looks like:

1. **Read data** from a connected data source (S3/Confluence/SharePoint/Salesforce/Web crawler/custom connector) or via programmatic ingestion.
2. **Parse** documents into extractable content (text + optionally tables/images/figures).
3. **Chunk** the parsed content.
4. **Embed** each chunk using the configured embedding model.
5. **Write** embeddings + chunk text + metadata into the configured vector store.

### B. Retrieval & generation (runtime)

For **vector-store** knowledge bases:

1. Convert the **user query → embedding vector**.
2. Query the vector index for **top-K similar chunks**.
3. Optionally **rerank** the candidate chunks.
4. Return chunks directly (**Retrieve**) or **augment a prompt and generate** a response (**RetrieveAndGenerate**) with citations.

For **structured** knowledge bases:

1. Convert user query → **SQL** (Bedrock-managed NL2SQL).
2. Execute SQL via the configured query engine.
3. Return query results (**Retrieve**) or summarize/answer (**RetrieveAndGenerate**).

---

## 2) Building blocks (what you configure)

### A. Knowledge base configuration types

- **Vector knowledge base**: pick an embedding model + vector store.
- **SQL knowledge base**: pick a query engine + structured data store configuration.

### B. Data source connectors (unstructured)

Knowledge Bases support connecting to:

- **Amazon S3** (most flexible; also required for multimodal support)
- **Confluence**
- **Microsoft SharePoint**
- **Salesforce**
- **Web crawler**
- **Custom data source** (your own connector)

**Multimodal (images/audio/video) ingestion is only supported with S3 and custom data sources.** Other connector types skip multimodal files during ingestion.

### C. Vector store options (unstructured)

You can **quick-create** some stores from the Bedrock console, or “bring your own” supported store.

Common options include:

- **Amazon OpenSearch Serverless (vector search)**
- **Amazon Aurora PostgreSQL Serverless (pgvector-backed)**
- **Amazon Neptune Analytics** (graph + vectors; enables GraphRAG-style linking)
- **Amazon S3 Vectors** (S3-native vector buckets)
- Additional supported third-party vector stores may be available depending on region and feature support.

**Binary vectors**: If you want lower-cost, lower-precision **binary** vector storage, OpenSearch Serverless/Managed are the primary vector stores that support binary vectors.

### D. Embeddings model

A vector knowledge base uses an embedding model to convert content and queries to vectors. AWS supports multiple embedding models (e.g., Titan text embeddings, Cohere embeds; availability varies by region).

Key tuning knobs:

- **Embeddings type**: float32 vs binary (if supported).
- **Vector dimension**: higher can improve retrieval accuracy but increases storage/cost/latency.

### E. Parsing configuration

Parsing is the “extract meaning from raw files” step.

Options:

- **Default parser (free)**: extracts text only (good for plain text docs; not great for visually rich PDFs).
- **Bedrock Data Automation (BDA) parser**: purpose-built multimodal extraction (tables/figures/images), priced per page/image.
- **Foundation model parser**: uses an FM to parse multimodal content; priced by tokens; can be customized with a parsing prompt.

Important operational constraints:

- If you choose **BDA or FM parsing**, that parsing method is used for **all PDFs** in the data source (even text-only PDFs), and you’ll incur the related costs.
- You **can’t change** parsing strategy after a data source is connected. To change it, add a new data source (and for multimodal storage destination changes, you may need a new knowledge base).

### F. Chunking configuration

Chunking determines how documents are split before embedding.

Default behavior (if you don’t specify settings):

- Bedrock splits into ~**300 token** chunks while preserving sentence boundaries.

Supported chunking strategies:

- **NONE**: treat each document as a single chunk.
- **FIXED_SIZE**: uniform chunks with token overlap.

  - Parameters: `maxTokens`, `overlapPercentage`.

- **HIERARCHICAL**: two-level chunking (large parent chunks + smaller child chunks).

  - Parameters: `levelConfigurations` (token sizes per level), `overlapTokens`.

- **SEMANTIC**: chunk boundaries based on meaning (semantic breakpoints).

  - Parameters: `breakpointPercentileThreshold`, `bufferSize`, `maxTokens`.

Like parsing, you **can’t change** chunking strategy for an existing data source after it’s connected.

### G. Optional: custom transformation Lambda (advanced ingestion)

You can insert a Lambda function into ingestion to:

- implement a **custom chunking** algorithm,
- attach **chunk-level metadata**,
- do post-processing/cleanup normalization.

This is how you escape “one-size-fits-all chunking” when your documents are weird (and documents are always weird).

---

## 3) Data preparation & limits (practical constraints)

### Supported document formats (typical unstructured ingestion)

Common supported formats include:

- `.txt`, `.md`, `.html`
- `.doc/.docx`
- `.xls/.xlsx`
- `.csv`
- `.pdf`

Typical size constraints:

- For many text/office/PDF docs, a common limit is **50 MB per file**.
- Multimodal knowledge bases have different limits for large audio/video and BDA-based ingestion (files-per-job and file-size limits can be much higher, but vary by feature).

### Metadata support

Metadata can dramatically improve retrieval quality by letting you filter the candidate set before semantic search.

Patterns:

- **Per-document metadata**: provide a separate metadata JSON file associated with a source document.
- **CSV metadata mapping**: for CSV ingestion, you can supply a `fileName.csv.metadata.json` that tells the knowledge base which columns are content vs metadata.

Practical notes:

- Metadata has **quotas** (number of attributes, key/value size, etc.). If your ingestion job reports “invalid metadata attributes,” it usually means you hit these constraints.

---

## 4) Querying a knowledge base

### A. Retrieve (RAG retrieval only)

Use **Retrieve** when you want:

- “Give me the best chunks”
- to build your own prompt orchestration
- to apply your own post-processing or cross-encoder reranking externally

### B. RetrieveAndGenerate (managed RAG)

Use **RetrieveAndGenerate** when you want:

- retrieval + answer generation in one call
- built-in citations/source attribution
- a simpler app pipeline

### C. Reranking

Knowledge Bases use a built-in ranker by default, and you can optionally select a **reranking model** to improve relevance ordering (especially when the initial vector search brings back near-misses).

### D. Guardrails (important nuance)

Bedrock Guardrails apply to:

- the **user input**, and
- the **generated response**

They generally do **not** apply to the retrieved references themselves. So if your corpus contains unsafe text, you need to govern and sanitize your data sources, not just rely on guardrails.

---

## 5) Operations: keeping data fresh

### A. Sync / ingestion jobs

Knowledge Bases provide ingestion job operations to keep your data source and embeddings synchronized.

Typical workflow:

- Update documents in your data source (e.g., S3 objects or updated Confluence pages)
- Start a **sync/ingestion** job
- Bedrock updates the vector index entries so retrieval reflects the latest content

### B. Programmatic ingestion

For streaming data or unsupported sources, you can **directly index documents** into the knowledge base via an API operation designed for document ingestion (useful for event-driven pipelines).

### C. Deletion policies

When deleting a knowledge base or data source, you typically choose a **data deletion policy**:

- **DELETE**: remove vectors/entries from the vector store (default behavior in many flows)
- **RETAIN**: keep the vectors in the store

RETAIN can be useful for recovery/forensics, but be careful: it also means data may linger and incur storage cost.

---

## 6) Structured Knowledge Bases (NL→SQL) deep dive

### What it solves

Many enterprise answers live in tables: orders, invoices, inventories, metrics. Traditional RAG requires “textifying” structured data and hoping embeddings do the right thing.

Structured Knowledge Bases offer a managed **natural-language-to-SQL (NL2SQL)** module so you can query structured data directly.

### Key components

When creating a structured knowledge base, you specify:

- **Query engine configuration** (compute that runs SQL)

  - Amazon Redshift is the primary query engine option in the core flow.
  - Authentication can use an IAM role, DB user, or Secrets Manager secret.

- **Storage configuration** (where the data lives)

  - Supported stores include Amazon Redshift and AWS Glue Data Catalog (Lake Formation). Some announcements also mention Amazon SageMaker Lakehouse support.

### Optional query configurations (accuracy boosters)

These help the SQL generator do a better job:

- **Maximum query time** (timeout)
- **Descriptions** for tables/columns (adds semantic context)
- **Inclusions/Exclusions** of tables/columns

  - Note: this is for accuracy, not security/guardrails.

- **Curated queries** (few-shot examples: NLQ → SQL)

### APIs specific to structured

- **GenerateQuery**: produce SQL from a natural-language question (without executing). Useful if you want to:

  - inspect the SQL,
  - enforce additional checks,
  - run it in your own query workflow.

### Syncing structured schemas

Structured KBs require schema metadata. When your schema changes (new tables/columns/relationships), you typically need to **sync** so the knowledge base can generate valid SQL.

---

## 7) Security & governance (things that bite teams later)

### IAM roles

A Knowledge Base usually needs a service role that allows it to:

- read from the data source(s)
- write/query the vector store (or query engine)
- write extracted multimodal artifacts to an S3 destination (if using multimodal parsing)

### Encryption

Common encryption surfaces:

- Vector store encryption (where supported)
- S3 source and supplemental storage encryption
- Optional KMS key configuration for transient ingestion data

### Data boundaries

- For connectors like Confluence/SharePoint/Salesforce, permissions and scoping are critical.
- Apply least-privilege and keep data sources narrow; “just index everything” is how you accidentally build a compliance incident.

---

## 8) Choosing chunking + parsing in the real world

### When default parsing + default chunking is enough

- mostly plain text (Markdown/HTML/text)
- PDFs that are truly text-first and cleanly extracted
- you’re prototyping and need fast results

### When to use BDA or FM parsing

- visually rich PDFs (tables, charts, screenshots)
- you need the KB to return images/figures as part of citations
- layout matters (e.g., manuals, scanned docs)

### Chunking heuristics (practical)

- **FIXED_SIZE**: strong baseline; use overlap for long explanations and “definition then usage” patterns.
- **HIERARCHICAL**: great for manuals/specs where you want both broad context and precise details.
- **SEMANTIC**: helps when topics shift within a document and you don’t want “token boundaries” to cut meaning in half.
- **NONE**: only use when docs are already short and self-contained.

---

## 9) Common failure modes (and how to debug)

- **Retrieval feels random** → wrong chunking (too big/too small), weak embeddings choice, or no metadata filters.
- **Good chunks, bad answer** → generation prompt/model choice issue; try Retrieve first to validate retrieval.
- **PDF answers miss tables/figures** → you’re using the default parser; switch to BDA or FM parsing.
- **Ingestion errors** → file size/format limits, invalid metadata attributes, connector permissions.
- **Structured KB returns wrong SQL** → add descriptions, curated queries, and tighten inclusions/exclusions.

---

## 10) Glossary (quick reference)

- **Parsing**: extracting usable content from raw files.
- **Chunking**: splitting parsed content into retrieval units.
- **Embedding**: mapping text/images/etc. to vectors for similarity search.
- **Vector store**: database/index optimized for nearest-neighbor search over vectors.
- **Retrieve**: return relevant chunks/results.
- **RetrieveAndGenerate**: retrieve + generate grounded response with citations.
- **Reranker**: model/step to reorder retrieved candidates by relevance.
- **Structured KB / NL2SQL**: translate natural language to SQL, execute, and optionally summarize.

## Sources

- https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
