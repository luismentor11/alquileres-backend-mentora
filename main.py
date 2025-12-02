from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.routes import router
from app.routers.propietarios import router as propietarios_router

app = FastAPI(
    title="Mentora - Administración de Alquileres",
    version="0.1.0",
    description="Backend inicial para gestión de alquileres con FastAPI."
)

# CORS (por si después conectás un frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(router)                # rutas que ya tenías
app.include_router(propietarios_router)   # NUEVO: propietarios


@app.get("/")
def root():
    return {"message": "API Mentora Alquileres funcionando"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "0.1.0"}
