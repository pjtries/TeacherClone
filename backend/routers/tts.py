from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from ..schemas.tts_schema import TTSRequest
from ..services.tts_service import tts_service
import os

router = APIRouter()

@router.post("/speak")
async def speak(request: TTSRequest):
    """
    Endpoint to convert text to speech using a real Coqui TTS model.
    Returns the generated WAV file directly.
    """
    try:
        # Generate the audio file
        file_path = tts_service.generate_audio(request.text)
        
        # Check if file was actually created
        if not os.path.exists(file_path):
            raise HTTPException(status_code=500, detail="Audio generation failed.")

        # Return the file as a response
        return FileResponse(
            path=file_path,
            media_type="audio/wav",
            filename=os.path.basename(file_path)
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
