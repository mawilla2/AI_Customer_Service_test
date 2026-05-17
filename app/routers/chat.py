from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import  generate_ai_reply

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    
    reply = generate_ai_reply(request.message)

    return ChatResponse(reply=reply)