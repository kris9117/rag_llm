from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.logger import logger

def chunk_documents(documents):

    try:

        logger.info("Starting document chunking")

        text_splitter = RecursiveCharacterTextSplitter(

            chunk_size=500,
            chunk_overlap=100,
            length_function=len

        )

        chunks = text_splitter.split_documents(documents)

        logger.info(f"Generated {len(chunks)} chunks")

        return chunks

    except Exception as e:

        logger.error(f"Chunking error: {str(e)}")

        raise e