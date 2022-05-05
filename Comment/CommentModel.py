from sqlalchemy import Column, String, Integer
from database import Model


class Comments(Model):
    __tablename__ = "Comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    comment_owner = Column(String, index=True)
    Photo_owner = Column(String, index=True)
