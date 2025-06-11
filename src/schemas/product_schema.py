from datetime import date
from decimal import Decimal
from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    category_id: int
    image_url: str
    price: Decimal
    expiration_date: date


class ProductAdd(ProductBase):
    pass


class ProductEdit(ProductBase):
    pass


class ProductResponse(BaseModel):
    id: int
    name: str
    category_id: int
    category_name: str
    image_url: str
    price: Decimal
    expiration_date: date
    purchased_date: date

    class Config:
        from_attributes = True  # Pydantic v2


class ProductListResponse(BaseModel):
    total_available: int
    total_return: int
    items: List[ProductResponse]
