from fastapi import FastAPI
from src.core.database import Base, engine
from src.exceptions.handler_exception import register_exception_handlers
from src.routes import category_route, product_route

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Make Life Easier API", version="1.0", description="Make Life Easier API")
register_exception_handlers(app)
app.include_router(product_route.router)
app.include_router(category_route.router)

