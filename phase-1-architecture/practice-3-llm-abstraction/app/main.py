from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
    title="LLM Abstraction Practice",
    description="Practice 3 — AI Engineering Architecture",
    version="1.0.0"
)

app.include_router(chat_router)


@app.get("/")
async def root():
    return {"message": "LLM Abstraction API Running"}