# # backend/reasoning.py

# import time
# import os
# import openai
# from .memory import get_full_transcript, update_summary, add_decision

# openai.api_key = os.getenv("OPENAI_API_KEY")

# SUMMARY_INTERVAL = 20  # seconds
# _last_run = 0

# def maybe_update_summary():
#     global _last_run

#     now = time.time()
#     if now - _last_run < SUMMARY_INTERVAL:
#         return

#     transcript = get_full_transcript()
#     if not transcript.strip():
#         return

#     prompt = f"""
# You are a real-time AI meeting assistant.

# Conversation so far:
# {transcript}

# Tasks:
# 1. Provide a concise summary (max 4 bullet points)
# 2. List any decisions made (if any)
# """

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.3
#         )

#         content = response.choices[0].message["content"]
#         update_summary(content)

#         for line in content.split("\n"):
#             if "decision" in line.lower() or "decided" in line.lower():
#                 add_decision(line.strip())

#         _last_run = now

#     except Exception as e:
#         print("⚠️ Summary update failed:", e)


#MOCK

from .memory import get_full_transcript, set_summary

def maybe_update_summary():
    transcript = get_full_transcript()
    if not transcript.strip():
        return

    # Simple evolving summary logic
    lines = transcript.split(".")
    important = lines[-3:] if len(lines) >= 3 else lines

    summary = "Meeting Summary:\n"
    for line in important:
        if line.strip():
            summary += f"- {line.strip()}\n"

    set_summary(summary)
