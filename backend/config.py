import os
from dotenv import load_dotenv

load_dotenv()

LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
LIVEKIT_URL = os.getenv("LIVEKIT_URL")

AUDIO_SAMPLE_RATE = 16000
AUDIO_CHUNK_SECONDS = 3  # Trade-off: latency vs accuracy
