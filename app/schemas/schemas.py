from pydantic import BaseModel
from typing import Optional

# -----------------------
#   PROPIETARIOS
# -----------------------

class PropietarioBase(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    email: Optional[str] = None


class PropietarioCreate(PropietarioBase):
    pass


class PropietarioUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None


class PropietarioOut(PropietarioBase):
    id: int

    class Config:
        orm_mode = True

