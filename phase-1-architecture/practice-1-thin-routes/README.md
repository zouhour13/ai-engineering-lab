# Practice 1 — Thin Routes Architecture

## Goal

Learn how to build a clean backend architecture using FastAPI by separating:

- API routes
- business logic
- data validation

This practice focuses on the Thin Routes pattern and Service Layer architecture.

---

# Project Structure

```txt
practice-1-thin-routes/
│
├── app/
│   ├── api/
│   │   └── chat.py
│   │
│   ├── services/
│   │   └── chat_service.py
│   │
│   ├── schemas/
│   │   └── chat_schema.py
│   │
│   └── main.py
│
├── requirements.txt
├── README.md
└── notes.md
```

---

# Architecture

```txt
Client
   ↓
Route Layer (API)
   ↓
Service Layer
   ↓
Response
```

---

# Concepts Learned

## 1. Thin Routes

Routes should:
- receive HTTP requests
- call services
- return responses

Routes should NOT:
- contain business logic
- manipulate complex data
- orchestrate AI workflows

---

## 2. Service Layer Architecture

Business logic belongs inside services.

Benefits:
- reusable logic
- cleaner codebase
- easier testing
- scalable architecture

---

## 3. Pydantic Schemas

Used request and response models for:
- validation
- typed APIs
- structured responses

Example:

```python
class ChatRequest(BaseModel):
    message: str
```

---

## 4. Response Models

Implemented FastAPI response models:

```python
@router.post("/chat", response_model=ChatResponse)
```

Benefits:
- automatic validation
- structured API responses
- predictable output format

---

## 5. Error Handling

Implemented structured exception handling using:

- `ValueError`
- `HTTPException`

Example:

```python
if not message.strip():
    raise ValueError("Message cannot be empty")
```

Benefits:
- prevents crashes
- improves API reliability
- returns meaningful error responses

---

# Key Backend Insight

Professional backend systems are designed to:
- handle success
- handle failure gracefully

not only success.

---

# Why This Matters for AI Engineering

Thin routes improve scalability and maintainability because routes only handle HTTP communication while services contain the business logic.

Separating services from routes creates modular architecture that is easier to test, debug, and extend.

Later, RAG pipelines and AI orchestration should live inside services because they involve complex logic such as:
- retrieval
- embeddings
- vector databases
- LLM interaction

This architecture scales better than one-file systems because responsibilities are isolated into dedicated layers.

This architecture prepares for:
- LLM integrations
- RAG pipelines
- AI agents
- tool orchestration
- scalable AI APIs

Because future AI logic will belong inside services, not routes.


# Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start server:

```bash
uvicorn app.main:app --reload
```

---

# Example Request

POST `/chat`

```json
{
  "message": "Hello AI Engineering"
}
```

---

# Example Response

```json
{
  "original": "Hello AI Engineering",
  "lowercase": "hello ai engineering",
  "word_count": 3
}
```

---

# Technologies Used

- FastAPI
- Pydantic
- Uvicorn
- Async Python

---

# Future Improvements

- dependency injection
- logging
- middleware
- database integration
- LLM service integration
- LangChain architecture