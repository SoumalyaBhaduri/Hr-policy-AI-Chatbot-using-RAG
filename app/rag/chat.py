from langchain_groq import ChatGroq
from app.core.config import GROQ_API_KEY, MODEL_NAME

groq_llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=0
)


def generate_response(prompt: str):
    response = groq_llm.invoke(prompt)
    return response.content