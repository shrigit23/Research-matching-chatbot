# Research Matching Chatbot

A terminal-based **Research Matching Chatbot** that helps students discover faculty members whose research interests align with their project ideas, while also assisting professors in identifying collaboration opportunities, research gaps, and emerging trends.

The chatbot uses **Retrieval-Augmented Generation (RAG)** with **ChromaDB** and **HuggingFace embeddings** to perform semantic search across faculty profiles, providing accurate and relevant matches instead of simple keyword-based results.

---

# Features

* 🎓 Match students with faculty research interests
* 🔍 Semantic search using ChromaDB (Vector Database)
* 📚 RAG pipeline for context-aware retrieval
* 🧠 Uses HuggingFace MiniLM embeddings (`all-MiniLM-L6-v2`)
* 📄 Supports multiple faculty profiles stored as text files
* 🤝 Cross-match faculty profiles to identify collaboration opportunities
* 📈 Track emerging research trends using Tavily Search
* ⚠️ Detect research gaps between faculty expertise
* ✅ Human-in-the-loop confirmation before logging important decisions
* 💻 Fully terminal-based (No UI required)

---

# Problem Statement

Finding the right faculty mentor for research projects is often difficult because students rely on manual browsing of faculty webpages and keyword searches.

Similarly, professors may miss potential collaborations due to limited visibility into overlapping research interests.

This chatbot solves these problems using semantic search over faculty research profiles.

---

# Tech Stack

| Technology             | Purpose               |
| ---------------------- | --------------------- |
| Python                 | Backend               |
| LangChain              | RAG Pipeline          |
| ChromaDB               | Vector Database       |
| HuggingFace Embeddings | Semantic Embeddings   |
| all-MiniLM-L6-v2       | Embedding Model       |
| TextLoader             | Load Faculty Profiles |
| CharacterTextSplitter  | Document Chunking     |
| dotenv                 | Environment Variables |
| Tavily Search API      | Live Research Trends  |

---

# Project Structure

```
Research-Matching-Chatbot/
│
├── data/
│   ├── faculty1.txt
│   ├── faculty2.txt
│   ├── faculty3.txt
│   └── ...
│
├── db/
│   └── Chroma Database
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

# Workflow

```
Faculty Profiles (.txt)
        │
        ▼
Load Documents
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
(HuggingFace MiniLM)
        │
        ▼
Store in ChromaDB
        │
        ▼
User Query
        │
        ▼
Similarity Search
        │
        ▼
Rank Faculty Profiles
        │
        ▼
Display Best Matches
```

---

# How It Works

### Step 1: Load Faculty Profiles

The chatbot reads every faculty profile stored as a `.txt` file inside the `data/` directory.

Each document stores metadata containing its source filename.

---

### Step 2: Document Chunking

Faculty profiles are divided into smaller chunks using:

* Chunk Size: **500**
* Chunk Overlap: **50**

This improves retrieval quality.

---

### Step 3: Generate Embeddings

Each chunk is converted into dense vector embeddings using:

```
all-MiniLM-L6-v2
```

from HuggingFace.

---

### Step 4: Store in ChromaDB

The embeddings are stored inside a persistent Chroma vector database.

```
persist_directory="db"
```

---

### Step 5: Semantic Search

When a student asks a question like:

```
I am interested in Machine Learning for Agriculture.
```

the chatbot:

* Converts the query into embeddings
* Performs similarity search
* Retrieves the Top-K relevant faculty profiles
* Calculates similarity score
* Displays the best matches

---

### Step 6: Research Trend Analysis

Using the Tavily Search API, the chatbot can fetch the latest research developments in a specific domain, helping students and faculty stay updated with current trends.

---

### Step 7: Collaboration & Gap Analysis

The chatbot compares faculty research areas to:

* Identify overlapping expertise
* Suggest interdisciplinary collaborations
* Highlight underexplored research topics and gaps

---

### Step 8: Human-in-the-Loop

Before saving or logging recommendations, the chatbot requests user confirmation to ensure important decisions are validated by a human.

---

# Sample Query

```
Ask your query:

I want to work on Computer Vision in Healthcare.
```

### Output

```
Top Matches

Faculty: Dr. A

Research Areas:
- Medical Imaging
- Deep Learning
- Computer Vision

Similarity: 0.91
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Research-Matching-Chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
TAVILY_API_KEY=your_api_key
```

Run the chatbot

```bash
python app.py
```

---

# Evaluation Criteria Mapping

| Criteria                    | Implementation                                                                                                         |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **RAG Usage (15%)**         | ChromaDB retrieves relevant faculty profile chunks using semantic search.                                              |
| **Tool Usage (15%)**        | LangChain, ChromaDB, HuggingFace Embeddings, Tavily Search API, dotenv.                                                |
| **Agent Design (20%)**      | Multi-step workflow: retrieval → matching → trend analysis → collaboration analysis → confirmation.                    |
| **Workflow Design (20%)**   | Document loading → chunking → embedding → vector storage → semantic retrieval → recommendation.                        |
| **Human-in-the-Loop (15%)** | User confirmation before logging or finalizing recommendations.                                                        |
| **Demo Quality (15%)**      | Terminal-based chatbot with live semantic search, ranked faculty matches, research trends, and collaboration insights. |

---

# Future Enhancements

* Web-based interface using Streamlit or React
* PDF and DOCX faculty profile support
* LLM-generated explanations for recommendations
* Personalized student research profiles
* Multi-university faculty database
* Research paper recommendations
* Email notifications for collaboration opportunities
* Advanced analytics dashboard for research trends

---

# Key Highlights

* **Semantic faculty matching** instead of keyword search.
* **Fast vector search** using ChromaDB.
* **Retrieval-Augmented Generation (RAG)** for context-aware responses.
* **Live research trend analysis** via Tavily Search.
* **Cross-faculty collaboration recommendations** and research gap identification.
* **Human-in-the-loop validation** before logging decisions.
* **Scalable architecture** supporting additional faculty profiles and institutions.

---
## 🎥 Demo Video

▶️ **Watch the Demo:** https://www.youtube.com/watch?v=306xeV3yk8A

## Authors

Developed as part of the **Hackathon: Build & Showcase** project to demonstrate an AI-powered research assistant that bridges the gap between students and faculty through intelligent semantic search and retrieval.
