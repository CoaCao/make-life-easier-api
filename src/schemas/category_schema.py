from datetime import date
from typing import List

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryAdd(CategoryBase):
    pass


class CategoryEdit(CategoryBase):
    pass


class CategoryResponse(BaseModel):
    id: int
    name: str
    created_date: date

    class Config:
        from_attributes = True  # Pydantic v2


class CategoryListResponse(BaseModel):
    total: int
    items: List[CategoryResponse]
