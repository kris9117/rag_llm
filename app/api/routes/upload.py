from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.rag.ingestion import load_pdf
from app.rag.chunking import chunk_documents
from app.rag.embeddings import generate_embeddings

from app.core.logger import logger

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")

async def upload_pdf(file: UploadFile = File(...)):

    try:

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info(f"Uploaded file: {file.filename}")

        documents = load_pdf(file_path)

        chunks = chunk_documents(documents)
        vectors, chunks = generate_embeddings(chunks)

        return {

            "filename": file.filename,

            "pages_loaded": len(documents),

            "chunks_created": len(chunks),

            "embedding_created": len(vectors),

            "embedding_diemension": len(vectors[0]),

            "status": "success"
        }

    except Exception as e:

        logger.error(str(e))

        return {

            "status": "error",

            "message": str(e)
        }