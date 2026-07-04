import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

import state
from tools import trend_search

# ----------------------------
# LOAD MODEL ONLY ONCE
# ----------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="db",
    embedding_function=embeddings
)


# ----------------------------
# LOAD DATA
# ----------------------------

def load_documents():
    docs = []
    folder_path = "data"

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(folder_path, file))
            docs.extend(loader.load())

    return docs


def split_docs(documents):
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


def create_vectorstore(docs):

    db = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="db"
    )

    return db


# ----------------------------
# HELPERS
# ----------------------------

def extract_name(text):

    for line in text.split("\n"):
        if line.lower().startswith("name:"):
            return line.strip()

    return "Unknown"


def similarity_score(score):
    return 1 / (1 + score)


# ----------------------------
# SEARCH FACULTY
# ----------------------------

def search_faculty(query):

    results = db.similarity_search_with_score(query, k=10)

    unique = {}

    for doc, score in results:

        name = extract_name(doc.page_content)

        if name not in unique:
            unique[name] = (doc, score)

    state.last_results = list(unique.values())
    state.current_index = 0

    output = "\n🔍 Top Matches:\n\n"

    for doc, score in state.last_results:

        sim = similarity_score(score)

        output += (
            f"📄 {doc.page_content}\n"
            f"⭐ Similarity: {sim:.2f}\n\n"
        )

    return output


# ----------------------------
# SHOW NEXT RESULT
# ----------------------------

def show_next():

    if state.current_index >= len(state.last_results):
        return "❌ No more results."

    doc, score = state.last_results[state.current_index]

    state.current_index += 1

    sim = similarity_score(score)

    return (
        f"\n📄 {doc.page_content}\n"
        f"⭐ Similarity: {sim:.2f}\n"
    )


# ----------------------------
# DETAIL LOOKUP
# ----------------------------

def detail_lookup(query):

    name = query.lower().replace(
        "tell me about",
        ""
    ).strip()

    results = db.similarity_search(name, k=1)

    if not results:
        return "No faculty found."

    return f"\n📄 {results[0].page_content}\n"


# ----------------------------
# PROJECT SUGGESTION
# ----------------------------

def suggest_project():

    if not state.last_results:
        return "❌ Search a research area first."

    doc, _ = state.last_results[0]

    confirm = input(
        "Do you want to select this faculty? (yes/no): "
    )

    if confirm.lower() != "yes":
        return "Selection cancelled."

    return f"""
💡 Suggested Project

Based on:

{doc.page_content}

Project Ideas

• AI Application
• Dataset Analysis
• Deep Learning Model
• Real-world Research Prototype
"""


# ----------------------------
# COLLABORATION
# ----------------------------

def collaboration_match(query):

    topic = (
        query.lower()
        .replace("find collaboration in", "")
        .replace("collaborate in", "")
        .strip()
    )

    search_faculty(topic)

    if len(state.last_results) < 2:
        return "Not enough faculty found."

    doc1, _ = state.last_results[0]
    doc2, _ = state.last_results[1]

    return f"""
🤝 Collaboration Suggestion

Faculty 1

{doc1.page_content}

Faculty 2

{doc2.page_content}

Reason

Both faculty members work in {topic.upper()} and can collaborate.
"""


# ----------------------------
# GAP ANALYSIS
# ----------------------------

def gap_analysis():

    faculty_topics = []

    docs = db.similarity_search("", k=20)

    for doc in docs:

        for line in doc.page_content.split("\n"):

            if "Research Areas:" in line:

                areas = line.replace(
                    "Research Areas:",
                    ""
                ).split(",")

                faculty_topics.extend(
                    [a.strip() for a in areas]
                )

    faculty_topics = set(faculty_topics)

    trending = {
        "Agentic AI",
        "AI Safety",
        "Federated Learning",
        "Quantum ML",
        "Multimodal AI"
    }

    missing = trending - faculty_topics

    output = "📊 Missing Research Areas\n\n"

    for area in sorted(missing):
        output += f"• {area}\n"

    return output


# ----------------------------
# ROUTER
# ----------------------------

def agent_router(query):

    q = query.lower()

    # ---------------- Student ----------------

    if state.mode == "student":

        if (
            "trending" in q
            or "collaborate" in q
            or "missing" in q
            or "gap" in q
        ):

            return """
❌ Professor Mode Only

Please switch to Professor Mode.

Available there:

• Research Trends
• Collaboration
• Gap Analysis
"""

    # ---------------- Professor ----------------

    if state.mode == "professor":

        if "project" in q:

            return """
❌ Student Mode Only

Project suggestions are only available in Student Mode.
"""

    # ---------------- Routing ----------------

    if "who works on" in q:
        return search_faculty(
            q.replace("who works on", "").strip()
        )

    elif "tell me about" in q:
        return detail_lookup(query)

    elif "show me another" in q:
        return show_next()

    elif "project" in q:
        return suggest_project()

    elif "collaborate" in q:
        return collaboration_match(query)

    elif "trending" in q:
        return trend_search(query)

    elif "missing" in q or "gap" in q:
        return gap_analysis()

    else:
        return search_faculty(query)