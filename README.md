AI-powered medical Q&A system built on Retrieval-Augmented Generation (RAG). Ingests clinical documents, indexes them into a vector database, and answers natural language medical queries using LLM APIs — with source citations for traceability.
Tech Stack

Language — Python 3.8
LLM Orchestration — LangChain
Vector Store — ChromaDB
Embeddings — OpenAI text-embedding-ada-002
LLM — OpenAI GPT-3.5-turbo
Frontend — Streamlit
Document Parsing — LangChain PDF Loaders · PyMuPDF
Environment — Conda

What this project does
MedIQ allows users to query medical documents (clinical guidelines, research papers, patient FAQs) using natural language. Instead of returning a generic LLM response, it retrieves the most relevant document chunks first (RAG), then generates a grounded answer with source references , reducing hallucination risk in a healthcare context.
Key use cases:

Query clinical guidelines without reading full PDFs
Summarise research papers on demand
Answer patient FAQs from a curated knowledge base
Architecture
User query
    │
    ▼
Streamlit UI (app.py)
    │
    ▼
LangChain RetrievalQA chain
    ├── Embeddings model (OpenAI / HuggingFace)
    │       └── Query → vector representation
    │
    ├── ChromaDB / FAISS vector store
    │       └── Similarity search → top-k relevant chunks
    │
    └── LLM (GPT-3.5 / GPT-4)
            └── Context + query → grounded answer with citations
Data ingestion pipeline:
Raw medical PDFs / text files
    → LangChain document loader
    → Text splitter (chunk size: 500 tokens, overlap: 50)
    → Embedding model
    → ChromaDB vector store (persisted locally)
Project structure
    MedIQ/
├── src/
│   ├── ingestion.py        # Document loading, chunking, embedding
│   ├── retriever.py        # Vector store query logic
│   ├── chain.py            # LangChain RetrievalQA setup
│   └── utils.py            # Helper functions
├── research/               # Notebooks for experimentation
├── app.py                  # Streamlit frontend
├── requirements.txt
└── setup.py


Skills demonstrated

RAG pipeline design — end-to-end from raw documents to grounded LLM response
LangChain — RetrievalQA chain, document loaders, text splitters
Vector databases — embedding, indexing, similarity search with ChromaDB/FAISS
LLM API integration — OpenAI API, prompt engineering, response parsing
Python — modular project structure with separation of ingestion, retrieval, and generation
Streamlit — interactive frontend for non-technical users
Healthcare domain awareness — understanding of why hallucination reduction matters in clinical contexts

1. Clone the repository
bashgit clone https://github.com/<your-username>/MedIQ-End-to-End-Powered-Medical-Chat-Assistant
cd MedIQ-End-to-End-Powered-Medical-Chat-Assistant
2. Create and activate environment
bashconda create -n llmapp python=3.8 -y
conda activate llmapp
3. Install dependencies
bashpip install -r requirements.txt
4. Add your OpenAI API key
Create a .env file in the root directory:
OPENAI_API_KEY=your_key_here
5. Run the app
bashstreamlit run app.py
