from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.core.database import SessionLocal
from src.exceptions.product_exceptions import ProductNotFoundException
from src.schemas.product_schema import ProductListResponse, ProductResponse, ProductAdd, ProductEdit
import src.repositories.product_repository as repository

router = APIRouter(prefix="/products", tags=["Products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=ProductListResponse)
def get_products(skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=1),
        sort_by: str = Query("expiration_date", pattern="^(name|expiration_date|purchased_date)$"),
        sort_order: str = Query("asc", pattern="^(asc|desc)$"),
        name: str| None = Query(None),
        days_to_expire: int | None = Query(None, ge=0),
        db: Session = Depends(get_db)):
    return repository.get_all(db, skip=skip, limit=limit,
                              sort_by=sort_by, sort_order=sort_order,
                              name=name,
                              days_to_expire=days_to_expire)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = repository.get_by_id(db, product_id)
    if not product:
        raise ProductNotFoundException(product_id=product_id)
    return product


@router.post("/", response_model=ProductResponse)
def add_product(product: ProductAdd, db: Session = Depends(get_db)):
    return repository.add(db, product)


@router.put("/{product_id}", response_model=ProductResponse)
def edit_product(product_id: int, product: ProductEdit, db: Session = Depends(get_db)):
    edited = repository.edit(db, product_id, product)
    if not edited:
        raise ProductNotFoundException(product_id=product_id)
    return edited


@router.delete("/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    removed = repository.remove(db, product_id)
    if not removed:
        raise ProductNotFoundException(product_id=product_id)
    return {"message": "Product deleted successfully"}
