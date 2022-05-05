from sqlalchemy import Column, String, Integer
from database import Model


class Photo(Model):
    __tablename__ = "Photos"

    id = Column(Integer, primary_key=True, index=True)
    photo_file = Column(String, unique=True, index=True)
    photo_dis = Column(String)
    photo_owner = Column(String, index=True)