from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .Commentrep import create_comment
from .Commentschem import CommentBase, CommentList
from dependencies import get_db
from User.Usersschem import UserBase
from auth.jwt import get_current_user
import model


router = APIRouter(prefix="/Photo", tags=["photos"])


@router.post("/posts/{post_id}/comment", response_model=CommentList)
def create_comments(
        comment: CommentBase, post_id: int, db: Session = Depends(get_db),
        current_user: model.User = Depends(get_current_user)):
    user_name = current_user.name

    return create_comment(db=db, post_id=post_id, name=user_name, comment=comment)
