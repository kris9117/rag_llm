from fastapi import FastAPI
from app.core.logger import logger

app = FastAPI(
    title="RAG LLM API",
    version="1.0"
)

@app.get("/")
async def home():
    logger.info("Home endpoint called")
    return {
        "message": "RAG LLM System Running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }