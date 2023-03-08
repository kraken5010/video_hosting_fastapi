import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form

from schemas import UploadVideo, GetVideo
from models import Video, User

video_router = APIRouter()


@video_router.post("/")
async def create_video(
        title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)
):
    info = UploadVideo(title=title, description=description)
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    user = await User.objects.first()
    return await Video.objects.create(file=file.filename, user=user, **info.dict())


@video_router.get("/video/{video_pk}", response_model=GetVideo)
async def get_video(video_pk: int):
    return await Video.objects.get(pk=video_pk)


