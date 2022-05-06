from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .Commentrep import create_comment, verify_comment, get_comment, delete_comment
from Photo.Photorep import get_post
from .Commentschem import CommentBase, CommentList
from dependencies import get_db
from auth.jwt import get_current_user
import model


router = APIRouter(prefix="/Comment", tags=["comments"])


@router.post("/api/photos/{photo_id}/comment", response_model=CommentList)
def create_comments(
        comment: CommentBase, photo_id: int, db: Session = Depends(get_db),
        current_user: model.User = Depends(get_current_user)):
    user_name = current_user.name
    photo_have = get_post(db=db, id=photo_id)
    if not photo_have:
        raise HTTPException(status_code=404, detail="Photo not found")
    return create_comment(db=db, photo_id=photo_id, name=user_name, comment=comment)


@router.delete("/api/photos/comment/[COMMENT_ID]/")
def photo_delete(comment_id: int, db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
    user_name = current_user.name
    post = get_comment(db=db, id=comment_id)
    stmt = verify_comment(db=db, id=comment_id, username=user_name)
    if not stmt == post:
        raise HTTPException(status_code=404, detail="unauthorized")
    dele = delete_comment(db=db, id=comment_id)
    return dele
