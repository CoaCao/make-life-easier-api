from datetime import date
from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    image_url: str
    expiry_date: date


class ProductAdd(ProductBase):
    pass


class ProductEdit(ProductBase):
    pass


class ProductResponse(ProductBase):
    added_date: date
    id: int

    class Config:
        from_attributes = True  # Pydantic v2


class ProductListResponse(BaseModel):
    total: int
    items: List[ProductResponse]
