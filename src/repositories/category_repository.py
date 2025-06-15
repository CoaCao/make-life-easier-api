from typing import Optional

from sqlalchemy.orm import Query, Session
from starlette import status
from starlette.exceptions import HTTPException

from src.exceptions.category_exceptions import CategoryExistException, CategoryNotFoundException
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


def get_by_id(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id, Category.enabled == 1).first()
    if not category:
        raise CategoryNotFoundException(f"Category not found with category_id={category_id}")

    return category


def add(db: Session, category: CategoryAdd):
    existing = db.query(Category).filter(Category.enabled == 1, Category.name == category.name).first()

    if existing:
        raise CategoryExistException("Category name already exists.")

    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def edit(db: Session, category_id: int, category: CategoryEdit):
    db_category = get_by_id(db, category_id)

    if category.name != db_category.name:
        existing = db.query(Category).filter(
            Category.enabled == 1,
            Category.name == category.name,
            Category.id != category_id  # Exclude itself
        ).first()

        if existing:
            raise CategoryExistException("Category name already exists.")

    for field, value in category.model_dump().items():
        setattr(db_category, field, value)
    db.commit()
    db.refresh(db_category)
    return db_category


def remove(db: Session, category_id: int):
    db_category = get_by_id(db, category_id)
    if db_category:
        db_category.enabled = 0
        db.commit()
