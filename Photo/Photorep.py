from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.params import Depends
from User.model import Photo
from typing import List
from dependencies import get_db


class PhotoRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_posts(self, name: str, title: str, body: str, url: str):
        db_post = Photo(title=title, body=body, owner_name=name, url=url)
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return db_post

    def get_post(self, id: int):
        query = self.db.query(Photo)
        return query.filter(Photo.id == id).first()

    def all(self, skip: int = 0, max: int = 100) -> List[Photo]:
        query = self.db.query(Photo)
        return query.offset(skip).limit(max).all()

    def verify_photo(self, id: int, username: str):
        query = self.db.query(Photo)
        find = query.filter(Photo.id == id).where(Photo.owner_name == username).first()
        if not find:
            raise HTTPException(status_code=404, detail="unauthorized")
        return find

    def delete_photo(self, id: int):
        de = self.db.get(Photo, id)
        if not de:
            raise HTTPException(status_code=404, detail="unauthorized")
        self.db.delete(de)
        self.db.commit()
        return {"ok": True}


