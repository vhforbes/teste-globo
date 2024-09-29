from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import User
from . import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: schemas.UserCreate):

        user_exists = self.db.query(User).filter(User.email == user.email).first()

        if user_exists:
            raise HTTPException(status_code=400, detail="Email already in use")

        hashed_password = pwd_context.hash(user.password)

        created_user = User(name=user.name, email=user.email, password=hashed_password)

        self.db.add(created_user)
        self.db.commit()
        self.db.refresh(created_user)

        return created_user

    # def get_user(self, user_id: int):
    #     user = self.db.query(User).filter(User.id == user_id).first()
    #     if not user:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     return user

    # def get_user_by_email(self, email: str):
    #     return self.db.query(User).filter(User.email == email).first()

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
