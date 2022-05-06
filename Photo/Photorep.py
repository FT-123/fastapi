from sqlalchemy.orm import Session
from model import Photo


def create_posts(db: Session, name:str, title:str, body:str, url:str):
    db_post = Photo(title=title, body=body, owner_name=name, url=url)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db, id: int):
    return db.query(Photo).filter(Photo.id == id).first()


def post_list(db):
    return db.query(Photo).filter(Photo.id == id).first()
