from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import firebase_admin
from firebase_admin import credentials

# Initialize Firebase (mocked/structured for future use)
try:
    # Use default credentials or a mock for now
    firebase_admin.initialize_app()
    print("Firebase initialized successfully")
except Exception as e:
    # If it fails (e.g. no credentials), we print a warning but continue
    # so the app doesn't crash in mock mode.
    print(f"Warning: Firebase not initialized: {e}")

from .routers import auth, chat, ingest, tts, dashboard

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure static directory exists
os.makedirs("backend/static/audio", exist_ok=True)

# Mount static files for audio/images
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(ingest.router, prefix="/ingest")
app.include_router(tts.router, prefix="/tts")
app.include_router(dashboard.router, prefix="/dashboard")
