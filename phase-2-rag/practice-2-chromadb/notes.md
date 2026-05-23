# What I Learned

---

# 1. Embeddings

Embeddings are numerical vector representations of text.

They capture:
- semantic meaning
- contextual relationships
- language patterns

Texts with similar meanings produce vectors that are close in vector space.

---

# 2. Semantic Search

Traditional keyword search relies on exact words.

Embedding-based search relies on meaning.

This enables:
- smarter retrieval
- contextual matching
- semantic understanding

---

# 3. Cosine Similarity

Cosine similarity measures vector similarity.

Higher similarity score:
→ more semantically related texts

This metric is foundational in:
- RAG
- vector search
- retrieval systems

---

# 4. Embedding Models

SentenceTransformers generate embeddings using pretrained transformer models.

Model used:

```txt
all-MiniLM-L6-v2
```

---

# 5. Retrieval Foundations

Embeddings are the foundation of:
- vector databases
- semantic retrieval
- AI memory
- document search
- recommendation systems

---

# AI Engineering Insight

Modern AI systems do not retrieve information using keywords only.

They retrieve information using semantic similarity between embeddings.

This is the core mechanism behind RAG systems.