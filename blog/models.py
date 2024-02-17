from sqlalchemy import Column, Integer, String, ForeignKey
from blog.database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    email = Column(String(50), unique=True)
    mobile = Column(String(10))
    about = Column(String(100))
    password = Column(String(300))

    blogs = relationship("Blog", back_populates="creator")