# RAG Demo

A hands-on repository for learning and experimenting with Retrieval-Augmented Generation (RAG) pipelines using Python and LangChain.

## Overview

This project demonstrates how to:

- load documents from a local folder,
- split them into smaller chunks,
- create embeddings,
- store them in a vector database,
- retrieve relevant context for a query,
- generate answers from retrieved documents.

## Project structure

- [docs](docs) — sample documents used for retrieval
- [db](db) — local ChromaDB storage
- [dbv1](dbv1) and [dbv2](dbv2) — additional database snapshots
- [1_ingestion_pipeline.py](1_ingestion_pipeline.py) — loads documents and builds the vector store
- [2_retrieval_pipeline.py](2_retrieval_pipeline.py) — basic retrieval example
- [3_answer_generation.py](3_answer_generation.py) — generates answers from retrieved context
- [4_history_aware_generation.py](4_history_aware_generation.py) — conversational/history-aware generation
- [5_recursive_character_text_spliiter.py](5_recursive_character_text_spliiter.py) — chunking examples
- [6_semantic_chunking.py](6_semantic_chunking.py) — semantic chunking demo
- [7_agentic_chunking.py](7_agentic_chunking.py) — prompt-based chunking experiment
- [9_retrieval_methods.py](9_retrieval_methods.py) — retrieval strategy comparisons
- [10_multi_query_retrieval.py](10_multi_query_retrieval.py) — multi-query retrieval flow
- [11_reciprocal_rank_fusion.py](11_reciprocal_rank_fusion.py) — reciprocal rank fusion example
- [12_hybrid_search.ipynb](12_hybrid_search.ipynb) — hybrid search notebook
- [13_reranker.ipynb](13_reranker.ipynb) — reranking notebook

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure your model endpoint is available.

   Some scripts use an OpenAI-compatible API setup (for example, with LM Studio). If needed, update the model URL and API key values in the scripts.

## Basic workflow

1. Put your `.txt` documents in [docs](docs)
2. Run the ingestion pipeline:

   ```bash
   python 1_ingestion_pipeline.py
   ```

3. Try retrieval and answer generation:

   ```bash
   python 2_retrieval_pipeline.py
   python 3_answer_generation.py
   ```

## Notes

- This project is mainly for learning and experimentation.
- The scripts are intentionally simple and easy to follow.
- You can explore different chunking and retrieval approaches using the numbered scripts.
