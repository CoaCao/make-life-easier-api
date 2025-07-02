from typing import Awaitable, Callable, cast

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.exceptions.category_exceptions import CategoryExistException, CategoryNotFoundException
from src.exceptions.product_exceptions import ProductNotFoundException


async def custom_422_handler(
        request: Request, exc: RequestValidationError
) -> Response:
    detail_message = ""
    if exc.errors():
        for error in exc.errors():
            detail_message = detail_message + f"'{error['loc'][1]}': {error['msg']}. "
    else:
        detail_message = "Invalid input"

    return JSONResponse(
        status_code=400,
        content={
            "message": "Bad Request",
            "detail": detail_message,
        }
    )


async def product_not_found_handler(
        request: Request, exc: ProductNotFoundException
) -> Response:
    return JSONResponse(
        status_code=404,
        content={
            "message": "Data not found",
            "detail": exc.message
        }
    )


async def category_not_found_handler(
        request: Request, exc: CategoryNotFoundException
) -> Response:
    return JSONResponse(
        status_code=404,
        content={
            "message": "Data not found",
            "detail": exc.message
        }
    )


async def category_exist_handler(
        request: Request, exc: CategoryExistException
) -> Response:
    return JSONResponse(
        status_code=400,
        content={
            "message": "Bad Request",
            "detail": exc.message
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
        CategoryNotFoundException,
        cast(Callable[[Request, Exception], Awaitable[Response]], category_not_found_handler),
    )

    app.add_exception_handler(
        CategoryExistException,
        cast(Callable[[Request, Exception], Awaitable[Response]], category_exist_handler),
    )

    app.add_exception_handler(
        StarletteHTTPException,
        cast(Callable[[Request, Exception], Awaitable[Response]], http_exception_handler),
    )

    app.add_exception_handler(
        Exception,
        cast(Callable[[Request, Exception], Awaitable[Response]], general_exception_handler),
    )
