from fastapi import FastAPI
from pydantic import BaseModel
from app.rag.rag_pipeline import ask_question, chat_memory
from app.rag.data_ingestion import data_ingest

app = FastAPI()

class query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"API": "Running Successfully"}

@app.get("/data")
def ingest():
    return data_ingest()

@app.post("/chat")
def chat(questions: query):
    result = ask_question(questions.question)
    return result

@app.post("/memory/reset")
def reset_memory():
    chat_memory.clear()
    return {"status": "memory reset", "entries": len(chat_memory)}

@app.get("/memory")
def get_memory():
    return {"memory": chat_memory}