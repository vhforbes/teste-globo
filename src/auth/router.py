from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.database import get_db
from src.auth.service import AuthService
from sqlalchemy.orm import Session
from . import schemas

auth_router = APIRouter()


@auth_router.post("/login")
def login(loginPayload: schemas.LoginPayload, db: Session = Depends(get_db)):

    auth_service = AuthService(db)

    result, status_code = auth_service.login(
        email=loginPayload.email, password=loginPayload.password
    )

    return JSONResponse(content=result, status_code=status_code)
