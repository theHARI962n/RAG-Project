import os
import uuid
from fastapi import UploadFile
from app.config import UPLOAD_DIR

def save_uploaded_file(file: UploadFile) -> str:
    file_ext = os.path.splitext(file.filename)[1]

    if file_ext.lower() != ".pdf":
        raise ValueError("Only PDF files are allowed")

    unique_name = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path
