from datetime import datetime, UTC

from sqlalchemy import Column, Integer, Numeric, String, Date

from src.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, index=True)
    image_url = Column(String)
    price = Column(Numeric(10, 2), default=0)
    expiration_date = Column(Date)
    purchased_date = Column(Date, default=datetime.now(UTC))
    enabled = Column(Integer, default=1)
    is_used = Column(Integer, default=0)