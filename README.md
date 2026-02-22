# 📄 Context-Aware Document Intelligence  
### A Simple Yet Powerful RAG Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-green)
![LLM](https://img.shields.io/badge/LLM-Google%20Gemini-orange)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![VectorDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🌍 The Idea Behind This Project

We often upload long PDFs — research papers, reports, notes — but finding answers inside them is slow and frustrating.

So I built this project to solve a simple problem:

👉 **What if you could just chat with your document and get clear answers instantly?**

This app lets you upload a PDF and ask questions in natural language.  
The AI reads the document, finds the most relevant parts, and gives answers grounded in the actual content — not guesses.

---

## 🚀 What This Project Does

This is a full **Retrieval-Augmented Generation (RAG)** system that:

- Reads complex PDF documents
- Breaks them into meaningful chunks
- Converts text into semantic vectors
- Searches for relevant context
- Uses an LLM to generate accurate answers
- Avoids hallucinations by grounding responses in the document

All of this runs in a clean, single-file Streamlit app.

---

## 🧠 How It Works (Simple Flow)

### 📥 Step 1 — Upload Document
The app reads your PDF using PyPDF and splits it into smaller chunks so context is preserved.

### 🔎 Step 2 — Create Embeddings
Each chunk is converted into vector embeddings using Google’s embedding model.

### 🗄️ Step 3 — Store in Vector Database
The vectors are stored in ChromaDB for fast semantic search.

### 💬 Step 4 — Ask Questions
When you ask a question, the system finds the most relevant chunks.

### 🤖 Step 5 — Generate Answer
The Gemini LLM generates a response using only the retrieved context to ensure accuracy.

---

## ✨ Why This Project Is Special

✅ Clean single-file architecture  
✅ Easy to deploy anywhere  
✅ Designed to reduce hallucinations  
✅ Real-time conversational interface  
✅ Demonstrates real GenAI engineering skills  
✅ Production-style pipeline  

---

## 🛠️ Tech Stack

| Area | Tools |
|------|------|
| Framework | LangChain (LCEL) |
| LLM | Gemini 2.5 Flash |
| Embeddings | Gemini Embedding 001 |
| Vector Database | ChromaDB |
| Frontend | Streamlit |
| PDF Processing | PyPDF |
| Language | Python |

---

## 🧩 Skills Demonstrated

This project highlights practical skills in:

- Retrieval-Augmented Generation
- LLM orchestration
- Prompt engineering
- Semantic search
- Vector databases
- AI system design
- API integration
- Streamlit app development
- Building production-style pipelines

---

## 🚀 How To Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/KrMayank789/CADIS.git
cd CADIS
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

**Windows**
```bash
.\venv\Scripts\Activate.ps1
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5️⃣ Run App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
context-aware-rag/
│
├── rag_app.py
├── requirements.txt
├── README.md
└── streamlit_app.py
└── .env
```

---

## 🔮 Future Improvements

I’d love to expand this project with:

- Hybrid search (keyword + semantic)
- Multiple document support
- Conversation memory
- Highlighting sources in answers
- Persistent database storage
- Docker deployment
- Authentication system

---

## 🎯 What This Project Shows About Me

This project reflects my ability to:

✔ Build real AI systems end-to-end  
✔ Understand how LLMs work beyond simple API calls  
✔ Design scalable pipelines  
✔ Focus on accuracy and user experience  
✔ Turn complex ideas into simple products  

---

## 🏆 Potential Use Cases

- Research assistants
- Legal document analysis
- Study tools
- Knowledge base search
- Internal company documentation chatbot
- Report analysis tools

---

## 👨‍💻 About the Author

Hi, I’m **Mayank Kumar** 👋  

I enjoy building practical AI systems that solve real problems and make technology easier to use.

If you liked this project, feel free to ⭐ the repo!

---

## 📜 License

MIT License — Free to use and modify.

---

## 💭 Final Note

This project is not just about using an LLM — it’s about building a reliable system around it.

Because great AI products aren’t just smart… they’re trustworthy.
