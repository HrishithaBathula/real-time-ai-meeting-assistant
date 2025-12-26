# backend/main.py

from fastapi import FastAPI
import asyncio
from pydantic import BaseModel
import openai
import os

from .livekit_client import start_ai_assistant
from .memory import get_full_transcript, get_summary, get_decisions

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Real-Time AI Meeting Assistant")

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_ai_assistant())

@app.get("/")
def health():
    return {"status": "AI Meeting Assistant Running"}

@app.get("/transcript")
def transcript():
    return {"text": get_full_transcript()}

@app.get("/summary")
def summary():
    return {
        "summary": get_summary(),
        "decisions": get_decisions()
    }

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Question):
    context = get_summary()

    prompt = f"""
You are a meeting assistant.

Context:
{context}

Answer clearly:
{q.question}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return {"answer": response.choices[0].message["content"]}
