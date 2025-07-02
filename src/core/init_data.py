import random
from datetime import date, timedelta
from decimal import Decimal

from sqlalchemy.orm import Session

from src.core.database import Base, engine, SessionLocal
from src.models.category_model import Category
from src.models.product_model import Product

# Create table if not exist
Base.metadata.create_all(bind=engine)

sample_categories = [
    {'id': 1, 'name': 'Food', 'enabled': 1},
    {'id': 2, 'name': 'Drink', 'enabled': 1},
    {'id': 3, 'name': 'Drug', 'enabled': 1},
    {'id': 4, 'name': 'Cosmetic', 'enabled': 1},
    {'id': 5, 'name': 'Supplement', 'enabled': 1}
]

# Generate 100 products, 20 for each category
sample_products = []
base_date = date.today()
for i in range(25):
    category_id = (i % 5) + 1  # 1 to 5
    product = {
        "id": i + 1,
        "name": f"Product {i + 1}",
        "category_id": category_id,
        "image_url": f"https://example.com/images/product_{i + 1}.jpg",
        "price": Decimal(f"{random.uniform(1.0, 100.0):.2f}"),
        "expiration_date": base_date + timedelta(days=random.randint(30, 365)),
        "purchased_date": base_date - timedelta(days=random.randint(0, 30)),
        "enabled": 1,
        "is_used": 0,
    }
    sample_products.append(product)


def seed_data():
    db: Session = SessionLocal()
    try:
        for item in sample_categories:
            db.add(Category(**item))
        db.commit()
        print("✅ Inserted 5 sample Categories.")

        for item in sample_products:
            db.add(Product(**item))
        db.commit()
        print("✅ Inserted 25 sample products.")
    except Exception as e:
        db.rollback()
        print("❌ Error inserting products:", e)
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
