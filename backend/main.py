from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    response_text = f"Вы сказали: {message.text}"
    return {"response": response_text}
