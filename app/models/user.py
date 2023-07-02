from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

    class Config:
        orm_mode = True