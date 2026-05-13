from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os
from pathlib import Path

#base Directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent
#database path
chroma_path = os.path.join(BASE_DIR, "chromadb")

def retrive(query: str):

    #Embedding

    embed = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

    #Vector Database

    vectordb = Chroma(
        embedding_function=embed,
        persist_directory=str(chroma_path)
    )

    #search

    retrieved = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    return retrieved.invoke(query)