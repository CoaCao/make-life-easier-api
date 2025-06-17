from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

import src.repositories.category_repository as repository
from src.core.database import get_db
from src.schemas.category_schema import CategoryAdd, CategoryEdit, CategoryListResponse, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=CategoryListResponse)
def get_all(name: str | None = Query(None), db: Session = Depends(get_db)):
    return repository.get_all(db, name=name)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return repository.get_by_id(db, category_id)


@router.post("/", response_model=CategoryResponse)
def add_category(category: CategoryAdd, db: Session = Depends(get_db)):
    return repository.add(db, category)


@router.put("/{category_id}", response_model=CategoryResponse)
def edit_category(category_id: int, category: CategoryEdit, db: Session = Depends(get_db)):
    return repository.edit(db, category_id, category)


@router.delete("/{category_id}")
def remove_category(category_id: int, db: Session = Depends(get_db)):
    repository.remove(db, category_id)

    return {"message": "Category deleted successfully"}
