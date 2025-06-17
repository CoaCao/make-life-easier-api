from decimal import Decimal

from pydantic import BaseModel


class SpendingByCategory(BaseModel):
    category_id: int
    category_name: str
    total_purchased: Decimal


class TotalPurchased(BaseModel):
    total_purchased: Decimal
