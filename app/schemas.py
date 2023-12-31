from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# POST
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# USER 
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# AUTH
class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id: Optional[int] = None