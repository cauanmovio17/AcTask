from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.database.database import Base, engine
from app.models.user import User
from app.routes import auth, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)

security = HTTPBearer()
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "TaskReal API rodando"}
