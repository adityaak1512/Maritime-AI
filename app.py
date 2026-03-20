import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="Maritime AI", page_icon="🚢")
st.title("🚢 Maritime AI: MARPOL Assistant")

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vector_db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

system_prompt = (
    "You are a maritime legal expert. Use the following context to answer the question. "
    "If the answer isn't in the context, say you don't know. "
    "\n\n"
    "{context}"
)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(vector_db.as_retriever(), question_answer_chain)

query = st.text_input("Ask a question about MARPOL Annex VI:")

if query:
    with st.spinner("Analyzing regulations..."):
        response = rag_chain.invoke({"input": query})
        st.markdown("### Response:")
        st.write(response["answer"])