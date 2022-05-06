import os
from .Photorep import create_posts, post_list, get_post
import model
from dependencies import get_db
from fastapi import APIRouter, Depends, status, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from auth.jwt import get_current_user
from User.Usersschem import UserBase

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


@router.get("/posts/")
def post_list(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return post_list(db=db)


@router.get("/posts/{post_id}")
def post_detail(post_id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    post = get_post(db=db, id=post_id)

    comment = db.query(model.Comment).filter(model.Comment.post_id == post_id)

    active_comment = comment.filter(model.Comment.is_active == True).all()

    if post is None:
        raise HTTPException(status_code=404, detail="post does not exist")
    return {"post": post, "active_comment": active_comment}
