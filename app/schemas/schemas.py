from pydantic import BaseModel, EmailStr
from typing import Optional


# ==========================
#    SCHEMAS PROPIETARIO
# ==========================

class PropietarioBase(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None


class PropietarioCreate(PropietarioBase):
    pass


class PropietarioUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None


class PropietarioOut(PropietarioBase):
    id: int

    class Config:
        orm_mode = True
