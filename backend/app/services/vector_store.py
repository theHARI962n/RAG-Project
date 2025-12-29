from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import BASE_DIR
import os

CHROMA_DIR = os.path.join(BASE_DIR, "data", "chroma")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def get_vector_store():
    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embedding_model
    )
