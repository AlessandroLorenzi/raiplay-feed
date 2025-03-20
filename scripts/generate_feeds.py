import os
import subprocess

# Percorso dello script single.py
SCRIPT_PATH = os.path.abspath("scripts/single.py")

# Lista dei programmi da generare
PROGRAMS = {
    "ungiornodapecora": "https://www.raiplaysound.it/programmi/ungiornodapecora",
    "zapping": "https://www.raiplaysound.it/programmi/zapping",
    "radioanchio": "https://www.raiplaysound.it/programmi/radioanchio"
}

for name, url in PROGRAMS.items():
    print(f"📡 Generazione feed per {name}...")

    try:
        # Esegui lo script single.py con il flag --programma
        result = subprocess.run(
            ["python3", SCRIPT_PATH, "--programma", url],
            capture_output=True,
            text=True,
            check=True
        )

        # Debug: Stampa il contenuto generato per vedere se è vuoto
        print(f"📜 Contenuto XML generato per {name}:\n{result.stdout}")

        # Se il contenuto è vuoto, segnalarlo
        if not result.stdout.strip():
            print(f"⚠ Attenzione: Il feed {name} è vuoto!")

        # Salva il feed generato
        file_name = f"feed_{name}.xml"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(result.stdout)

        print(f"✅ Feed XML salvato: {file_name}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Errore nell'esecuzione di single.py per {name}: {e.stderr}")
    except Exception as e:
        print(f"❌ Errore generico per {name}: {e}")
