from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])


router = APIRouter()

@router.get("/me")
def read_me(user=Depends(get_current_user)):
    return {"message": "Autenticado com sucesso"}