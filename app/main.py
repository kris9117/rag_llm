from fastapi import FastAPI
from app.core.logger import logger
from app.api.routes.upload import router as upload_router
from app.api.routes.query import router as query_router

app = FastAPI(
    title="RAG LLM API",
    version="1.0"
)

app.include_router(upload_router)
app.include_router(query_router)

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