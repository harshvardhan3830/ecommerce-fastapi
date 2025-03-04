from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    description: str
    price: float
    stock: int
