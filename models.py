import datetime

from sqlalchemy import Column, Integer, String, DateTime

from db import Base


class Post(Base):

    __tablename__ = "posts"


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable = False)
    text = Column(String, nullable = False)
    created_at = Column(DateTime, nullable = False, default=datetime.datetime.utcnow)