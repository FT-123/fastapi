from sqlalchemy.orm import Session
from .Commentschem import CommentBase
from model import Comment


def create_comment(db: Session, post_id: int, name: str, comment: CommentBase):
    db_comment = Comment(post_id=post_id, name=name, **comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
