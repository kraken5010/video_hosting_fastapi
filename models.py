import datetime
from typing import Optional, Union

import ormar
from ormar import Model, ModelMeta
from db import metadata, database


class MainMata(ModelMeta):
    metadata = metadata
    database = database


class User(Model):
    class Meta(MainMata):
        pass

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=100)


class Video(Model):
    class Meta(MainMata):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=50)
    description: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    user: Union[User, int, None] = ormar.ForeignKey(User)