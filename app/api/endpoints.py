from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from app.services.file_service import save_upload_file, list_files, get_file_path
from pathlib import Path

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    saved_path = save_upload_file(file)
    return {"filename": saved_path.name, "message": "Archivo subido correctamente"}


@router.get("/files")
async def get_files():
    files = list_files()
    return {"files": files}


@router.get("/download/{filename}")
async def download_file(filename: str):
    file_path = get_file_path(filename)
    if not file_path:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return FileResponse(path=file_path, filename=filename, media_type='application/octet-stream')


@router.get("/", response_class=HTMLResponse)
async def root():
    # Retorna la página web estática
    index_path = Path(__file__).parent.parent / "static" / "index.html"
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)
