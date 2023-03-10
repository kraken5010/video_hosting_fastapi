import shutil
from fastapi import UploadFile, BackgroundTasks, HTTPException
from uuid import uuid4

from models import Video
from schemas import UploadVideo


async def save_video(
        user: int,
        file: UploadFile,
        title: str,
        description: str,
        back_tasks: BackgroundTasks
):
    print(user.__dict__.get('id'))

    file_name = f'media/{user}_{uuid4()}.mp4'
    if file.content_type == 'video/mp4':
        back_tasks.add_task(write_video, file_name, file)
    else:
        raise HTTPException(status_code=418, detail="It isn't mp4")
    info = UploadVideo(title=title, description=description)
    return await Video.objects.create(file=file_name, user=user, **info.dict())


def write_video(file_name: str, file: UploadFile):
    # async with aiofiles.open(file_name, "wb") as buffer:
    #     data = await file.read()
    #     await buffer.write(data)
    with open(file_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)