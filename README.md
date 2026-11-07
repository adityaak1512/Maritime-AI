# 🚢 Maritime AI: MARPOL Assistant

An intelligent regulatory assistant that uses **Retrieval-Augmented Generation (RAG)** to answer complex questions about MARPOL Annex VI. Built with Google Gemini 2.5 and LangChain.

## 🌟 Features
* **Regulatory RAG:** Processes technical maritime PDFs (like MARPOL) into a searchable vector database.
* **Gemini 2.5 Integration:** Leverages the latest LLM reasoning for high-accuracy compliance answers.
* **Streamlit Interface:** Clean, web-based chat UI for maritime professionals.

## 🛠️ Tech Stack
* **LLM:** Google Gemini 2.5 Flash
* **Embeddings:** Google Gemini Embedding 2
* **Orchestration:** LangChain (Classic)
* **Vector Store:** ChromaDB
* **Frontend:** Streamlit

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.12+
* A Google AI Studio API Key

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/adityaak1512/Maritime-AI.git
cd Maritime-AI

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
