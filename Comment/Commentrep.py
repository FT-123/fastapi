from sqlalchemy.orm import Session
from .Commentschem import CommentBase
from model import Comment


def create_comment(db: Session, photo_id: int, name: str, comment: CommentBase):
    db_comment = Comment(photo_id=photo_id, name=name, **comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment(db: Session, id: int):
    query = db.query(Comment)
    return query.filter(Comment.id == id).first()


def verify_comment(db: Session, id: int, username: str):
    query = db.query(Comment)
    find = query.filter(Comment.id == id).where(Comment.name == username).first()
    if not find:
        raise HTTPException(status_code=404, detail="unauthorized")
    return find


def delete_comment(id: int, db: Session):
    de = db.get(Comment, id)
    if not de:
        raise HTTPException(status_code=404, detail="unauthorized")
    db.delete(de)
    db.commit()
    return {"ok": True}