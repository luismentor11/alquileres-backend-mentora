from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.models import Propietario
from app.schemas.schemas import PropietarioCreate, PropietarioOut, PropietarioUpdate

router = APIRouter(
    prefix="/propietarios",
    tags=["Propietarios"]
)


@router.post("/", response_model=PropietarioOut)
def create_propietario(data: PropietarioCreate, db: Session = Depends(get_db)):
    propietario = Propietario(
        nombre=data.nombre,
        telefono=data.telefono,
        email=data.email
    )
    db.add(propietario)
    db.commit()
    db.refresh(propietario)
    return propietario


@router.get("/", response_model=list[PropietarioOut])
def list_propietarios(db: Session = Depends(get_db)):
    propietarios = db.query(Propietario).all()
    return propietarios


@router.get("/{propietario_id}", response_model=PropietarioOut)
def get_propietario(propietario_id: int, db: Session = Depends(get_db)):
    propietario = db.query(Propietario).filter(Propietario.id == propietario_id).first()
    if not propietario:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")
    return propietario


@router.put("/{propietario_id}", response_model=PropietarioOut)
def update_propietario(propietario_id: int, data: PropietarioUpdate, db: Session = Depends(get_db)):
    propietario = db.query(Propietario).filter(Propietario.id == propietario_id).first()
    if not propietario:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")

    cambios = data.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(propietario, campo, valor)

    db.commit()
    db.refresh(propietario)
    return propietario


@router.delete("/{propietario_id}")
def delete_propietario(propietario_id: int, db: Session = Depends(get_db)):
    propietario = db.query(Propietario).filter(Propietario.id == propietario_id).first()
    if not propietario:
        raise HTTPException(status_code=404, detail="Propietario no encontrado")

    db.delete(propietario)
    db.commit()
    return {"message": "Propietario eliminado correctamente"}
