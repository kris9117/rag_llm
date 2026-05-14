from app.rag.embeddings import embedding_model
from app.rag.vector_store import search_faiss
from app.core.logger import logger
from cachetools import TTLCache

query_cache = TTLCache(maxsize=100, ttl=300)

def retrieve_context(query: str, top_k=3):

    if query in query_cache:
        return query_cache[query]

    query_vector = embedding_model.encode(query)

    results = search_faiss(query_vector, top_k)

    query_cache[query] = results

    return results
    

