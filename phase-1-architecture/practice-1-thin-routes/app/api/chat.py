
from fastapi import APIRouter, HTTPException
from app.services.chat_service import generate_response
from app.schemas.chat_schema import ChatRequest, ChatResponse

router = APIRouter()

   
@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):#receives input

    try:
        response = await generate_response(request.message)
        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))




   