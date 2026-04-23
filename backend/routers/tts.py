from fastapi import APIRouter
from ..schemas.tts_schema import TTSRequest, TTSResponse
from ..services.tts_service import tts_service

router = APIRouter()


@router.post("/speak", response_model=TTSResponse)
def speak(request: TTSRequest):
    """
    Simulates Text-to-Speech generation.
    Delegates to TTSService.
    """
    return tts_service.generate_speech(request.text)
