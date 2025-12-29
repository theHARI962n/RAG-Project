from fastapi import APIRouter
from app.services.rag_engine import retrieve_relevant_chunks

router = APIRouter()

@router.post("/search")
def search(query: str):
    results = retrieve_relevant_chunks(query)
    return {
        "query": query,
        "results": results
    }
