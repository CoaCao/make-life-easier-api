from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

import src.repositories.product_repository as repository
from src.core.database import get_db, SessionLocal
from src.schemas.product_schema import ProductAdd, ProductEdit, ProductListResponse, ProductResponse
from src.utils.factory import to_product_response

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=ProductListResponse)
def get_products(skip: int = Query(0, ge=0),
        limit: int = Query(None, ge=1),
        sort_by: str = Query("expiration_date", pattern="^(name|expiration_date|purchased_date|category_name)$"),
        sort_order: str = Query("asc", pattern="^(asc|desc)$"),
        category_id: int | None = Query(None, ge=1),
        name: str | None = Query(None),
        days_to_expire: int | None = Query(None, ge=0),
        is_used: int | None = Query(None, ge=0),
        db: Session = Depends(get_db)):
    return repository.get_all(db, skip=skip, limit=limit,
                              sort_by=sort_by, sort_order=sort_order,
                              category_id=category_id,
                              name=name,
                              days_to_expire=days_to_expire,
                              is_used=is_used)


@router.get("/{product_id}", response_model=ProductResponse)
def get_by_id(product_id: int, db: Session = Depends(get_db)):
    product = repository.get_by_id(db, product_id)

    return to_product_response(product)


@router.post("/", response_model=ProductResponse)
def add_product(product: ProductAdd, db: Session = Depends(get_db)):
    product = repository.add(db, product)

    return to_product_response(repository.get_by_id(db, product.id))


@router.put("/{product_id}", response_model=ProductResponse)
def edit_product(product_id: int, product: ProductEdit, db: Session = Depends(get_db)):
    repository.edit(db, product_id, product)

    return to_product_response(repository.get_by_id(db, product_id))


@router.delete("/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    repository.remove(db, product_id)

    return {"message": "Product deleted successfully"}
