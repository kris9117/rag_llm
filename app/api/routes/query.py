from fastapi import APIRouter, Depends
from app.core.security import verify_api_key

from app.models.schemas import QueryRequest

from app.rag.retriever import retrieve_context
from app.services.llm_service import generate_answer

router = APIRouter()

@router.post("/query")
async def query_docs(
    request: QueryRequest,
    _: str = Depends(verify_api_key)
):

    results = retrieve_context(request.question)

    answer = generate_answer(request.question, results)

    sources = [
        {
            "text": doc.page_content[:300],
            "page": doc.metadata.get("page", "NA")
        }
        for doc in results
    ]

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }