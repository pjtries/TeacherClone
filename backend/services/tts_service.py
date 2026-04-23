import os
import torch
import uuid
from TTS.api import TTS
from abc import ABC, abstractmethod

# Path configuration
VOICE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "voices")
AUDIO_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "audio")
REFERENCE_VOICE = os.path.join(VOICE_DIR, "teacher.wav")

# Ensure directories exist
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)

class TTSServiceInterface(ABC):
    @abstractmethod
    def generate_audio(self, text: str) -> str:
        pass

class CoquiTTSService(TTSServiceInterface):
    def __init__(self):
        # Load Coqui model once
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Loading Coqui TTS model (XTTS-v2) on {self.device}...")
        
        # Agree to Coqui TOS (required for XTTS-v2)
        os.environ["COQUI_TOS_AGREED"] = "1"
        
        try:
            self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
            print("TTS Model loaded successfully.")
        except Exception as e:
            print(f"Error loading TTS model: {e}")
            self.tts = None

    def generate_audio(self, text: str) -> str:
        """
        Generate a real audio file using Coqui TTS.
        """
        if not self.tts:
            raise RuntimeError("TTS model is not loaded.")

        if not os.path.exists(REFERENCE_VOICE):
            raise FileNotFoundError(f"Reference voice file not found at {REFERENCE_VOICE}. Please provide a teacher.wav file.")

        # Generate unique filename
        filename = f"{uuid.uuid4()}.wav"
        output_path = os.path.join(AUDIO_OUTPUT_DIR, filename)

        # Generate audio
        self.tts.tts_to_file(
            text=text,
            speaker_wav=REFERENCE_VOICE,
            language="en",
            file_path=output_path
        )

        return output_path

# Global instance for service injection
tts_service = CoquiTTSService()
