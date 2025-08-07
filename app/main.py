from fastapi import FastAPI
from app.api.endpoints import router
from app.core.config import HOST, PORT
import uvicorn

app = FastAPI(title="JD Server")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
