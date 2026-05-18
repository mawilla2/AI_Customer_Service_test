from sqlalchemy import Column, Integer, String

from app.database import Base

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    user_message = Column(String)

    ai_reply = Column(String)