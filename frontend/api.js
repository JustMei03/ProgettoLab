// Collegamento con il backend: tutte le chiamate HTTP passano da qui.

// Se la pagina è servita dal backend (localhost:8000) basta l'URL relativo,
// altrimenti (es. Live Server) si punta al backend su :8000.
const API_BASE = location.port === "8000" ? "" : "http://localhost:8000";

async function chiama(percorso, opzioni = {}) {
  const risposta = await fetch(API_BASE + percorso, {
    headers: { "Content-Type": "application/json" },
    ...opzioni,
  });
  if (!risposta.ok) throw new Error(`Errore del backend (${risposta.status})`);
  return risposta.json();
}

// GET /health → { status: "ok" }
export function statoBackend() {
  return chiama("/health");
}

// POST /api/chat → { response, sarcastico, probabilita }
export function inviaMessaggio(message, context = null) {
  return chiama("/api/chat", {
    method: "POST",
    body: JSON.stringify({ message, context }),
  });
}
