from fastapi import FastAPI
from app.routers import chat
from app.database import engine
from app.models.chat_model import ChatHistory


app = FastAPI()



app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "AI Customer Service is running"}