import numpy as np
from .stt import transcribe_audio
from .memory import add_transcript
from .reasoning import maybe_update_summary

AUDIO_BUFFER = []
SAMPLE_RATE = 48000   # LiveKit sends 48kHz audio
CHUNK_SECONDS = 3

def process_audio_frame(frame_event):
    """
    frame_event: AudioFrameEvent from LiveKit
    """

    # ✅ Extract raw PCM bytes correctly
    pcm_bytes = frame_event.frame.data

    # Convert bytes → int16 → float32
    pcm = np.frombuffer(pcm_bytes, dtype=np.int16).astype(np.float32) / 32768.0

    AUDIO_BUFFER.extend(pcm)

    if len(AUDIO_BUFFER) >= SAMPLE_RATE * CHUNK_SECONDS:
        audio_chunk = np.array(AUDIO_BUFFER[:SAMPLE_RATE * CHUNK_SECONDS])
        del AUDIO_BUFFER[:SAMPLE_RATE * CHUNK_SECONDS]

        text = transcribe_audio(audio_chunk)
        if text:
            print(" Transcript:", text)
            add_transcript(text)
            maybe_update_summary()
