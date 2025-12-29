from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_utils import save_uploaded_file
from app.services.pdf_loader import extract_text_from_pdf
from app.services.chunker import chunk_pages
from app.services.embeddings import store_chunks

router = APIRouter()

@router.post("/")
def upload_document(file: UploadFile = File(...)):
    try:
        file_path = save_uploaded_file(file)

        pages = extract_text_from_pdf(file_path)
        chunks = chunk_pages(pages)

        store_chunks(chunks)

        return {
            "message": "Document indexed successfully",
            "pages": len(pages),
            "chunks_stored": len(chunks)
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
