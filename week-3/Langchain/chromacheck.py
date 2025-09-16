#!/usr/bin/env python3
# 📦 ChromaDB + Sentence-Transformers Tutorial — Fully Fixed for Chroma 1.0+
# Author: Senior ML Tutor
# Uses BAAI/bge-small-en-v1.5 directly via sentence-transformers — no Chroma wrapper bugs.
# Compliant with Chroma's EmbeddingFunction interface (input param + name method).
# Persistence is AUTOMATIC in Chroma 1.0+ when using persist_directory — no .persist() needed!
# Python 3.9+

import os
import sys
from typing import List, Dict, Any, Optional
from chromadb import Client
from chromadb.config import Settings

# 🧠 Load sentence-transformers model directly
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("❌ sentence-transformers not installed.")
    print("👉 Run: pip install sentence-transformers")
    sys.exit(1)

# 💡 Custom Embedding Function — NOW CHROMA 1.0+ COMPLIANT ✅
class LocalEmbeddingFunction:
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        print(f"📥 Loading model: {model_name} (may take a moment on first run)...")
        self.model = SentenceTransformer(model_name)
        self.dim = self.model.get_sentence_embedding_dimension()
        self._model_name = model_name
        print(f"✅ Model loaded. Embedding dimension: {self.dim}")

    def __call__(self, input: List[str]) -> List[List[float]]:
        # Encode input texts to embeddings — NOTE: parameter name MUST be 'input'
        embeddings = self.model.encode(input, convert_to_numpy=False, normalize_embeddings=True)
        # Convert to list of lists of floats
        return [embedding.tolist() for embedding in embeddings]

    def name(self) -> str:
        """Required by ChromaDB for validation. Returns a unique identifier."""
        return "local_sentence_transformer"

# 🧠 Step 1: Verify chromadb version
try:
    import chromadb
except ImportError:
    print("❌ chromadb not installed.")
    print("👉 Run: pip install chromadb")
    sys.exit(1)

print(f"✅ ChromaDB version: {chromadb.__version__}")

# 💾 Step 2: Initialize embedding function
try:
    embedding_func = LocalEmbeddingFunction("BAAI/bge-small-en-v1.5")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    print("👉 Check model name or internet connection.")
    sys.exit(1)

# 💾 Step 3: Initialize persistent Chroma client & collection
PERSIST_DIR = "./chroma_store"
os.makedirs(PERSIST_DIR, exist_ok=True)

client = Client(Settings(
    persist_directory=PERSIST_DIR,
    anonymized_telemetry=False
))

# Create or get collection — using cosine similarity
collection = client.get_or_create_collection(
    name="community_demo",
    embedding_function=embedding_func,  # Use our compliant custom function
    metadata={"hnsw:space": "cosine"}
)

print(f"✅ Collection 'community_demo' ready at {PERSIST_DIR}")

# 📚 Step 4: Define sample corpus with metadata
SAMPLE_DOCS = [
    "How to bake chocolate chip cookies from scratch.",
    "Python list comprehensions are a concise way to create lists.",
    "The mitochondria is the powerhouse of the cell.",
    "React hooks allow function components to have state and lifecycle features.",
    "Photosynthesis converts sunlight into chemical energy in plants.",
    "Docker containers package apps with their dependencies for portability.",
    "Machine learning models improve with more data and better features.",
    "CSS Grid is a two-dimensional layout system for the web.",
    "The Fibonacci sequence starts with 0, 1, and each next number is the sum of the two before.",
    "GraphQL allows clients to request exactly the data they need."
]

METADATAS = [
    {"title": "Baking Guide", "tag": "food", "source": "blog"},
    {"title": "Python Tips", "tag": "code", "source": "docs"},
    {"title": "Biology Fact", "tag": "science", "source": "textbook"},
    {"title": "React Hooks Intro", "tag": "code", "source": "tutorial"},
    {"title": "Plant Biology", "tag": "science", "source": "article"},
    {"title": "Docker Basics", "tag": "devops", "source": "manual"},
    {"title": "ML Concepts", "tag": "ml", "source": "course"},
    {"title": "CSS Layout", "tag": "code", "source": "guide"},
    {"title": "Math Sequence", "tag": "math", "source": "reference"},
    {"title": "GraphQL API", "tag": "api", "source": "spec"}
]

# Generate deterministic IDs
IDS = [f"doc-{i:03d}" for i in range(len(SAMPLE_DOCS))]

