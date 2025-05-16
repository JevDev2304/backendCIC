from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class ProductBase(SQLModel):
    title: str
    price: int
    image: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None

class Products(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creationAt: datetime = Field(default_factory=datetime.utcnow)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    title: Optional[str] = None
    price: Optional[int] = None


