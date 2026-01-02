from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    return {
        "message": "Login recebido com sucesso",
        "username": username
    }
