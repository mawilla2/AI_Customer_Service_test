from fastapi import FastAPI
from app.routers import chat

app = FastAPI()

app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "AI Customer Service is running"}