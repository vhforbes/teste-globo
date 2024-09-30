from fastapi import FastAPI
from fastapi import FastAPI
from src.user.router import user_router
from src.auth.router import auth_router
from .models import Base
from .database import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(auth_router)
