# Rilevatore di sarcasmo

Scheletro del progetto: frontend in HTML e JavaScript puro collegato a un
backend Python/FastAPI. Per ora il backend non analizza nulla: la logica va
scritta nella funzione `analizza()` di `backend/main.py`.

## Struttura

```text
ProgettoLab/
├── backend/
│   ├── main.py            # API: GET /health e POST /api/chat
│   └── requirements.txt
└── frontend/
    ├── index.html         # pagina
    ├── api.js             # collegamento con il backend (fetch)
    └── app.js             # gestione della chat
```

## Avvio

Apri un terminale dalla cartella `ProgettoLab`.

Nel terminale, crea e attiva un ambiente Python, installa le dipendenze e avvia
il backend:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python -m uvicorn main:app --reload --app-dir backend --port 8000
```

Su Windows, attiva l'ambiente con:

```powershell
.venv\Scripts\Activate.ps1
```

Lascia il backend in esecuzione e apri http://localhost:8000 nel browser.
La stessa app serve sia la pagina sia l'API; per controllare il backend,
visita http://localhost:8000/health.

## Connessione frontend ↔ backend

- `GET /health` → `{"status": "ok"}`
- `POST /api/chat` con `{"message": "...", "context": "..." | null}`
  → `{"response": "...", "sarcastico": true | false | null, "probabilita": 0.0-1.0 | null}`

`context` è il messaggio a cui l'utente risponde (facoltativo).
