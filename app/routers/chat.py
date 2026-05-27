from app.core.dependencies import (
    get_db,
    get_current_user
)
from app.crud.chat_crud import create_chat_history, get_chat_history
from app.models.user_model import User
from app.schemas.chat_response_schema import ChatHistoryResponse
from app.schemas.chat_schema import ChatRequest
from app.services.chat_service import generate_ai_reply
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    reply = generate_ai_reply(request.message)

    create_chat_history(
        db=db,
        user_message=request.message,
        ai_reply=reply,
        user_id=current_user.id
    )

    return {
        "reply": reply
    }

@router.get(
    "/chat/history",
    response_model=list[ChatHistoryResponse]
)
def read_chat_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    history = get_chat_history(db, current_user.id)

    return history
