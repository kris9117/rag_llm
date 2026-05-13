from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.retriever import retrieve_context

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
async def query_docs(request: QueryRequest):

    results = retrieve_context(request.question)

    context = [doc.page_content for doc in results]

    return {
        "question": request.question,
        "retrieved_chunks": context
    }