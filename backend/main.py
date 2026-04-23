from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(ingest.router, prefix="/ingest")
app.include_router(tts.router, prefix="/tts")
app.include_router(dashboard.router, prefix="/dashboard")
