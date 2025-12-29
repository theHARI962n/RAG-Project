from app.services.vector_store import get_vector_store

def retrieve_relevant_chunks(query: str, k: int = 4):
    """
    Returns top-k relevant chunks for the query.
    """
    vector_store = get_vector_store()

    docs = vector_store.similarity_search(query, k=k)

    results = []
    for doc in docs:
        results.append({
            "text": doc.page_content,
            "metadata": doc.metadata
        })

    return results
