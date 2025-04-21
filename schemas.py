from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class QueryResponse(BaseModel):
    text: str
    similarity: float 