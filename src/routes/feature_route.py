from datetime import date
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

import src.repositories.feature_repository as repository
from src.core.database import get_db
from src.schemas.feature_schema import SpendingByCategory, TotalPurchased

router = APIRouter(prefix="/features", tags=["Feature"])


@router.get("/categories/purchased", response_model=List[SpendingByCategory])
def get_categories_purchased(category_id: Optional[int] = Query(None, description="Filter by category ID"),
        from_date: Optional[date] = Query(..., description="Start date (yyyy-mm-dd)"),
        to_date: Optional[date] = Query(..., description="End date (yyyy-mm-dd)"),
        db: Session = Depends(get_db)):

    return repository.get_categories_purchased(db, from_date, to_date, category_id)


@router.get("/products/purchased", response_model=TotalPurchased)
def get_products_purchased(
        from_date: Optional[date] = Query(..., description="Start date (yyyy-mm-dd)"),
        to_date: Optional[date] = Query(..., description="End date (yyyy-mm-dd)"),
        db: Session = Depends(get_db)
):
    total = repository.get_products_purchased(db, from_date, to_date)
    return {"total_purchased": total}
