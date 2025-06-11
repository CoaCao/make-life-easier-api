from datetime import date
from sqlalchemy.orm import Session
from src.core.database import Base, SessionLocal, engine
from src.models.product_model import Product


# Create table if not exist
Base.metadata.create_all(bind=engine)

sample_products = [
    {
        "name": "Omega-3 Fish Oil",
        "image_url": "https://example.com/images/omega3.jpg",
        "expiration_date": date(2026, 5, 1),
        "purchased_date": date(2025, 6, 1),
    },
    {
        "name": "Vitamin C 1000mg",
        "image_url": "https://example.com/images/vitamin-c.jpg",
        "expiration_date": date(2025, 12, 20),
        "purchased_date": date(2025, 6, 1),
    },
    {
        "name": "Collagen Peptides",
        "image_url": "https://example.com/images/collagen.jpg",
        "expiration_date": date(2027, 3, 15),
        "purchased_date": date(2025, 6, 1),
    },
    {
        "name": "Multivitamin Gummies",
        "image_url": "https://example.com/images/gummies.jpg",
        "expiration_date": date(2025, 11, 5),
        "purchased_date": date(2025, 6, 2),
    },
    {
        "name": "Zinc + D3 Complex",
        "image_url": "https://example.com/images/zinc-d3.jpg",
        "expiration_date": date(2025, 10, 10),
        "purchased_date": date(2025, 6, 2),
    },
    {
        "name": "Hair Growth Serum",
        "image_url": "https://example.com/images/hair-serum.jpg",
        "expiration_date": date(2026, 6, 30),
        "purchased_date": date(2025, 6, 2),
    },
    {
        "name": "Hydrating Facial Cream",
        "image_url": "https://example.com/images/facial-cream.jpg",
        "expiration_date": date(2027, 1, 1),
        "purchased_date": date(2025, 6, 3),
    },
    {
        "name": "Retinol Night Serum",
        "image_url": "https://example.com/images/retinol.jpg",
        "expiration_date": date(2026, 9, 30),
        "purchased_date": date(2025, 6, 3),
    },
    {
        "name": "Turmeric Capsules",
        "image_url": "https://example.com/images/turmeric.jpg",
        "expiration_date": date(2026, 8, 25),
        "purchased_date": date(2025, 6, 3),
    },
    {
        "name": "Magnesium Glycinate",
        "image_url": "https://example.com/images/magnesium.jpg",
        "expiration_date": date(2026, 2, 15),
        "purchased_date": date(2025, 6, 4),
    },
    {
        "name": "Herbal Sleep Aid",
        "image_url": "https://example.com/images/sleep-aid.jpg",
        "expiration_date": date(2025, 9, 1),
        "purchased_date": date(2025, 6, 4),
    },
    {
        "name": "Vitamin D3 5000 IU",
        "image_url": "https://example.com/images/d3.jpg",
        "expiration_date": date(2027, 4, 10),
        "purchased_date": date(2025, 6, 4),
    },
    {
        "name": "Eye Repair Cream",
        "image_url": "https://example.com/images/eye-cream.jpg",
        "expiration_date": date(2026, 12, 1),
        "purchased_date": date(2025, 6, 5),
    },
    {
        "name": "Probiotic 30 Billion CFU",
        "image_url": "https://example.com/images/probiotic.jpg",
        "expiration_date": date(2026, 7, 20),
        "purchased_date": date(2025, 6, 5),
    },
    {
        "name": "Niacinamide Toner",
        "image_url": "https://example.com/images/toner.jpg",
        "expiration_date": date(2026, 11, 11),
        "purchased_date": date(2025, 6, 5),
    },
    {
        "name": "Whey Protein Isolate",
        "image_url": "https://example.com/images/whey.jpg",
        "expiration_date": date(2026, 10, 1),
        "purchased_date": date(2025, 6, 6),
    },
    {
        "name": "Joint Support Formula",
        "image_url": "https://example.com/images/joint-support.jpg",
        "expiration_date": date(2026, 5, 5),
        "purchased_date": date(2025, 6, 6),
    },
    {
        "name": "Hydrating Lip Balm",
        "image_url": "https://example.com/images/lip-balm.jpg",
        "expiration_date": date(2027, 3, 18),
        "purchased_date": date(2025, 6, 6),
    },
    {
        "name": "Green Tea Extract",
        "image_url": "https://example.com/images/green-tea.jpg",
        "expiration_date": date(2026, 8, 1),
        "purchased_date": date(2025, 6, 7),
    },
    {
        "name": "Skin Brightening Serum",
        "image_url": "https://example.com/images/brightening.jpg",
        "expiration_date": date(2027, 6, 1),
        "purchased_date": date(2025, 6, 7),
    },
]


def seed_data():
    db: Session = SessionLocal()
    try:
        for item in sample_products:
            product = Product(**item)
            db.add(product)
        db.commit()
        print("✅ Inserted 20 sample products.")
    except Exception as e:
        db.rollback()
        print("❌ Error inserting products:", e)
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
