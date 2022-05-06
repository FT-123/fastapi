
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, URLType
import datetime
from auth import hashing
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



class Comments(Model):
    __tablename__ = "Comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    comment_owner = Column(String, unique=True, index=True)
    Photo_owner = Column(String, unique=True, index=True)
