# IronITA 2018

Tweet italiani annotati per ironia e sarcasmo, dal task IronITA di EVALITA 2018.

| File | Tweet | Ironici | Sarcastici |
|---|---|---|---|
| `train.tsv` | 3977 | 2023 | 913 |
| `test.tsv` | 872 | 435 | 216 |

## Colonne (separate da tabulazione)

- `id`: id del tweet
- `text`: testo, con link sostituiti da `<URL>`
- `irony`: 1 = ironico, 0 = non ironico
- `sarcasm`: 1 = sarcastico, 0 = non sarcastico (un tweet sarcastico è sempre anche ironico)
- `topic`: corpus di provenienza. Nel train: `HSC` (immigrazione), `TW-BS` (Buona Scuola), `TW-SENTIPOLC` (politica), `TW-SPINO` (satira di Spinoza); nel test c'è anche `TWITA`

## Fonte e licenza

- Copia da [RiTA-nlp/UINAUIL](https://huggingface.co/datasets/RiTA-nlp/UINAUIL) (cartella `ironita/`)
- Licenza: CC BY-NC-SA 4.0 (solo uso non commerciale)
- Da citare: Cignarella et al., *Overview of the EVALITA 2018 Task on Irony Detection in Italian Tweets (IronITA)*, EVALITA 2018.
