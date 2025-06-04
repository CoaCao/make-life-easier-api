from datetime import date
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    image_url: str
    expiry_date: date
    added_date: date


class ProductAdd(ProductBase):
    pass


class ProductEdit(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2
