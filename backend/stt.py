import whisper
import tempfile
import soundfile as sf

model = whisper.load_model("base")

def transcribe_audio(audio_pcm, sample_rate=16000):
    """
    audio_pcm: numpy array (float32)
    """
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        sf.write(tmp.name, audio_pcm, sample_rate)
        result = model.transcribe(tmp.name)
        return result["text"].strip()
