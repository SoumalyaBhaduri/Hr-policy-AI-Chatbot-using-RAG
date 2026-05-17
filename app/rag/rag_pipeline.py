from app.rag.retriever import retrive
from app.rag.chat import generate_response

chat_memory = []
MAX_MEMORY_ENTRIES = 10


def _get_memory_context() -> str:
    if not chat_memory:
        return ""
    memory_lines = []
    for entry in chat_memory[-MAX_MEMORY_ENTRIES:]:
        memory_lines.append(f"User: {entry['question']}")
        memory_lines.append(f"Assistant: {entry['answer']}")
    return "\n".join(memory_lines)


def ask_question(question: str):
    docs = retrive(query=question)

    context = "".join([doc.page_content for doc in docs])
    memory_context = _get_memory_context()

    prompt = f"""You are an AI assistant responding to question.
    Use prior conversation memory to keep continuity.
    only provide resposne to the question.
    Previous conversation:
    {memory_context or 'None'}
    Context:
    {context}
    Question:
    {question}
    Answer:"""

    response = generate_response(prompt)
    chat_memory.append({"question": question, "answer": response})
    if len(chat_memory) > MAX_MEMORY_ENTRIES:
        del chat_memory[0]

    return {
        "question": question,
        "answer": response,
        "context": context,
        "memory": memory_context
    }