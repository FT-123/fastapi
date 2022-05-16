from sqlalchemy.orm import Session
from .comment_schem import CommentBase
from fastapi import HTTPException, Depends
from dependencies import get_db
from user.model import Comment


class CommentRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_comment(self, photo_id: int, name: str, comment: CommentBase):
        db_comment = Comment(photo_id=photo_id, name=name, **comment.dict())
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return db_comment

    def get_comment(self, id: int):
        query = self.db.query(Comment)
        return query.filter(Comment.id == id).first()

    def verify_comment(self, id: int, username: str):
        query = self.db.query(Comment)
        find = query.filter(Comment.id == id).where(Comment.name == username).first()
        if not find:
            raise HTTPException(status_code=404, detail="unauthorized")
        return find

    def delete_comment(self, id: int):
        de = self.db.get(Comment, id)
        if not de:
            raise HTTPException(status_code=404, detail="unauthorized")
        self.db.delete(de)
        self.db.commit()
        return {"ok": True}
