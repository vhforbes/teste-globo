from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.models import Video
from . import schemas


class VideoService:
    def __init__(self, db: Session):
        self.db = db

    def create_video(self, video: schemas.CreateVideoPayload):

        self.check_existing_url(video.url)

        new_video = Video(user_id=video.user_id, title=video.title, url=video.url)

        self.db.add(new_video)
        self.db.commit()

        return new_video

    def edit_video(self, video_id, video: schemas.EditVideoPayload):
        existing_video = self.db.query(Video).filter(Video.id == video_id).first()

        self.check_existing_url(video.url, video_id=video_id)

        if existing_video:
            existing_video.title = video.title
            existing_video.url = video.url

            self.db.add(existing_video)
            self.db.commit()

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Video does not exist"
            )

        return existing_video

    def list_videos(self):
        videos = self.db.query(Video).all()
        return videos

    def delete_video(self, video_id: int):
        video = self.db.query(Video).filter(Video.id == video_id).first()

        if not video:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Video not found"
            )

        self.db.delete(video)
        self.db.commit()

        return {"detail": "Video deleted successfully"}

    def check_existing_url(self, url, video_id=None):
        query = self.db.query(Video).filter(Video.url == url)

        if video_id:
            query = query.filter(Video.id != video_id)

        video_url_already_exists = query.first()

        if video_url_already_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A video with this URL already exists",
            )
