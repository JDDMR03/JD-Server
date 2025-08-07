from pathlib import Path
from fastapi import UploadFile
from app.core.config import UPLOAD_DIR
import shutil


def save_upload_file(upload_file: UploadFile) -> Path:
    file_location = UPLOAD_DIR / upload_file.filename
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_location


def list_files():
    return [f.name for f in UPLOAD_DIR.iterdir() if f.is_file()]


def get_file_path(filename: str) -> Path:
    file_path = UPLOAD_DIR / filename
    if file_path.exists() and file_path.is_file():
        return file_path
    return None
