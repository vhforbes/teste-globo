from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.database import get_db
from typing import List
from .service import VideoService
from .schemas import CreateVideoPayload, EditVideoPayload, VideoSchema
from src.models import Video

video_router = APIRouter()


@video_router.post("/create-video", response_model=VideoSchema)
def create_video(video: CreateVideoPayload, db: Session = Depends(get_db)):
    video_service = VideoService(db)

    created_video = video_service.create_video(video)

    return created_video


@video_router.patch("/video/{video_id}", response_model=VideoSchema)
def edit_video(
    video_id: int, edit_video_payload: EditVideoPayload, db: Session = Depends(get_db)
):
    video_service = VideoService(db)

    edited_video = video_service.edit_video(video_id, edit_video_payload)

    return edited_video


@video_router.get("/videos", response_model=List[VideoSchema])
def list_videos(db: Session = Depends(get_db)):
    video_service = VideoService(db)
    videos = video_service.list_videos()
    return videos


@video_router.delete("/video/{video_id}", response_model=dict)
def list_videos(video_id: int, db: Session = Depends(get_db)):
    video_service = VideoService(db)
    result = video_service.delete_video(video_id)
    return result
