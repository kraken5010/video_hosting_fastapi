from fastapi import APIRouter, UploadFile, File, Form
from starlette.background import BackgroundTasks
from starlette.responses import StreamingResponse
from starlette.templating import Jinja2Templates

from models import Video, User
from services import save_video

video_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@video_router.post("/")
async def create_video(
        back_tasks: BackgroundTasks,
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...)
):
    user = await User.objects.first()
    return await save_video(user, file, title, description, back_tasks)


@video_router.get("/video/{video_pk}")
async def get_video(video_pk: int):
    file = await Video.objects.select_related('user').get(pk=video_pk)
    file_like = open(file.dict().get('file'), mode='rb')
    return StreamingResponse(file_like, media_type="video/mp4")


