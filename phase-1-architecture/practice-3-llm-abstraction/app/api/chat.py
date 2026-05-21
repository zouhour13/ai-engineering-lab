from fastapi import APIRouter, HTTPException

from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import generate_chat_response

router = APIRouter(prefix="/api")


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:
        response = await generate_chat_response(request.message)
        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))