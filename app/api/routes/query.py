from fastapi import APIRouter, Depends

from app.core.security import verify_api_key

from app.models.schemas import QueryRequest

from app.rag.retriever import retrieve_context
from app.rag.memory import add_to_memory, get_memory

from app.services.llm_service import generate_answer

router = APIRouter()

@router.post("/query")

async def query_docs(
    request: QueryRequest,
    _: str = Depends(verify_api_key)
):

    history = get_memory(request.session_id)

    results = retrieve_context(request.question)

    answer = generate_answer(
        request.question,
        results,
        history
    )

    add_to_memory(
        request.session_id,
        "user",
        request.question
    )

    add_to_memory(
        request.session_id,
        "assistant",
        answer
    )

    sources = [
        {
            "text": doc.page_content[:300],
            "page": doc.metadata.get("page", "NA")
        }
        for doc in results
    ]

    return {
        "session_id": request.session_id,
        "question": request.question,
        "answer": answer,
        "sources": sources
    }