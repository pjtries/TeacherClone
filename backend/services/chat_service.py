import httpx
import json
from openai import OpenAI
from ..config import settings

class ChatService:
    """Service to handle chat logic using either OpenAI or Ollama."""

    def __init__(self):
        self.openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.ollama_url = f"{settings.OLLAMA_BASE_URL}/api/chat"
        self.use_ollama = True  # Set to True to use local Ollama by default

    def generate_answer(self, question: str) -> dict:
        """
        Generates an answer using the configured provider.
        """
        if self.use_ollama:
            return self._generate_with_ollama(question)
        else:
            return self._generate_with_openai(question)

    def _generate_with_ollama(self, question: str) -> dict:
        """
        Generates an answer using the local Ollama instance.
        """
        try:
            payload = {
                "model": settings.OLLAMA_MODEL,
                "messages": [
                    {"role": "system", "content": "You are a helpful teaching assistant named TeacherClone. Provide clear, concise explanations for students."},
                    {"role": "user", "content": question}
                ],
                "stream": False
            }
            
            with httpx.Client(timeout=30.0) as client:
                response = client.post(self.ollama_url, json=payload)
                response.raise_for_status()
                data = response.json()
                
            answer = data["message"]["content"]
            
            return {
                "answer": answer,
                "source": f"Ollama ({settings.OLLAMA_MODEL})",
                "confidence": 0.9
            }
        except Exception as e:
            print(f"Ollama Error: {e}. Falling back to OpenAI...")
            # Fallback to OpenAI if Ollama fails
            return self._generate_with_openai(question)

    def _generate_with_openai(self, question: str) -> dict:
        """
        Generates an answer using OpenAI's GPT-4o model.
        """
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful teaching assistant named TeacherClone. Provide clear, concise explanations for students."},
                    {"role": "user", "content": question}
                ],
                temperature=0.7
            )

            answer = response.choices[0].message.content
            
            return {
                "answer": answer,
                "source": "OpenAI GPT-4o",
                "confidence": 0.95
            }
        except Exception as e:
            print(f"OpenAI Error: {e}")
            return {
                "answer": f"I encountered an error while processing your request: {e}",
                "source": "Error System",
                "confidence": 0.0
            }

chat_service = ChatService()
