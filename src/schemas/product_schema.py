from datetime import date
from decimal import Decimal
from typing import List

from pydantic import BaseModel
from sqlalchemy import Numeric


class ProductBase(BaseModel):
    name: str
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
    image_url: str
    price: Decimal
    expiration_date: date
    purchased_date: date

    class Config:
        from_attributes = True  # Pydantic v2


class ProductListResponse(BaseModel):
    total: int
    items: List[ProductResponse]
