from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.chat_schema import ChatRequest
from app.services.chat_service import generate_ai_reply

from app.dependencies import get_db
from app.crud.chat_crud import create_chat_history

router = APIRouter()

@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    reply = generate_ai_reply(request.message)

    create_chat_history(
        db=db,
        user_message=request.message,
        ai_reply=reply
    )

    return {
        "reply": reply
    }