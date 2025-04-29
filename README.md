# RAG API

A simple Retrieval-Augmented Generation (RAG) API built with FastAPI, using sentence-transformers for embeddings and FAISS for vector storage.

## Features

- Text ingestion with automatic embedding generation
- Semantic search using cosine similarity
- RESTful API endpoints
- Automatic loading of sample data on startup
- Batch processing for efficient text ingestion

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

Response:
```json
{
    "message": "Text successfully ingested",
    "status_code": 200,
    "success": true
}
```

### GET /query?=`<text>`&k=`<k>`
Query the vector store for similar texts.

Parameters:
- `text`: The query text (required)
- `k`: Number of results to return (default: 3)

Response:
```json
[
    {
        "text": "Retrieved text content",
        "similarity": 0.95
    }
]
```

## Running Tests

Run the test suite:
```bash
pytest tests/
```

The test suite includes:

### Unit Tests
- VectorStore initialization and configuration
- Text ingestion (single and batch)
- Search functionality
- Edge cases and error handling

-> Only unit test was created, as the scale of the product is not grand. 


httpi POST http://localhost:8000/ingest -d '{"text": "apple is a fruit that is sweet and sour. it tastes really good"}'
httpi GET "http://localhost:8000/query?text=what%is%apple?"                        

