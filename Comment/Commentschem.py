from pydantic import BaseModel
from typing import Optional
from fastapi import Body
from User.Usersschem import UserBase
import datetime


class CommentBase(BaseModel):
    body: str


class CommentList(CommentBase):
    id: int
    name: str
    photo_id: int
    created_date: Optional[datetime.datetime] = Body(None)


    class Config:
        orm_mode= True