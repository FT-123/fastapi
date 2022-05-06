import os
from .Photorep import create_posts, all, get_post, delete_photo, verify_photo
import model
from dependencies import get_db
from fastapi import APIRouter, Depends, status, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from auth.jwt import get_current_user


import shutil


router = APIRouter(prefix="/Photo", tags=["photos"])


@router.post("/api/photos/", status_code=status.HTTP_201_CREATED)
def create_photo(
    title: str, body: str, file: UploadFile = File(...), db: Session = Depends(get_db),
        current_user: model.User = Depends(get_current_user)
):
    with open(f'image/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    user_name = current_user.name

    url = os.getcwd()+"/image/"+file.filename

    return create_posts(db=db, name=user_name, title=title, body=body, url=url)


@router.get("/api/photos/[PHOTO_ID]")
def photo_detail(post_id: int, db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
    post = get_post(db=db, id=post_id)

    comment = db.query(model.Comment).filter(model.Comment.post_id == post_id)

    active_comment = comment.filter(model.Comment.is_active == True).all()

    if post is None:
        raise HTTPException(status_code=404, detail="post does not exist")
    return {"post": post, "active_comment": active_comment}

@router.get("/api/photos/")
def photo_list(db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
    return all(db=db)

@router.delete("/api/photos/[PHOTO_ID]/")
def photo_delete(post_id: int, db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
    user_name = current_user.name
    post = get_post(db=db, id=post_id)
    stmt = verify_photo(db=db, id=post_id, username=user_name)
    if not stmt == post:
        raise HTTPException(status_code=404, detail="unauthorized")
    dele = delete_photo(db=db, id=post_id)
    return dele




