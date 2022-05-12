
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, URLType
import datetime
from User import hashing
from database import Model
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


class User(Model):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    post = relationship("Photo", back_populates="owner")
    usercomment = relationship("Comment", back_populates="userowner")

    def __init__(self, name, email, password, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = hashing.get_password_hash(password)

    def check_password(self, password):
        return hashing.verify_password(self.password, password)


class Photo(Model):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    title = Column(String)
    url = Column(URLType)
    body = Column(String)
    owner_name = Column(String, ForeignKey("users.name"), nullable=False)
    owner = relationship("User", back_populates="post", foreign_keys=[owner_name])
    post_comment = relationship("Comment", back_populates="post_related")


class Comment(Model):

    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    name = Column(String, ForeignKey("users.name"), nullable=False)
    body = Column(String)
    photo_id = Column(Integer, ForeignKey("photos.id"), nullable=False)
    post_related = relationship("Photo", back_populates="post_comment", foreign_keys=[photo_id])
    userowner = relationship("User", back_populates="usercomment", foreign_keys=[name])
    