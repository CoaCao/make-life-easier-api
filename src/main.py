from fastapi import FastAPI
from src.core.database import Base, engine
from src.routes import product_route

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Make Life Easier API", version="1.0", description="Make Life Easier API")
app.include_router(product_route.router)
