from app.services.vector_store import get_vector_store

def store_chunks(chunks: list):
    """
    chunks = [
      {
        "text": "...",
        "metadata": {"page": 1}
      }
    ]
    """
    vector_store = get_vector_store()

    texts = [chunk["text"] for chunk in chunks]
    metadatas = [chunk["metadata"] for chunk in chunks]

    vector_store.add_texts(texts=texts, metadatas=metadatas)
    vector_store.persist()
