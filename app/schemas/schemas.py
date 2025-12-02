from pydantic import BaseModel
from typing import Optional

# ==========================
#    SCHEMAS PROPIETARIO
# ==========================

class PropietarioBase(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    email: Optional[str] = None


class PropietarioCreate(PropietarioBase):
    """
    Schema para crear un propietario.
    Usa todos los campos de PropietarioBase.
    """
    pass


class PropietarioUpdate(BaseModel):
    """
    Schema para actualizar un propietario.
    Todos los campos son opcionales.
    """
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None


class PropietarioOut(PropietarioBase):
    """
    Lo que devuelve la API al frontend.
    Incluye el id.
    """
    id: int

    class Config:
        orm_mode = True
