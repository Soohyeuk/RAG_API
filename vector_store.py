import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from typing import List, Union

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.dimension = self.model.get_sentence_embedding_dimension()
        self.faiss_index = faiss.IndexFlatL2(self.dimension)
        self.texts = []

    def add(self, texts: Union[str, List[str]]) -> None:
        """Add text(s) to the vector store.
        
        Args:
            texts: Either a single string or a list of strings to add
        """
        texts_list = [texts] if isinstance(texts, str) else texts
        embeddings = self.model.encode(texts_list)
        self.faiss_index.add(embeddings.astype('float32'))
        self.texts.extend(texts_list)

    def search(self, query: str, k: int = 3) -> List[tuple]:
        """Search for similar texts.
        
        Args:
            query: The search query string
            k: Number of results to return
            
        Returns:
            List of tuples containing (text, similarity_score)
        """
        query_embedding = self.model.encode(query)
        distances, indices = self.faiss_index.search(np.array([query_embedding]).astype('float32'), k)
        
        return [(self.texts[idx], float(1 / (1 + distances[0][i]))) 
                for i, idx in enumerate(indices[0])] 