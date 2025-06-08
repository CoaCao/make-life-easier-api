from fastapi import FastAPI
from src.core.database import Base, engine
from src.exceptions.handlers import register_exception_handlers
from src.routes import product_route
from src.utils.openapi import custom_openapi

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Make Life Easier API", version="1.0", description="Make Life Easier API")

register_exception_handlers(app)
app.openapi = lambda: custom_openapi(app)
app.include_router(product_route.router)
