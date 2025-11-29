from fastapi import APIRouter

router = APIRouter(prefix="", tags=["General"])

@router.get("/ping")
def ping():
    return {"ping": "pong"}
