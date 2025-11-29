from fastapi import FastAPI
from app.database import get_db
from app.routers.routes import router

app = FastAPI(
    title="Mentora - Administración de Alquileres",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API Mentora Alquileres funcionando"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "0.1.0"}
