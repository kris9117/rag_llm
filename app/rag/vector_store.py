import faiss
import numpy as np
import pickle
import os

from app.core.logger import logger

INDEX_PATH = "vector_store/faiss_index.index"
DOC_PATH = "vector_store/chunks.pkl"

def create_faiss_index(vectors, chunks):
    try:
        logger.info("Creating FAISS index")

        vectors = np.array(vectors).astype("float32")

        dimension = vectors.shape[1]

        index = faiss.IndexFlatL2(dimension)

        index.add(vectors)

        faiss.write_index(index, INDEX_PATH)

        with open(DOC_PATH, "wb") as f:
            pickle.dump(chunks, f)

        logger.info("FAISS index saved")

    except Exception as e:
        logger.error(str(e))
        raise e
    


def search_faiss(query_vector, top_k=3):
    try:
        index = faiss.read_index(INDEX_PATH)

        with open(DOC_PATH, "rb") as f:
            chunks = pickle.load(f)

        query_vector = np.array([query_vector]).astype("float32")

        distances, indices = index.search(query_vector, top_k)

        results = [chunks[i] for i in indices[0]]

        return results

    except Exception as e:
        logger.error(str(e))
        raise e