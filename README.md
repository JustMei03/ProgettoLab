# Template progetto

Starter minimale per un progetto di interfacce linguistiche: una chat web
collegata a un backend Python/FastAPI. Copia questa cartella per iniziare un
nuovo progetto e personalizza il frontend e la funzione `genera_risposta`.
Non serve installare Node.js o npm.

## Struttura

```text
template-progetto/
├── backend/
│   ├── main.py
│   └── requirements.txt
└── frontend/
    └── index.html
```

## Avvio

Apri un terminale dalla cartella `template-progetto`.

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

## Personalizzazione

- Cambia titolo, testi, stile e comportamento della chat in
  `frontend/index.html`.
- Modifica `genera_risposta()` in `backend/main.py` per implementare il
  comportamento linguistico del progetto.
- La richiesta inviata dal frontend ha forma `{"message": "..."}`; il backend
  risponde con `{"response": "..."}`.
- Il backend iniziale è un segnaposto che ripete il messaggio ricevuto: non
  chiama un LLM e non richiede token o chiavi API.

Se in seguito aggiungi un servizio esterno, conserva le sue chiavi in
variabili d'ambiente lato backend. Non inserirle nel frontend né committarle.
