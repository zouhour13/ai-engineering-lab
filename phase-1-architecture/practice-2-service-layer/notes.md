# What I Learned

---

# 1. Service Layer Architecture

Business logic should be separated from routes.

Routes should:
- receive requests
- call services
- return responses

Services should:
- contain application logic
- process data
- coordinate workflows

---

# 2. Service Composition

Instead of placing all logic inside one service, logic can be divided into multiple focused services.

Example:

```txt
validation_service.py
text_service.py
chat_service.py
```

This creates modular architecture.

---

# 3. Orchestration

The chat service acts as an orchestrator.

It coordinates:
- validation
- processing
- response generation

Example flow:

```txt
Route
 ↓
Chat Service
 ↓
Validation Service
 ↓
Text Service
```

---

# 4. Single Responsibility Principle

Each service should have one responsibility.

Benefits:
- cleaner architecture
- easier testing
- reusable logic
- simpler debugging

---

# 5. Modular Backend Design

Large systems become easier to scale when logic is isolated into layers and services.

Problems with monolithic architecture:
- duplicated logic
- difficult maintenance
- poor readability
- tightly coupled code

---

# 6. Error Handling Across Services

Validation errors should originate from services.

Routes should convert exceptions into HTTP responses.

Example:

```python
raise ValueError("Message cannot be empty")
```

This keeps business validation centralized.

---

# 7. AI Engineering Insight

Future AI systems will contain many specialized services such as:

```txt
embedding_service.py
retrieval_service.py
memory_service.py
llm_service.py
tool_service.py
```

The orchestration layer will coordinate these components.

This practice prepares for scalable AI architecture.

---

# Key Insight

Large systems remain maintainable when responsibilities are separated into dedicated services instead of centralized in one file.