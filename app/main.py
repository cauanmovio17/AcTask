from fastapi import FastAPI
from app.routes import auth, users

app = FastAPI(title="TaskReal API")

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"status": "API rodando com sucesso 🚀"}
