from datetime import datetime, UTC

from sqlalchemy import Column, Integer, String, Date

from src.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image_url = Column(String)
    expiry_date = Column(Date)
    added_date = Column(Date, default=datetime.now(UTC))
    enabled = Column(Integer, default=1)
