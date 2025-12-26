# backend/memory.py

from collections import deque
import time

TRANSCRIPT_BUFFER = deque(maxlen=100)

SUMMARY_STATE = {
    "summary": "",
    "last_updated": 0
}

DECISIONS = deque(maxlen=20)

def add_transcript(text: str):
    TRANSCRIPT_BUFFER.append(text)

def get_full_transcript():
    return "\n".join(TRANSCRIPT_BUFFER)

def update_summary(summary: str):
    SUMMARY_STATE["summary"] = summary
    SUMMARY_STATE["last_updated"] = time.time()

def get_summary():
    return SUMMARY_STATE["summary"]

def add_decision(text: str):
    DECISIONS.append(text)

def get_decisions():
    return list(DECISIONS)
