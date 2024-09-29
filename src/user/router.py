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
    try:
        db_user = user_service.create_user(user)
        return db_user
    except HTTPException as e:
        return JSONResponse(
            content={"detail": str(e.detail)}, status_code=e.status_code
        )


@user_router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.get_user(user_id)
    return user
