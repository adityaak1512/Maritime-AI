import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

PDF_PATH = "data/MARPOL Annex VI.pdf" 
DB_DIR = "chroma_db"

if os.path.exists(PDF_PATH):
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(docs)
    
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    vector_db = Chroma.from_documents(
        documents=splits, 
        embedding=embeddings, 
        persist_directory=DB_DIR
    )
    print(f"✅ Success: {len(splits)} chunks saved to {DB_DIR}")
else:
    print(f"❌ Error: {PDF_PATH} not found.")