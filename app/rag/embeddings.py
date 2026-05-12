from sentence_transformers import SentenceTransformer
from app.core.logger import logger

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    try:
        logger.info("Generating embeddings")
        texts = [chunk.page_content for chunk in chunks]

        vectors = embedding_model.encode(texts)

        logger.info(f"Generated embeddings for {len(vectors)} chunks")

        return vectors, chunks
    

    except Exception as e:
        logger.error(f"Embedding error: {str(e)}")
        raise e