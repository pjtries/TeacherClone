class TTSService:
    """Service to handle text-to-speech logic."""

    @staticmethod
    def generate_speech(text: str) -> dict:
        """
        Simulates speech generation.
        Later this can integrate with OpenAI TTS, ElevenLabs, or local Coqui TTS.
        """
        # Mock logic: simply pretending to save it to a public URL
        return {
            "audio_url": f"/static/audio/mock_{hash(text)}.wav"
        }

tts_service = TTSService()
