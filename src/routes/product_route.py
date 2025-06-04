from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.core.database import SessionLocal
from src.schemas.product_schema import ProductResponse, ProductAdd, ProductEdit
import src.repositories.product_repository as repository
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ProductResponse])
def get_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    sort_by: str = Query("expiry_date", pattern="^(name|expiry_date|added_date)$"),
    sort_order: str = Query("asc", pattern="^(asc|desc)$"),
    db: Session = Depends(get_db)
):
    return repository.get_all(db, skip=skip, limit=limit, sort_by=sort_by, sort_order=sort_order)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = repository.get_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=ProductResponse)
def add_product(product: ProductAdd, db: Session = Depends(get_db)):
    return repository.add(db, product)

@router.put("/{product_id}", response_model=ProductResponse)
def edit_product(product_id: int, product: ProductEdit, db: Session = Depends(get_db)):
    edited = repository.edit(db, product_id, product)
    if not edited:
        raise HTTPException(status_code=404, detail="Product not found")
    return edited

@router.delete("/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    removed = repository.remove(db, product_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}
