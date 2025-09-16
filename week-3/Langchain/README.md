
# 🧠 ChromaDB + Sentence-Transformers: Local Semantic Search Tutorial

> ✅ **No API keys • No cloud • 100% offline • Beginner-friendly • ChromaDB 1.0+ Compliant**

A self-contained, educational Python script that demonstrates how to build a persistent local vector store using **ChromaDB** and **Hugging Face’s BGE sentence-transformer embeddings** — perfect for learning, prototyping, or lightweight production use.

Built to handle all breaking changes in ChromaDB 1.0+, including:
- Removal of `client.persist()`
- Mandatory `input` parameter in embedding functions
- Requirement for `.name()` method
- Bypassing broken `HuggingFaceEmbeddingFunction` wrapper

---

## 🚀 Features

- 📦 Creates a **persistent ChromaDB collection** saved to `./chroma_store`
- 🧠 Uses **`BAAI/bge-small-en-v1.5`** — a state-of-the-art, lightweight embedding model (better than `all-MiniLM-L6-v2`)
- ➕ **Upserts 10 sample documents** with rich metadata (`title`, `tag`, `source`) and deterministic IDs
- 🔍 Runs **3 semantic search queries** + **1 metadata-filtered query**
- 🔄 **Reloads the collection from disk** to prove persistence works
- 🧪 Includes **sanity checks** (embedding shape, query variations, top-k control)
- 🧑‍🏫 **Fully commented** with clear section headers and error handling
- ❌ **No OpenAI, no API keys, no credentials required**

---

## 🛠️ Requirements

- Python 3.9+
- `pip install chromadb sentence-transformers`

> 💡 First run will download the BGE model (~100MB). Subsequent runs are fast and offline.

---

## ▶️ Quick Start

1. Clone or download this repo.
2. Install dependencies:

```bash
pip install chromadb sentence-transformers
```

3. Run the script:

```bash
python chroma_local_search.py
```

4. Watch it:
   - Download the embedding model (once)
   - Create and populate the vector store
   - Run semantic queries
   - Reload from disk to prove persistence

---

## 📄 Sample Output

```
✅ ChromaDB version: 1.0.21
📥 Loading model: BAAI/bge-small-en-v1.5 (may take a moment on first run)...
✅ Model loaded. Embedding dimension: 384
✅ Collection 'community_demo' ready at ./chroma_store
➕ Adding documents to collection...
✅ Upserted 10 documents.
💾 Collection is automatically persisted to disk (Chroma 1.0+).

============================================================
🔎 RUNNING EXAMPLE QUERIES
============================================================

🔍 Query: "How do I create lists in Python?"
   Top 3 results (lower distance = more similar):

   1. ID: doc-001 | Distance: 0.1824
      Title: Python Tips | Tag: code
      Snippet: "Python list comprehensions are a concise way to create lists..."

🔍 Query: "powerhouse of the cell"
   Top 3 results (lower distance = more similar):

   1. ID: doc-002 | Distance: 0.1201
      Title: Biology Fact | Tag: science
      Snippet: "The mitochondria is the powerhouse of the cell..."

============================================================
FilterWhere: Only 'code' tagged documents
============================================================

🔍 Query: "How to manage state in components?"
   Top 3 results (lower distance = more similar):

   1. ID: doc-003 | Distance: 0.2915
      Title: React Hooks Intro | Tag: code
      Snippet: "React hooks allow function components to have state and lifecycle features..."

============================================================
🔁 RELOADING STORE FROM DISK
============================================================
✅ Reload successful! Found doc: Docker containers package apps with their...

🎉 Tutorial complete! You’re using BGE embeddings — stable, compliant, no Chroma bugs.
```

*(Distances may vary slightly due to model updates, but rankings should be stable.)*

---

## 🧩 Try This Next

- 🔄 **Swap the model**: Try `"BAAI/bge-base-en-v1.5"` or `"thenlper/gte-small"` for different performance/accuracy trade-offs.
- 📖 **Expand the corpus**: Add your own documents to `SAMPLE_DOCS` and `METADATAS`.
- 🎯 **Filter differently**: Query with `where={"source": "tutorial"}` or combine filters: `where={"$and": [{"tag": "code"}, {"source": "guide"}]}`
- 📊 **Inspect embeddings**: Uncomment `print(f"→ Embedding: {embedding_func(['test'])[0][:5]}...")` to see raw vectors.
- 🗑️ **Reset the store**: Delete the `./chroma_store` folder to start fresh.

---

## 🛠️ Troubleshooting

- ❌ `ModuleNotFoundError` → Run `pip install chromadb sentence-transformers`
- ❌ `OSError: Unable to load weights` → Check internet — first run downloads model.
- ❌ `ValueError: Expected EmbeddingFunction.__call__...` → Ensure your `__call__` method uses `input: List[str]`, not `texts`.
- ❌ `AttributeError: 'Client' object has no attribute 'persist'` → You’re on Chroma 1.0+ — persistence is automatic. Delete the `.persist()` call.
- ❌ `sqlite3.OperationalError: database is locked` → Another process is using the DB. Close other scripts or reboot.
- 🐢 *First query is slow?* → Normal! Model loads and indexes on first use.

---

## 📁 Project Structure

```
.
├── README.md                 # You are here!
├── chroma_local_search.py    # The main runnable script
└── chroma_store/             # Auto-created persistent database (after first run)
```

---

## 📚 Learn More

- [ChromaDB Official Docs](https://docs.trychroma.com/)
- [Sentence-Transformers Documentation](https://www.sbert.net/)
- [BGE Model Card (Hugging Face)](https://huggingface.co/BAAI/bge-small-en-v1.5)

---

## 🙌 Acknowledgements

Inspired by the ChromaDB community and Hugging Face’s amazing open-source models. Built to empower beginners and tinkerers.

---

## 📜 License

MIT — Do whatever you want with it. Share, learn, build!

---
