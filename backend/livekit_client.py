from livekit import rtc
from livekit.api import AccessToken, VideoGrants
from .config import LIVEKIT_API_KEY, LIVEKIT_API_SECRET, LIVEKIT_URL
from .audio_processor import process_audio_frame
import asyncio

async def start_ai_assistant():
    room = rtc.Room()

    @room.on("track_subscribed")
    def on_track(track, publication, participant):
        if track.kind == rtc.TrackKind.KIND_AUDIO:
            print(f" Subscribed to audio from {participant.identity}")

            audio_stream = rtc.AudioStream(track)

            async def read_audio():
                async for frame_event in audio_stream:
                    process_audio_frame(frame_event)

            asyncio.create_task(read_audio())

    token = (
        AccessToken(LIVEKIT_API_KEY, LIVEKIT_API_SECRET)
        .with_identity("ai-assistant")
        .with_name("AI Assistant")
        .with_grants(
            VideoGrants(
                room_join=True,
                room="demo-room"
            )
        )
        .to_jwt()
    )

    print(" AI Assistant joining room: demo-room")
    await room.connect(LIVEKIT_URL, token)
