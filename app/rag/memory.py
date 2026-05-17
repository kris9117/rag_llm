from collections import defaultdict

# session_id -> chat history
chat_memory = defaultdict(list)

def add_to_memory(session_id, role, content):

    chat_memory[session_id].append({
        "role": role,
        "content": content
    })

def get_memory(session_id):

    return chat_memory[session_id]