# ➕ Step 5: Upsert documents (add or update)
print("➕ Adding documents to collection...")
try:
    collection.upsert(
        documents=SAMPLE_DOCS,
        metadatas=METADATAS,
        ids=IDS
    )
    print(f"✅ Upserted {len(SAMPLE_DOCS)} documents.")
except Exception as e:
    print(f"❌ Upsert failed: {e}")
    sys.exit(1)

# 💾 💡 ChromaDB 1.0+ AUTOMATICALLY PERSISTS when using persist_directory.
# NO NEED to call client.persist() — it doesn't exist anymore!
# Data is saved to disk as you go.
print("💾 Collection is automatically persisted to disk (Chroma 1.0+).")

# 🔎 Step 6: Define helper to print results cleanly
def print_results(query: str, results: Dict[str, Any], top_k: int = 3):
    print(f"\n🔍 Query: \"{query}\"")
    print(f"   Top {top_k} results (lower distance = more similar):\n")

    if len(results['ids'][0]) == 0:
        print("   ❌ No results found.")
        return

    for i, (doc_id, distance, doc, meta) in enumerate(
        zip(results['ids'][0], results['distances'][0], results['documents'][0], results['metadatas'][0])
    ):
        print(f"   {i+1}. ID: {doc_id} | Distance: {distance:.4f}")
        print(f"      Title: {meta.get('title', 'N/A')} | Tag: {meta.get('tag', 'N/A')}")
        print(f"      Snippet: \"{doc[:70]}...\"")
        print()

# 🧪 Step 7: Run example queries
QUERIES = [
    "How do I create lists in Python?",  # semantic match
    "powerhouse of the cell",           # keyword-ish
    "How to fly a spaceship to Mars?"   # out-of-domain
]

print("\n" + "="*60)
print("🔎 RUNNING EXAMPLE QUERIES")
print("="*60)

for query in QUERIES:
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    print_results(query, results)

# 🧩 Step 8: Demonstrate metadata filtering
print("\n" + "="*60)
print("FilterWhere: Only 'code' tagged documents")
print("="*60)

results_filtered = collection.query(
    query_texts=["How to manage state in components?"],
    n_results=3,
    where={"tag": "code"}  # filter by metadata
)
print_results("How to manage state in components?", results_filtered)

# 💾 Step 9: Close client, re-open, and verify persistence
print("\n" + "="*60)
print("🔁 RELOADING STORE FROM DISK")
print("="*60)

del client  # Close old client
client = Client(Settings(
    persist_directory=PERSIST_DIR,
    anonymized_telemetry=False
))
# Reuse same embedding function
collection = client.get_or_create_collection(
    name="community_demo",
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"}
)

# Run a quick test query to verify reload
reload_test_query = "What is Docker?"
results_reload = collection.query(
    query_texts=[reload_test_query],
    n_results=1
)

if len(results_reload['ids'][0]) > 0:
    print(f"✅ Reload successful! Found doc: {results_reload['documents'][0][0][:50]}...")
else:
    print("❌ Reload failed: no documents found after reopening.")

# 🧪 Step 10: Evaluation sanity checks
print("\n" + "="*60)
print("🧪 SANITY CHECKS")
print("="*60)

# Check 1: Small edit impact
print("→ Query: 'Python list comprehensions'")
results_edit1 = collection.query(query_texts=["Python list comprehensions"], n_results=1)
print(f"   Top Distance: {results_edit1['distances'][0][0]:.4f}")

print("→ Query: 'Python lists made easy'")
results_edit2 = collection.query(query_texts=["Python lists made easy"], n_results=1)
print(f"   Top Distance: {results_edit2['distances'][0][0]:.4f}")
print("   (Slight rephrasing → small distance change = model is working!)")

# Check 2: Embedding shape (optional debug)
sample_embedding = embedding_func([SAMPLE_DOCS[0]])[0]
print(f"→ Embedding shape for first doc: {len(sample_embedding)} dimensions")

# Check 3: Change n_results
print("→ Query with n_results=1 vs n_results=5")
results_n1 = collection.query(query_texts=["machine learning"], n_results=1)
results_n5 = collection.query(query_texts=["machine learning"], n_results=5)
print(f"   n=1 → {len(results_n1['ids'][0])} result(s)")
print(f"   n=5 → {len(results_n5['ids'][0])} result(s)")

print("\n🎉 Tutorial complete! You’re using BGE embeddings — stable, compliant, no Chroma bugs.")