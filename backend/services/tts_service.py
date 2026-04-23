import os
import uuid
from openai import OpenAI
from ..config import settings

class TTSService:
    """Service to handle text-to-speech logic using OpenAI."""

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.audio_dir = "backend/static/audio"
        os.makedirs(self.audio_dir, exist_ok=True)

    def generate_speech(self, text: str) -> dict:
        """
        Generates speech using OpenAI's TTS-1 model.
        Saves the audio file locally and returns the URL.
        """
        try:
            filename = f"speech_{uuid.uuid4().hex}.mp3"
            filepath = os.path.join(self.audio_dir, filename)

            # Call OpenAI TTS
            response = self.client.audio.speech.create(
                model="tts-1",
                voice="alloy",
                input=text
            )

            # Save the file
            response.stream_to_file(filepath)

            # Return the static URL
            # Note: In production, you'd use a full URL or cloud storage
            return {
                "audio_url": f"/static/audio/{filename}"
            }
        except Exception as e:
            print(f"Error in TTS generation: {e}")
            # Fallback to mock behavior if API fails
            return {
                "audio_url": f"/static/audio/error_fallback.wav",
                "error": str(e)
            }

tts_service = TTSService()
