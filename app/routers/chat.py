from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    
    user_message = request.message

    # 伪AI逻辑（先简单写死）
    if "你好" in user_message:
        reply = "您好，请问有什么可以帮您？"
    else:
        reply = "抱歉，我暂时无法理解您的问题"

    return ChatResponse(reply=reply)