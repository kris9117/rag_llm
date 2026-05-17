from langchain_ollama import ChatOllama
from app.core.logger import logger

llm = ChatOllama(
    model="llama3",
    temperature=0
)

def generate_answer(question, context, history):

    try:

        joined_context = "\n\n".join(
            [doc.page_content for doc in context]
        )

        history_text = "\n".join([
            f"{msg['role']}: {msg['content']}"
            for msg in history
        ])

        prompt = f"""
You are a helpful AI assistant.

Use:
1. Previous conversation history
2. Retrieved context

to answer the user.

Conversation History:
{history_text}

Retrieved Context:
{joined_context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        logger.info("Generated conversational response")

        return response.content

    except Exception as e:

        logger.error(str(e))

        raise e