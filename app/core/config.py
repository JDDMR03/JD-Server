import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"

# Crear carpeta uploads si no existe
os.makedirs(UPLOAD_DIR, exist_ok=True)

HOST = "0.0.0.0"
PORT = 8000
