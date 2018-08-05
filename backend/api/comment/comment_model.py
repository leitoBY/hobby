from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime, String, Text, Integer
from connection import db


class Comment(db.Model):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    title = Column(String(25))
    message = Column(Text())
    post_id = Column(Integer, ForeignKey('blog_post.id'))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
