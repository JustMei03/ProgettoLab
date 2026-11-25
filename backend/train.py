"""Legge il dataset CSV, pulisce i testi, addestra il modello sul sarcasmo e salva il file"""

import os
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Configurazione dei percorsi (relativi alla cartella backend/)
DATASET_PATH = "../data/dataset_sarcasmo.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "logistic_sarcasm.joblib")

def build_and_train_model():
    # --- FASE 1: Caricamento del dataset ---
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(
            f"Dataset non trovato in '{DATASET_PATH}'. "
            "Assicurati di aver messo il file CSV nella cartella data/."
        )

    df = pd.read_csv(DATASET_PATH)

    # Rimuove eventuali righe vuote
    df = df.dropna(subset=["text", "label"])

    X = df["text"].astype(str)   # Le frasi (Input)
    y = df["label"].astype(int)  # Le etichette: 1 = sarcastico, 0 = non sarcastico (Output)

    # --- FASE 2: Struttura dell'algoritmo (TF-IDF + Logistic Regression) ---
    pipeline = Pipeline([
        # Blocco A: Trasforma il testo in vettori numerici
        ("tfidf", TfidfVectorizer(
            ngram_range=(1, 2),                 # Analizza parole singole e coppie di parole
            max_features=15000,                 # Mantiene le 15.000 espressioni più rilevanti
            sublinear_tf=True,                  # Riduce il peso delle parole troppo ripetute
            token_pattern=r"(?u)\b\w+\b|[!?\"']" # Mantiene anche ! ? e virgolette
        )),
        # Blocco B: L'algoritmo di Logistic Regression vero e proprio
        ("logreg", LogisticRegression(
            C=1.0,                              # Forza di regolarizzazione (evita overfitting)
            max_iter=1000,                      # Numero massimo di passaggi per trovare i pesi ottimali
            class_weight="balanced",            # Bilancia automaticamente se ci sono più 0 che 1
            random_state=42
        ))
    ])

    # --- FASE 3: Test di verifica (80% addestramento, 20% esame) ---
    if len(df) >= 20:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        pipeline.fit(X_train, y_train)
        
        predictions = pipeline.predict(X_test)
        print(f"Accuratezza rilevata sul test set: {accuracy_score(y_test, predictions):.2%}")
        print("\nDettaglio metriche (Precision / Recall):\n")
        print(classification_report(y_test, predictions))

    # --- FASE 4: Addestramento finale su TUTTI i dati e salvataggio ---
    print("Addestramento finale sull'intero dataset in corso...")
    pipeline.fit(X, y)

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Fatto! Modello salvato in '{MODEL_PATH}'.")

if __name__ == "__main__":
    build_and_train_model()