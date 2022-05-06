from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import parse_obj_as
from typing import List
import model
import User.Usersschem
from User.Usersschem import User, UserCreate, UserBase
from User.Usersrep import UserRepository
from auth.jwt import get_current_user


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/api/registration/", response_model=User, status_code=status.HTTP_201_CREATED)
def createuser(user: UserCreate, users: UserRepository = Depends()):
    db_user = users.find_by_email(email=user.email)
    db_name = users.find_by_name(username=user.name)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    if db_name:
        raise HTTPException(
            status_code=404,
            detail="Username already registered"
        )
    db_user = users.create(user)
    return User.from_orm(db_user)


@router.get("/api/user/", response_model=User)
def cur_user(users: UserRepository = Depends(), current_user: model.User = Depends(get_current_user)):
    curret_name = current_user.name
    user_name = users.find_by_name(username=curret_name)
    return user_name


