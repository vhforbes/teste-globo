from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.database import get_db
from .service import UserService
from .schemas import UserCreate, User

user_router = APIRouter()


@user_router.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)

    created_user = user_service.create_user(user)

    return created_user


@user_router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return JSONResponse(content="Not Implemented", status_code=200)
