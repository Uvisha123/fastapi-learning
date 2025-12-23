from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=3)
    price: float = Field(..., ge=0)
    description: Optional[str] = None

class ItemOut(BaseModel):
    id: int
    name: str
    price: float
