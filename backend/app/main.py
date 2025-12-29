from fastapi import FastAPI
from app.routes import upload, chat, documents

app = FastAPI(title="Chat With Your Documents")

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(documents.router, prefix="/documents", tags=["Documents"])

@app.get("/")
def root():
    return {"message": "Backend running da"}
