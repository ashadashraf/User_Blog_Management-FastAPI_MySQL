from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    mobile: str
    about: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    mobile: str
    about: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

class UpdateUser(BaseModel):
    name: str
    email: str
    mobile: str
    about: str
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    id: int | None = None

class Order(BaseModel):
    product: str
    units: int

class Product(BaseModel):
    name: str
    notes: str