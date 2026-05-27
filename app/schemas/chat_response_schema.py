from pydantic import BaseModel

class ChatHistoryResponse(BaseModel):

    id: int

    user_message: str

    ai_reply: str

    class Config:
        from_attributes = True