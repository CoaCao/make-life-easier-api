from datetime import date
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

import src.repositories.product_repository as repository
from src.core.database import SessionLocal
from src.schemas.product_schema import SpendingByCategory, TotalSpending

router = APIRouter(prefix="/features", tags=["Feature"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/categories/spending", response_model=List[SpendingByCategory])
def get_spending(category_id: Optional[int] = Query(None, description="Filter by category ID"),
        from_date: Optional[date] = Query(..., description="Start date (yyyy-mm-dd)"),
        to_date: Optional[date] = Query(..., description="End date (yyyy-mm-dd)"),
        db: Session = Depends(get_db)):
    return repository.get_categories_spending(db, from_date, to_date, category_id)


@router.get("/products/spending", response_model=TotalSpending)
def total_spending(
        from_date: Optional[date] = Query(..., description="Start date (yyyy-mm-dd)"),
        to_date: Optional[date] = Query(..., description="End date (yyyy-mm-dd)"),
        db: Session = Depends(get_db)
):
    total = repository.get_total_spending(db, from_date, to_date)
    return {"total_spent": total}
