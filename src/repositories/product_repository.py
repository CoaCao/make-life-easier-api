from datetime import date, datetime, timedelta, UTC
from decimal import Decimal
from typing import Optional

from sqlalchemy import asc, desc, func
from sqlalchemy.orm import Query, Session

from src.exceptions.product_exceptions import ProductNotFoundException
from src.models.category_model import Category
from src.models.product_model import Product
from src.schemas.product_schema import ProductAdd, ProductEdit, ProductResponse


def get_all(db: Session, skip: int, limit: int,
        sort_by: str = "expiration_date", sort_order: str = "asc",
        name: str | None = None, category_id: int | None = None, days_to_expire: int | None = None):
    query = (db.query(Product, Category.name.label("category_name"))
             .join(Category, Product.category_id == Category.id)
             .filter(Category.enabled == 1, Product.enabled == 1))

    query = apply_filters(query, name, category_id, days_to_expire)
    total = query.count()

    if total == 0:
        raise ProductNotFoundException("Not found data with given parameters")

    sort_column = getattr(Product, sort_by, None)
    if sort_column:
        query = query.order_by(asc(sort_column) if sort_order == "asc" else desc(sort_column))

    query = query.offset(skip)
    if limit:
        query = query.limit(limit)

    results = query.all()

    items = [
        ProductResponse(
            id=product.id,
            name=product.name,
            category_id=product.category_id,
            category_name=category_name,
            image_url=product.image_url,
            price=product.price,
            expiration_date=product.expiration_date,
            purchased_date=product.purchased_date,
        )
        for product, category_name in results
    ]
    return {"total_available": total, "total_return": len(items), "items": items}


def apply_filters(query: Query,
        name: Optional[str] = None,
        category_id: Optional[int] = None,
        days_to_expire: Optional[int] = None) -> Query:
    if name is not None:
        query = query.filter(Product.name.ilike(f"%{name}%"))

    if category_id is not None:
        query = query.filter(Product.category_id == category_id)

    if days_to_expire is not None:
        now = datetime.now(UTC).date()
        future = now + timedelta(days=days_to_expire)
        query = query.filter(Product.expiration_date >= now, Product.expiration_date <= future)

    return query


def get_by_id(db: Session, product_id: int):
    # product = db.query(Product).filter(Product.id == product_id, Product.enabled == 1).first()
    product = (db.query(Product, Category.name.label("category_name"))
               .join(Category, Product.category_id == Category.id)
               .filter(Category.enabled == 1, Product.enabled == 1, Product.id == product_id)
               .first())

    if not product:
        raise ProductNotFoundException(f"Product not found with product_id={product_id}")

    return product


def add(db: Session, product: ProductAdd):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def edit(db: Session, product_id: int, product: ProductEdit):
    db_product, category_name = get_by_id(db, product_id)

    for field, value in product.model_dump().items():
        setattr(db_product, field, value)
    db.commit()
    # db.refresh(db_product)
    #
    # return get_by_id(db, product_id)


def remove(db: Session, product_id: int):
    db_product = get_by_id(db, product_id)

    if db_product:
        db_product.enabled = 0
        db.commit()
        return db_product
    return None


def get_categories_spending(
        db: Session,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
        category_id: Optional[int] = None
):
    query = (
        db.query(
            Category.id.label("category_id"),
            Category.name.label("category_name"),
            func.sum(Product.price).label("total_spent")
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


def get_total_spending(
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
