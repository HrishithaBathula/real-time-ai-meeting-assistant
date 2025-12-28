# # backend/memory.py

# from collections import deque
# import time

# TRANSCRIPT_BUFFER = deque(maxlen=100)

# SUMMARY_STATE = {
#     "summary": "",
#     "last_updated": 0
# }

# DECISIONS = deque(maxlen=20)

# def add_transcript(text: str):
#     TRANSCRIPT_BUFFER.append(text)

# def get_full_transcript():
#     return "\n".join(TRANSCRIPT_BUFFER)

# def update_summary(summary: str):
#     SUMMARY_STATE["summary"] = summary
#     SUMMARY_STATE["last_updated"] = time.time()

# def get_summary():
#     return SUMMARY_STATE["summary"]

# def add_decision(text: str):
#     DECISIONS.append(text)

# def get_decisions():
#     return list(DECISIONS)


#MOCK

# backend/memory.py

TRANSCRIPTS = []
SUMMARY_POINTS = []

def add_transcript(text: str):
    TRANSCRIPTS.append(text)

def get_full_transcript():
    return "\n".join(TRANSCRIPTS)

def update_summary(text: str):
    """
    Very simple heuristic summary:
    Adds important decisions / facts only
    """
    lowered = text.lower()

    if "fastapi" in lowered and "fastapi backend" not in SUMMARY_POINTS:
        SUMMARY_POINTS.append("FastAPI selected for backend")

    if "jwt" in lowered and "jwt authentication" not in SUMMARY_POINTS:
        SUMMARY_POINTS.append("JWT authentication decided")

    if "next steps" in lowered and "frontend integration" not in SUMMARY_POINTS:
        SUMMARY_POINTS.append("Frontend integration planned")

def get_summary():
    return "\n• ".join([""] + SUMMARY_POINTS) if SUMMARY_POINTS else ""
