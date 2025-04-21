from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
import json
from typing import List
from schemas import TextInput, QueryResponse
from vector_store import VectorStore


vector_store = VectorStore()

@asynccontextmanager
async def lifespan(app: FastAPI):
    '''
    Initialize and process the data, before the app starts. 
    The data should look like a nested JSON object in a list. 

    Args:
        app: The FastAPI application instance
    Yields:
        None
    '''
    try:
        with open("sample_data.json", "r") as f:
            sample_data = json.load(f)
        
        sample_texts = [item["text"] for item in sample_data]
        vector_store.add(sample_texts)  
    except Exception as e:
        print(f"Error loading initial data: {e}")
    
    yield #processes everything above, before the app starts

app = FastAPI(title="RAG API", lifespan=lifespan)

@app.post("/ingest")
async def ingest_text(text_input: TextInput):
    """
    Ingest new text and store it in the vector store.
    
    Args:
        text_input: The text to ingest
    Returns:
        A message indicating the text was successfully ingested
    """
    try:
        vector_store.add(text_input.text)
        return {
            "success": True,
            "message": "Text successfully ingested",
            "status_code": 200
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": str(e),
                "status_code": 500
            }
        )

@app.get("/query")
async def query_text(text: str, k: int = 3) -> List[QueryResponse]:
    """
    Query the vector store for similar texts.

    Args:
        text: The text to query
        k: The number of results to return
    Returns:
        A list of QueryResponse objects
    """
    try:
        results = vector_store.search(text, k)
        return [QueryResponse(text=text, similarity=similarity) for text, similarity in results]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": str(e),
                "status_code": 500
            }
        )
