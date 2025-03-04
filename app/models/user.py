from pydantic import BaseModel, Field
from typing import Optional


class UserModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    username: str
    email: str
    password: str
