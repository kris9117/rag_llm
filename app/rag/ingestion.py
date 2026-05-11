from langchain_community.document_loaders import PyPDFLoader
from app.core.logger import logger

def load_pdf(pdf_path: str):

    try:

        logger.info(f"Loading PDF: {pdf_path}")

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

        logger.info(f"Loaded {len(documents)} pages")

        print("\n========= FIRST PAGE CONTENT =========\n")

        print(documents[0].page_content[:1000])

        print("\n========= METADATA =========\n")

        print(documents[0].metadata)

        return documents

    except Exception as e:

        logger.error(f"Error loading PDF: {str(e)}")

        raise e