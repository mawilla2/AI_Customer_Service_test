from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Customer Service is running"}