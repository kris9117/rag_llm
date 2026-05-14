from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.retriever import retrieve_context
from app.services.llm_service import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
async def query_docs(request: QueryRequest):

    results = retrieve_context(request.question)

    answer = generate_answer(request.question, results)

    sources = [doc.page_content[:300] for doc in results]

    return {
        "question": request.question,
        "answer": answer,
        "source_chunks": sources
    }