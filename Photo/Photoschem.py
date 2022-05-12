from typing import Optional
from pydantic import BaseModel
import datetime
from User.Usersschem import UserBase


class PostBase(BaseModel):
    title: str
    body: str


class PostList(PostBase):
    created_date: Optional[datetime.datetime]
    owner_name: str
    owner: UserBase.name

    class Config:
        orm_mode=True