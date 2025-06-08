from typing import Callable, Awaitable, cast
from fastapi import Request
from fastapi.responses import JSONResponse, Response
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.exceptions.product_exceptions import ProductNotFoundException


async def custom_422_handler(
        request: Request, exc: RequestValidationError
) -> Response:
    return JSONResponse(
        status_code=400,
        content={
            "message": "Bad Request",
            "detail": exc.errors()[0]["msg"] if exc.errors() else "Invalid input",
        }
    )


async def product_not_found_handler(
        request: Request, exc: ProductNotFoundException
) -> Response:
    return JSONResponse(
        status_code=404,
        content={
            "message": "Data not found",
            "detail": f"Product Id {exc.product_id} not found"
        }
    )


async def http_exception_handler(
        request: Request, exc: StarletteHTTPException
) -> Response:
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={
                "message": "Path not found",
                "detail": f"No route found for {request.method} {request.url.path}"
            },
        )
    elif exc.status_code == 405:
        return JSONResponse(
            status_code=405,
            content={
                "message": "Method not allowed",
                "detail": f"The method {request.method} is not allowed for path {request.url.path}"
            },
        )
    else:
        return JSONResponse(
            status_code=500,
            content={
                # "message": exc.detail or "HTTP error",
                "message": "Internal server error",
                "detail": f"{request.method} {request.url.path}"
            },
        )


async def general_exception_handler(
        request: Request, exc: Exception
) -> Response:
    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal server error",
            "detail": str(exc)
        }
    )


def register_exception_handlers(app):
    app.add_exception_handler(
        RequestValidationError,
        cast(Callable[[Request, Exception], Awaitable[Response]], custom_422_handler),
    )

    app.add_exception_handler(
        ProductNotFoundException,
        cast(Callable[[Request, Exception], Awaitable[Response]], product_not_found_handler),
    )

    app.add_exception_handler(
        StarletteHTTPException,
        cast(Callable[[Request, Exception], Awaitable[Response]], http_exception_handler),
    )

    app.add_exception_handler(
        Exception,
        cast(Callable[[Request, Exception], Awaitable[Response]], general_exception_handler),
    )
