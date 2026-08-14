# Phase 2

## Data

Phase 2 introduces a normalized PostgreSQL model for poems, authors, knowledge chunks and learning records. The public anthology source is imported by `backend/scripts/import_tang_poetry.py`.

The project deliberately separates **source text** from **educational enrichment**. Poem text can be imported from a public-domain / freely accessible corpus, while translations, teaching notes and interpretive annotations are treated as a separate provenance-aware layer.

## RAG

The first retriever is intentionally lexical and deterministic. It uses title/content/background/appreciation matching so the system can work without an embedding key. Production RAG can then add pgvector embeddings without changing the API contract.

Pipeline:

`question -> retrieve -> context assembly -> stage-aware prompt -> LLM -> citations`

## AI safety / trust

- No unsupported historical claims.
- No hidden fallback to fabricated model output.
- Retrieval-only fallback when no LLM key is configured.
- Every retrieved source is returned as a citation object.
