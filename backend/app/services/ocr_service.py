from pdf2image import convert_from_path
import pytesseract

def extract_text_with_ocr(file_path: str):
    pages_text = []

    images = convert_from_path(file_path, dpi=300)

    for idx, image in enumerate(images, start=1):
        image = image.convert("L")  # grayscale

        text = pytesseract.image_to_string(image)

        if text.strip():
            pages_text.append({
                "page": idx,
                "text": text.strip()
            })

    return pages_text
