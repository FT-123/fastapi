from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, Depends
from auth.jwt import get_current_user
from model import Photo, User
from typing import List


def create_posts(db: Session, name:str, title:str, body:str, url:str):
    db_post = Photo(title=title, body=body, owner_name=name, url=url)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, id: int):
    query = db.query(Photo)
    return query.filter(Photo.id == id).first()


def all(db: Session, skip: int = 0, max: int = 100) -> List[Photo]:
    query = db.query(Photo)
    return query.offset(skip).limit(max).all()


def get_user_by_photo_id(db: Session, id: int):
    query = db.query(Photo)
    return query.select(Photo.owner_name).where(Photo.id == id).first()


def delete_photo(id: int, db: Session):
    de = db.get(Photo, id)
    if not de:
        raise HTTPException(status_code=404, detail="Photo not found")
    db.delete(de)
    db.commit()
    return {"ok": True}


