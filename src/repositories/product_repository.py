from datetime import datetime, timedelta, UTC
from typing import Optional

from sqlalchemy import asc, desc
from sqlalchemy.orm import Query, Session
from src.models.product_model import Product
from src.schemas.product_schema import ProductAdd, ProductEdit


def get_all(db: Session, skip: int = 0, limit: int = 10,
        sort_by: str = "expiry_date", sort_order: str = "asc",
        name: str | None = None,
        days_to_expire: int | None = None):
    query = db.query(Product)
    query = apply_filters(query, name, days_to_expire)
    total = query.count()

    sort_column = getattr(Product, sort_by, None)
    if sort_column:
        query = query.order_by(asc(sort_column) if sort_order == "asc" else desc(sort_column))

    products = query.offset(skip).limit(limit).all()

    return {"total": total, "items": products}


def apply_filters(query: Query,
        name: Optional[str] = None,
        days_to_expire: Optional[int] = None) -> Query:
    query = query.filter(Product.enabled == 1)

    if days_to_expire is not None:
        now = datetime.now(UTC).date()
        future = now + timedelta(days=days_to_expire)
        query = query.filter(Product.expiry_date >= now, Product.expiry_date <= future)

    if name is not None:
        query = query.filter(Product.name.ilike(f"%{name}%"))

    return query


def get_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id, Product.enabled == 1).first()


def add(db: Session, product: ProductAdd):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def edit(db: Session, product_id: int, product: ProductEdit):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        for field, value in product.model_dump().items():
            setattr(db_product, field, value)
        db.commit()
        db.refresh(db_product)
        return db_product
    return None


def remove(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db_product.enabled = 0
        db.commit()
        return db_product
    return None
