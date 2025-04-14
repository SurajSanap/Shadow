import json

# Logic to embed and store chunks using FAISS or similarimport json
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

class VectorStore:
    def __init__(self, chunks_path: str, embedding_model: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(embedding_model)

        with open(chunks_path, 'r') as f:
            self.chunks = json.load(f)
        self.embeddings = self.model.encode([chunk["text"] for chunk in self.chunks])

    def query(self, input_text: str, top_k: int = 3):
        input_emb = self.model.encode([input_text])

        sims = cosine_similarity(input_emb, self.embeddings)[0]

        top_indices = sims.argsort()[-top_k:][::-1]
        
        return [self.chunks[i] for i in top_indices]
