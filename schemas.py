from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    user: Optional[str]


class UploadVideo(BaseModel):
    title: str
    description: str


class GetVideo(BaseModel):
    user: User
    title: str
    description: str