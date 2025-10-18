# dependencies: pip install fastapi uvicorn numpy pydantic
# uvicorn main:app --reload

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import numpy as np
import httpx

# Initialize FastAPI app
app = FastAPI(title="InfoCore Similarity Service")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],   
    allow_headers=["*"],  
)

# Pydantic model for request body
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Compute cosine similarity between two vectors."""
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

@app.post("/similarity")
async def compute_similarity(request: SimilarityRequest):
    """
    Computes cosine similarity between the query embedding and each document embedding.
    Returns the top 3 most similar documents.
    """
    docs = request.docs
    query = request.query


    url= "https://aipipe.org/openai/v1/embeddings"
    headers = {
        "Authorization": "Bearer <ai_pipe_token>",
        "Content-Type": "application/json",
    }

    # 🔹 Generate embeddings for all documents + query
    inputs = docs + [query]

    payload={
        "model":"text-embedding-3-small",
        "input":inputs
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        data = response.json()

    # Check for errors
    if "data" not in data:
        return {"error": data}

    # Extract embeddings
    embeddings = [item["embedding"] for item in data["data"]]

    doc_embeddings = embeddings[:-1]
    query_embedding = embeddings[-1]

    # 🔹 Compute cosine similarity between query and each document
    scores = [cosine_similarity(query_embedding, doc_emb) for doc_emb in doc_embeddings]

    # 🔹 Rank documents by similarity (descending)
    ranked_indices = np.argsort(scores)[::-1]
    top_matches = [docs[i] for i in ranked_indices[:3]]

    # 🔹 Return top 3 matches
    return {"matches": top_matches}

# run the server: uvicorn main:app --reload
# the url is: http://127.0.0.1:8000/similarity










  
