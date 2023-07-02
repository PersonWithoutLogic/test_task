from typing import Optional
from pydantic import BaseModel

class MessageBase(BaseModel):
    text: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True