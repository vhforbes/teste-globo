from pydantic import BaseModel


class VideoSchema(BaseModel):
    id: int
    user_id: int
    title: str
    url: str


class CreateVideoPayload(BaseModel):
    user_id: int
    title: str
    url: str


class EditVideoPayload(BaseModel):
    title: str
    url: str
