from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_ingest_text():
    response = client.post(
        "/ingest",
        json={"text": "This is a test text for ingestion"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Text successfully ingested",
        "status_code": 200,
        "success": True
    }

def test_ingest_invalid_json():
    response = client.post(
        "/ingest",
        data="invalid json"
    )
    assert response.status_code == 422
    assert "detail" in response.json()

def test_query_text():
    response = client.get("/query", params={"text": "AI mail assistant"})
    assert response.status_code == 200

    results = response.json()
    assert len(results) > 0
    assert "text" in results[0]
    assert "similarity" in results[0]
    assert isinstance(results[0]["similarity"], float)

def test_query_with_k_parameter():
    response = client.get("/query", params={"text": "AI", "k": 2})
    assert response.status_code == 200

    results = response.json()
    assert len(results) <= 2
