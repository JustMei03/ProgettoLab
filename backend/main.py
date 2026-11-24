from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Rilevatore di sarcasmo")
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

# Permette al frontend di chiamare il backend anche se è aperto da un altro
# server locale (es. Live Server su :5500). Con http://localhost:8000 non serve.
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


# Formato dei dati scambiati con il frontend
class ChatRequest(BaseModel):
    message: str
    context: str | None = None  # messaggio a cui l'utente risponde (facoltativo)


class ChatResponse(BaseModel):
    response: str
    sarcastico: bool | None = None
    probabilita: float | None = None


def analizza(message: str, context: str | None) -> ChatResponse:
    """TODO: qui va il modello che rileva il sarcasmo."""
    return ChatResponse(response=f"Ho ricevuto: {message}")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    return analizza(request.message.strip(), request.context)


app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
