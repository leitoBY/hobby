from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime, String, Text, Integer
from connection import db


class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    title = Column(String(25))
    content = Column(Text())
    comments = relationship("Comment")
    author = Column(String(25))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
