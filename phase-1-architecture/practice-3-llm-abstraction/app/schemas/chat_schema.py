from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    original: str
    processed: str
    llm_response: str
    word_count: int