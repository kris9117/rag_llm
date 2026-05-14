from langchain_ollama import ChatOllama
from app.core.logger import logger

llm = ChatOllama(
    model="llama3",
    temperature=0
)

def generate_answer(question: str, context: list):
    try:
        joined_context = "\n\n".join([doc.page_content for doc in context])

        prompt = f"""
Answer ONLY using the context below.
If answer is unavailable, say:
I could not find this in uploaded documents.

Context:
{joined_context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        logger.info("Generated local LLM response")

        return response.content

    except Exception as e:
        logger.error(str(e))
        raise e