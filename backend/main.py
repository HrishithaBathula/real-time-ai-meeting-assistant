# # backend/main.py

# from fastapi import FastAPI
# import asyncio
# from pydantic import BaseModel
# import openai
# import os

# from .livekit_client import start_ai_assistant
# from .memory import get_full_transcript, get_summary, get_decisions

# openai.api_key = os.getenv("OPENAI_API_KEY")

# app = FastAPI(title="Real-Time AI Meeting Assistant")

# @app.on_event("startup")
# async def startup_event():
#     asyncio.create_task(start_ai_assistant())

# @app.get("/")
# def health():
#     return {"status": "AI Meeting Assistant Running"}

# @app.get("/transcript")
# def transcript():
#     return {"text": get_full_transcript()}

# @app.get("/summary")
# def summary():
#     return {
#         "summary": get_summary(),
#         "decisions": get_decisions()
#     }

# class Question(BaseModel):
#     question: str

# @app.post("/ask")
# def ask(q: Question):
#     context = get_summary()

#     prompt = f"""
# You are a meeting assistant.

# Context:
# {context}

# Answer clearly:
# {q.question}
# """

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.2
#     )

#     return {"answer": response.choices[0].message["content"]}


#MOCK

# backend/main.py

from fastapi import FastAPI
import asyncio
from fastapi.middleware.cors import CORSMiddleware

from backend.memory import get_full_transcript, get_summary
from backend.mock_audio import start_mock_audio_stream
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI(title="Real-Time AI Meeting Assistant (Mock Audio)")

# ✅ REQUIRED: CORS for frontend (5500) → backend (8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    asyncio.create_task(start_mock_audio_stream())

@app.get("/")
def health():
    return {"status": "running"}

@app.get("/transcript")
def transcript():
    return {"text": get_full_transcript()}

@app.get("/summary")
def summary():
    return {"summary": get_summary()}

model = SentenceTransformer("all-MiniLM-L6-v2")

@app.post("/ask")
def ask(payload: dict):
    question = payload.get("question", "").strip()

    if not question:
        return {"answer": "Please ask a question."}

    transcript = get_full_transcript()
    summary = get_summary()

    context_text = transcript + "\n" + summary

    if not context_text.strip():
        return {"answer": "No meeting information available yet."}

    # Split into semantic chunks
    sentences = [s.strip() for s in context_text.split("\n") if s.strip()]

    # Generate embeddings
    sentence_embeddings = model.encode(sentences)
    question_embedding = model.encode([question])

    similarities = cosine_similarity(
        question_embedding,
        sentence_embeddings
    )[0]

    best_idx = int(np.argmax(similarities))
    best_score = similarities[best_idx]

    # Confidence threshold
    if best_score < 0.45:
        return {"answer": "I don't have enough information to answer that yet."}

    return {"answer": sentences[best_idx]}