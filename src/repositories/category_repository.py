from typing import Optional

from sqlalchemy.orm import Query, Session
from src.models.category_model import Category
from src.schemas.category_schema import CategoryAdd, CategoryEdit


def get_all(db: Session, name: str | None = None):
    query = db.query(Category)
    query = apply_filters(query, name)

    return {"total": query.count(), "items": query.all()}


def apply_filters(query: Query, name: Optional[str] = None) -> Query:
    query = query.filter(Category.enabled == 1)
    if name is None:
        return query

    return query.filter(Category.name.ilike(f"%{name}%"))


def get_by_id(db: Session, id: int):
    return db.query(Category).filter(Category.id == id, Category.enabled == 1).first()


def add(db: Session, category: CategoryAdd):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def edit(db: Session, category_id: int, category: CategoryEdit):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        for field, value in category.model_dump().items():
            setattr(db_category, field, value)
        db.commit()
        db.refresh(db_category)
        return db_category
    return None


def remove(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db_category.enabled = 0
        db.commit()
        return db_category
    return None
