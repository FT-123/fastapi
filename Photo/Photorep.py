from sqlalchemy.orm import Session
from model import Photo
from typing import List


def create_posts(db: Session, name:str, title:str, body:str, url:str):
    db_post = Photo(title=title, body=body, owner_name=name, url=url)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(self, id: int):
    query = self.db.query(Photo)
    return query(Photo).filter(Photo.id == id).first()


def all(db: Session, skip: int = 0, max: int = 100) -> List[Photo]:
    query = db.query(Photo)
    return query.offset(skip).limit(max).all()




