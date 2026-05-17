# Enterprise RAG PDF Chatbot

A production-style Retrieval-Augmented Generation (RAG) chatbot built using Groq, LangChain, FastAPI, Streamlit, Docker, and FAISS.

This project allows users to upload PDF documents and interact with them conversationally using semantic search and LLM-powered responses.

---

## Features

- PDF Upload & Ingestion
- Semantic Chunking
- Vector Search with Chromadb
- Groq LLM Integration
- FastAPI Backend
- Streamlit Frontend
- Dockerized Deployment
- RAGAS Evaluation Pipeline
- Low Hallucination Responses
- Enterprise-Style Architecture

---

## Tech Stack

- Python
- LangChain
- Groq
- FastAPI
- Streamlit
- Chromadb
- HuggingFace Embeddings
- Docker
- RAGAS

---

## Architecture

text User  ↓ Streamlit Frontend  ↓ FastAPI Backend  ↓ Retriever  ↓ FAISS Vector Store  ↓ Groq LLM 

---

## Dockerized Infrastructure

This project is fully containerized using Docker and Docker Compose.

Services:
- FastAPI API Container
- Streamlit Frontend Container

Benefits:
- Consistent environments
- Easy deployment
- Scalable architecture
- Simplified dependency management
- Production-ready setup

---

## RAGAS Evaluation Scores

| Metric | Score |
|---|---|
| Faithfulness | 1.0000 |
| Answer Relevancy | 0.9149 |
| Context Precision | 1.0000 |
| Context Recall | 1.0000 |

---

## Installation

### Clone Repository

bash git clone <repo_url> cd Pdf_Chatbot 

---

## Environment Variables

env GROQ_API_KEY=your_key MODEL_NAME=llama-3.3-70b-versatile 

---

## Run with Docker

### Build Containers

bash docker compose build --no-cache 

### Start Services

bash docker compose up 

---

## Access Application

### Streamlit Frontend

text http://localhost:8501 

### FastAPI Docs

text http://localhost:8000/docs 

---

## Project Structure

text Pdf_Chatbot/ │ ├── app/ │   ├── rag/ │   ├── frontend.py │   ├── main.py │ ├── data/ ├── vectorstore/ ├── eval.py ├── requirements.txt ├── Dockerfile.api ├── Dockerfile.streamlit ├── docker-compose.yml └── .env 

---

## Future Improvements

- Hybrid Search (BM25 + Vector)
- Reranking
- Qdrant Integration
- Authentication
- Multi-user Chat Memory
- GPU Embeddings
- Kubernetes Deployment
- CI/CD Pipeline
