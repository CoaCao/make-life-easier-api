from datetime import datetime, UTC

from sqlalchemy import Column, Integer, Numeric, String, Date

from src.core.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_date = Column(Date, default=datetime.now(UTC))
    enabled = Column(Integer, default=1)