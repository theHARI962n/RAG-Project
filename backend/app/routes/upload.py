from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_utils import save_uploaded_file
from app.services.pdf_loader import extract_text_from_pdf
from app.services.chunker import chunk_pages

router = APIRouter()

@router.post("/")
def upload_document(file: UploadFile = File(...)):
    try:
        file_path = save_uploaded_file(file)
        pages = extract_text_from_pdf(file_path)
        chunks = chunk_pages(pages)

        return {
            "message": "File processed",
            "pages": len(pages),
            "chunks_created": len(chunks),
            "sample_chunk": chunks[0]
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
