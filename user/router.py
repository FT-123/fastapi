from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from user.model import User
from . import hashing
from .jwt import create_access_token
import dependencies

router = APIRouter(tags=["users"])


@router.post('/api/login/')
def login(request: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(dependencies.get_db)):
    user = database.query(User).filter(User.name == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Name')

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    access_token = create_access_token(data={"sub": user.name})

    return {"access_token": access_token, "token_type": "bearer"}
