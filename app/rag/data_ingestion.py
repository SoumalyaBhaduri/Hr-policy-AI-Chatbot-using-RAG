from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from pathlib import Path

#base Directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent
#database path
chroma_path = os.path.join(BASE_DIR, "chromadb")
#data path
data_path = os.path.join(BASE_DIR, "data")

def data_ingest():
   #load data
   loader = DirectoryLoader(data_path)
   document = loader.load()
   #chunking
   chunking = RecursiveCharacterTextSplitter(
      chunk_size=500,
      chunk_overlap=50
   )

   chunks=chunking.split_documents(document)

   embed = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

   #vector database

   vectordb = Chroma(
      collection_name="rag_data",
      embedding_function=embed,
      persist_directory=str(chroma_path)
   )

   vectordb.add_documents(documents=chunks)







