---
title: "Chunking strategies for RAG (deep dive notes)"
scope: "AWS Machine Learning and AI"
certifications:
  - "MLA-C01"
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
  - "Chunking strategies for RAG (deep dive notes)"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Chunking strategies for RAG (deep dive notes)

Chunking is the step where you turn “documents” into **retrieval units**. Retrieval (vector / hybrid / keyword) typically happens at the chunk level, so chunking quietly controls everything downstream: relevance, citations, hallucination rate, latency, and cost.

## 1) The core tradeoff (the only law of chunking)

Chunking is always a balance between:

- **Recall (don’t miss relevant info)** → prefer _larger_ chunks, more overlap, parent context
- **Precision (don’t retrieve irrelevant junk)** → prefer _smaller_ chunks, cleaner boundaries

Every chunking strategy is just a different way of deciding _where boundaries go_ and _how big the pieces are_.

## 2) What chunking is optimizing for

### Retrieval quality goals

- **High precision @ top-k**: the first few retrieved chunks are actually useful.
- **Sufficient context**: a retrieved chunk contains enough surrounding text to be self-explanatory.
- **Grounding**: the answer can be traced back to the retrieved text (citations are meaningful).

### System goals

- **Low latency**: fewer tokens, fewer retrieved chunks, faster rerank.
- **Lower cost**: fewer embeddings stored + fewer prompt tokens.
- **Maintainability**: stable chunk IDs and minimal re-index churn when documents update.

## 3) The chunking design space (what you can control)

### A) Unit of splitting

- **Characters**: simplest, robust to weird text, but can cut semantics.
- **Tokens**: best aligned with model context limits and billing.
- **Sentences / paragraphs**: preserves meaning but depends on clean formatting.
- **Structure-aware**: headers, sections, tables, code blocks, Q&A pairs.

### B) Chunk size

Usually described as:

- **Target max tokens** (e.g., 200–1,000)
- Or “sentences per chunk”

### C) Overlap

Overlap helps avoid “boundary loss” (important info split across two chunks).

- Too little overlap → missing connecting context.
- Too much overlap → duplicates dominate retrieval and waste tokens.

### D) Boundary rules

How you choose a break:

- Hard limit (token cutoff)
- Soft limit (prefer sentence boundaries)
- Semantic boundary (topic shift)
- Structural boundary (header/table/code fences)

### E) Metadata strategy

Attach metadata to each chunk to support **filtering** and better ranking:

- source, doc_id, section heading path, page number
- timestamps, product version, access control tags
- entity tags (service names, customer names, ticket IDs)

Metadata often matters as much as chunk size.

## 4) Baseline strategies (good starting points)

### 4.1 No chunking (document-level retrieval)

**When it works:**

- docs are short and single-topic
- you have strong keyword search

**When it fails:**

- long documents with many topics
- high token cost and noisy context

### 4.2 Fixed-size token chunking (with overlap)

Split text into token windows of size `N` with overlap `O`.

**Pros:**

- predictable
- fast
- easy to implement

**Cons:**

- can cut definitions from examples
- mixes unrelated content in multi-topic docs

**Practical knobs:**

- `N` (maxTokens)
- `overlap` (either percent or tokens)

A common baseline in production because it’s stable and easy to tune.

### 4.3 Sentence/paragraph chunking

Group sentences/paragraphs until you reach a token budget.

**Pros:** preserves meaning better than raw fixed-size

**Cons:** depends on clean punctuation and formatting; PDFs can be messy

### 4.4 Recursive chunking (structure → smaller structure)

Start with large separators (e.g., headings / blank lines), and recursively split until within size.

**Pros:**

- good general-purpose approach for mixed content
- tends to preserve natural boundaries

**Cons:**

- still not “topic-aware” unless your separators reflect topics

This is often the best default for general text corpora.

## 5) Structure-aware chunking (best for docs with real structure)

### 5.1 Markdown / HTML header-based chunking

Split by header levels (H1/H2/H3), keep heading path as metadata.

**Why it works:**

- retrieval becomes “section retrieval”
- citations map cleanly to user-visible structure

### 5.2 PDF-aware chunking (layout-aware)

If you can extract layout (pages, blocks, tables), chunk by:

- page blocks
- table rows/sections
- figure captions + surrounding explanation

**Key warning:** PDF text extraction often destroys structure. If the parser output is garbage, chunking can’t save it.

### 5.3 Code-aware chunking

Chunk by:

- functions/classes/modules
- docstrings and comments together with code
- dependency edges (imports, call graph) as metadata

**Why it’s special:** semantic meaning in code often sits in function boundaries, not sentences.

### 5.4 Table-aware chunking

Tables are tricky: embeddings on raw CSV-like strings can be weak.

Approaches:

- chunk by logical table sections (header + grouped rows)
- add “row summaries” as auxiliary text fields
- store table metadata (column names, units, keys)

## 6) Semantic chunking (topic-aware boundaries)

Semantic chunking tries to split where the topic changes, not where tokens run out.

Typical algorithm:

1. sentence-split the document
2. embed sentences (or sliding windows of sentences)
3. compute similarity between adjacent sentences/windows
4. break where similarity drops (topic shift)
5. merge to respect max token size

