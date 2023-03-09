from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: Optional[str]


class UploadVideo(BaseModel):
    title: str
    description: str


class GetListVideo(BaseModel):
    id: int
    title: str
    description: str


class GetVideo(GetListVideo):
    user: User