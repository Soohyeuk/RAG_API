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

## Running the API

Start the server:
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### POST /ingest
Ingest new text into the vector store.

Request body:
```json
{
    "text": "Your text here"
}
```

### GET /query
Query the vector store for similar texts.

Parameters:
- `text`: The query text
- `k`: Number of results to return (default: 3)

## Running Tests

Run the test suite:
```bash
pytest
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 