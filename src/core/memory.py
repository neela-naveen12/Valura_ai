memory = {}

def get_history(session_id):
    return memory.get(session_id, [])

def add_message(session_id, message):
    if session_id not in memory:
        memory[session_id] = []
    memory[session_id].append(message)