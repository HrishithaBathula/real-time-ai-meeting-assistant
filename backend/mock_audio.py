# backend/mock_audio.py

import asyncio
from backend.memory import add_transcript, update_summary

MOCK_SPEECH = [
    "Hello everyone, let's start the meeting.",
    "Today we are discussing the API design for the new service.",
    "The backend will be built using FastAPI.",
    "We agreed to use JWT authentication.",
    "Next steps include frontend integration and testing."
]

async def start_mock_audio_stream():
    for sentence in MOCK_SPEECH:
        await asyncio.sleep(3)
        print(f"🗣️ Mock speech: {sentence}")
        add_transcript(sentence)
        update_summary(sentence)
