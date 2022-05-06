import os

from .Photorep import create_posts
import model
from dependencies import get_db
from fastapi import APIRouter, Depends, status, File, UploadFile
from sqlalchemy.orm import Session
from auth.jwt import get_current_user

import shutil


router = APIRouter(prefix="/Photo", tags=["photos"])


@router.post("/posts/",status_code=status.HTTP_201_CREATED)
def create_post(
    title:str, body:str, file: UploadFile = File(...), db: Session = Depends(get_db),
        current_user: model.User = Depends(get_current_user)
):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    user_name = current_user.name

    url = file.filename
    #os.getcwd()+"/image/"file.filename

    return create_posts(db=db, name=user_name, title=title, body=body, url=url)