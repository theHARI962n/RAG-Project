from pypdf import PdfReader
from app.services.ocr_service import extract_text_with_ocr

def extract_text_from_pdf(file_path: str):
    reader = PdfReader(file_path)
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text and text.strip():
            pages.append({
                "page": page_number,
                "text": text.strip()
            })

    # If no text found → scanned PDF
    if not pages:
        print("No text found, running OCR...")
        pages = extract_text_with_ocr(file_path)

    return pages
