# Practice 1 — Embeddings Fundamentals

## Goal

Learn the foundations of semantic AI systems using text embeddings and cosine similarity.

This practice focuses on:
- embeddings
- vector representations
- semantic similarity
- retrieval foundations

---

# Project Structure

```txt
practice-1-embeddings/
│
├── app/
│   ├── services/
│   │   ├── embedding_service.py
│   │   └── similarity_service.py
│   │
│   ├── utils/
│   │   └── cosine_similarity.py
│   │
│   └── main.py
│
├── data/
│   └── sample_texts.txt
│
├── requirements.txt
├── README.md
└── notes.md
```

---

# Concepts Learned

## 1. Embeddings

Embeddings transform text into numerical vectors that capture semantic meaning.

Texts with similar meanings produce similar vector representations.

---

## 2. Semantic Similarity

Two sentences can be semantically similar even if they use different words.

Example:

```txt
"AI is changing medicine"
"Artificial intelligence transforms healthcare"
```

Embeddings capture this relationship.

---

## 3. Cosine Similarity

Cosine similarity measures how close two vectors are.

Used heavily in:
- RAG systems
- vector databases
- semantic search
- recommendation systems

---

## 4. Embedding Models

Used SentenceTransformers to generate embeddings.

Model used:

```txt
all-MiniLM-L6-v2
```

---

# Why This Matters for AI Engineering

Embeddings are foundational for:
- Retrieval-Augmented Generation (RAG)
- vector databases
- semantic search
- AI memory systems
- recommendation engines

Modern AI systems rely heavily on embedding-based retrieval.

---

# Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app/main.py
```

---

# Example Output

```python
{
    'text1': 'Artificial intelligence is transforming healthcare.',
    'text2': 'AI is changing modern medicine.',
    'similarity_score': 0.7633265256881714
}
```

---

# Technologies Used

- SentenceTransformers
- NumPy
- Scikit-learn

---

# Future Improvements

- vector databases
- document chunking
- semantic search
- retrieval pipelines
- RAG systems