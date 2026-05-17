from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
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
   loader = PyPDFDirectoryLoader(data_path)
   document = loader.load()
   #chunking
   chunking = RecursiveCharacterTextSplitter(
      chunk_size=1000,
      chunk_overlap=200
   )

   chunks=chunking.split_documents(document)

   embed = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-large-en-v1.5")

   #vector database

   vectordb = Chroma(
      collection_name="rag_data",
      embedding_function=embed,
      persist_directory=str(chroma_path)
   )

   vectordb.add_documents(documents=chunks)







