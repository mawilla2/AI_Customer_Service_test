from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.database import Base


class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    user_message = Column(Text)

    ai_reply = Column(Text)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship("User")