**Pros:**

- better topical purity
- improves precision in multi-topic docs

**Cons:**

- more expensive at ingestion time
- tuning threshold is non-trivial
- can over-split if writing style changes frequently

Practical knobs you’ll see:

- breakpoint threshold/percentile
- buffer size (sentences to consider around a breakpoint)
- maxTokens cap

## 7) Hierarchical / parent–child chunking

Hierarchical chunking keeps **two (or more) granularities**:

- **Parent chunks**: larger sections
- **Child chunks**: smaller, more precise pieces derived from parents

Retrieval options:

- retrieve children for precision, but provide parent for context
- retrieve parents first, then drill down into children

**Pros:**

- strong for long technical docs
- keeps local detail + global context

**Cons:**

- more complex indexing and retrieval logic
- duplicates can increase if not handled carefully

A useful mental model:

- Children answer “where exactly?”
- Parents answer “what is this about?”

## 8) Late chunking (chunk after retrieval)

Late chunking delays fine-grained splitting until after you’ve identified relevant documents/sections.

Pattern:

1. index larger units (e.g., sections or pages)
2. retrieve top sections
3. chunk only those sections into smaller pieces
4. rerank / select final context for generation

**Pros:**

- preserves cross-references in long docs
- reduces total embedding/storage footprint
- focuses compute on “hot” documents

**Cons:**

- higher runtime complexity
- latency can increase if chunking happens online

Good for corpora with huge documents (manuals/specs) where only a small portion is queried at a time.

## 9) Contextual chunking (attach “why this chunk exists”)

A common failure mode: a chunk is technically relevant but ambiguous without nearby context (e.g., “It supports this in that case…”).

Contextual chunking adds lightweight context fields:

- prepend the heading path
- include a short parent summary
- include key entity mentions extracted from the section

You can do this as:

- extra metadata fields (preferred)
- a short “context header” added to the chunk text (works but increases tokens)

## 10) Chunk overlap: how to pick it

Overlap is a band-aid for boundary loss. Use it deliberately.

Heuristics:

- **High overlap** when meaning spans boundaries (legal text, policy docs, narratives)
- **Low overlap** when you have clean structure (header-based, function-based)

A practical range for fixed-size chunking is often **5–20% overlap**, but the best setting is data-dependent.

## 11) Chunk size: how to pick it

Chunk size depends on:

- the embedding model’s ability to represent long contexts
- how “atomic” the facts are in your corpus
- how much context the generator needs to answer confidently

Rules of thumb (start points, not laws):

- **FAQ / short policy**: 150–400 tokens
- **General docs / articles**: 300–800 tokens
- **Dense technical specs**: 500–1,200 tokens (often with hierarchy)

Bigger chunks improve recall but hurt precision and raise token cost. Smaller chunks do the opposite.

## 12) Retrieval-aware chunking (chunking is not independent)

Chunking should be chosen together with:

- **Retrieval method**: dense vs keyword vs hybrid
- **Reranking**: cross-encoder or LLM reranker can rescue imperfect chunking
- **Filtering**: metadata filters reduce noise drastically
- **Top-k**: more chunks retrieved can compensate for smaller chunks (cost tradeoff)

If you have a strong reranker, you can tolerate more aggressive (smaller) chunking.

## 13) Evaluation: how to tell if chunking is “good”

Chunking is measurable. Treat it like a model hyperparameter.

### Offline metrics

- **Recall@k** (does retrieved context contain the answer?)
- **Precision@k** (are retrieved chunks relevant?)
- **MRR / nDCG** (ranking quality)

### End-to-end metrics

- Answer correctness / faithfulness (human or LLM-judge)
- Citation quality (does the citation actually support the claim?)
- Latency and cost per query

### Quick ablation plan

Test at least:

1. fixed-size baseline
2. structure-aware (headers)
3. semantic or hierarchical

Then tune chunk size/overlap before trying exotic tricks.

## 14) A practical decision guide

- If your docs have strong structure (Markdown/HTML/manuals): **header-based + token cap** (optionally hierarchical).
- If your docs are messy or mixed: **recursive chunking** as default baseline.
- If your docs are long and multi-topic: **semantic or hierarchical**.
- If you have huge PDFs/specs and runtime can afford it: **late chunking**.
- If chunks feel “contextless”: add **contextual chunking** (heading path + parent summary).

## 15) Common pitfalls (and how to avoid them)

- **Chunking before cleaning**: garbage extraction produces garbage chunks.
- **No metadata**: you’re forcing embeddings to do all the work.
- **Too much overlap**: duplicates dominate retrieval and waste context.
- **One global strategy**: different doc types (FAQ vs specs vs code) often need different chunkers.
- **Ignoring updates**: stable chunk IDs and dedup strategy matter for incremental re-index.

## 16) Implementation patterns (tooling notes)

Common building blocks in RAG frameworks:

- Token-based splitters
- Recursive/semantic splitters
- Header splitters
- Parent–child node parsing

When you implement chunking yourself, store:

- `doc_id`, `chunk_id`
- `start_offset`, `end_offset` (or page number)
- `heading_path`
- `created_at`, `source_version`

This makes debugging and incremental updates dramatically easier.

## Sources

- https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
