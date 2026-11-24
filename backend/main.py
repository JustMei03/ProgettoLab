from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Template progetto")
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


def genera_risposta(message: str) -> str:
    """Segnaposto: sostituisci questa funzione con la logica del tuo progetto."""
    return (
        f"Hai scritto: {message}\n\n"
        "Questa è una risposta segnaposto. Personalizza "
        "genera_risposta() in backend/main.py."
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    if not request.message.strip():
        return ChatResponse(response="Scrivi un messaggio per iniziare.")
    return ChatResponse(response=genera_risposta(request.message.strip()))


app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
