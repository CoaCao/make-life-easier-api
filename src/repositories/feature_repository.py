from datetime import date
from decimal import Decimal
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from src.models.category_model import Category
from src.models.product_model import Product


def get_categories_purchased(
        db: Session,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
        category_id: Optional[int] = None
):
    query = (
        db.query(
            Category.id.label("category_id"),
            Category.name.label("category_name"),
            func.sum(Product.price).label("total_purchased")
        )
        .join(Product, Product.category_id == Category.id)
        .filter(Product.enabled == 1, Category.enabled == 1)
    )

    if category_id:
        query = query.filter(Category.id == category_id)

    if from_date:
        query = query.filter(Product.purchased_date >= from_date)
    if to_date:
        query = query.filter(Product.purchased_date <= to_date)

    query = query.group_by(Category.id, Category.name)
    return query.all()


def get_products_purchased(
        db: Session,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
) -> Decimal:
    query = db.query(func.sum(Product.price)).filter(Product.enabled == 1)

    if from_date:
        query = query.filter(Product.purchased_date >= from_date)
    if to_date:
        query = query.filter(Product.purchased_date <= to_date)

    total = query.scalar() or 0
    return total
