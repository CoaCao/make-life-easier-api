from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from src.models.product_model import Product
from src.schemas.product_schema import ProductAdd, ProductEdit


def get_all(db: Session, skip: int = 0, limit: int = 10, sort_by: str = "expiry_date", sort_order: str = "asc"):
    query = db.query(Product).filter(Product.enabled == 1)

    sort_column = getattr(Product, sort_by, None)
    if sort_column:
        query = query.order_by(asc(sort_column) if sort_order == "asc" else desc(sort_column))

    return query.offset(skip).limit(limit).all()


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
