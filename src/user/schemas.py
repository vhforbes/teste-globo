from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class User(BaseModel):
    id: int
    name: str
    email: str

    class ConfigDict:
        from_attributes = True
