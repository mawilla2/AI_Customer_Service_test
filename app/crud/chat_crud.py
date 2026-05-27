from sqlalchemy.orm import Session

from app.models.chat_model import ChatHistory

def create_chat_history(
    db: Session,
    user_message: str,
    ai_reply: str,
    user_id: int
):

    chat = ChatHistory(
        user_message=user_message,
        ai_reply=ai_reply,
        user_id=user_id
    )

    db.add(chat)

    db.commit()

    db.refresh(chat)

    return chat

def get_chat_history(
    db: Session,
    user_id: int
):

    return db.query(ChatHistory).filter(
        ChatHistory.user_id == user_id
    ).all()
