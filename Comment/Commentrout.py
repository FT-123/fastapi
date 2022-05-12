from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .Commentrep import CommentRepository
from Photo.Photorep import PhotoRepository
from .Commentschem import CommentBase, CommentList
from dependencies import get_db
from User.jwt import get_current_user
from User import model

router = APIRouter(prefix="/Comment", tags=["comments"])


@router.post("/api/photos/{photo_id}/comment", response_model=CommentList)
def create_comments(
        comment: CommentBase, photo_id: int, current_user: model.User = Depends(get_current_user),
        comments: CommentRepository = Depends(), photos: PhotoRepository = Depends()):
    user_name = current_user.name
    photo_have = photos.get_post(id=photo_id)
    if not photo_have:
        raise HTTPException(status_code=404, detail="Photo not found")
    return comments.create_comment(photo_id=photo_id, name=user_name, comment=comment)


@router.delete("/api/photos/comment/[COMMENT_ID]/")
def photo_delete(comment_id: int, comments: CommentRepository = Depends(),
                 current_user: model.User = Depends(get_current_user)):
    user_name = current_user.name
    post = comments.get_comment(id=comment_id)
    stmt = comments.verify_comment(id=comment_id, username=user_name)
    if not stmt == post:
        raise HTTPException(status_code=404, detail="unauthorized")
    dele = comments.delete_comment(id=comment_id)
    return dele
