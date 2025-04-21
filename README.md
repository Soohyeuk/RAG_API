# RAG API

A simple Retrieval-Augmented Generation (RAG) API built with FastAPI, using sentence-transformers for embeddings and FAISS for vector storage.

## Features

- Text ingestion with automatic embedding generation
- Semantic search using cosine similarity
- RESTful API endpoints
- Automatic loading of sample data on startup

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

