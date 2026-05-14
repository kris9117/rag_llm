from app.rag.embeddings import embedding_model
from app.rag.vector_store import search_faiss
from app.core.logger import logger

def retrieve_context(query: str, top_k=3):
    try:
        logger.info(f"Retrieving context for query: {query}")

        query_vector = embedding_model.encode(query)

        results = search_faiss(query_vector, top_k=top_k)

        return results

        

    except Exception as e:
        logger.error(str(e))
        raise e
    

