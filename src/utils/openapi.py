from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="My API",
        version="1.0.0",
        description="API with custom error responses in docs",
        routes=app.routes,
    )

    error_responses = {
        "403": {
            "description": "Invalid input",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Invalid input",
                        "detail": "Input should be a valid integer, unable to parse string as an integer"
                    }
                }
            },
        },
        "404": {
            "description": "Path not found",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Path not found",
                        "detail": "No route found for GET /not-found"
                    }
                }
            },
        },
        "405": {
            "description": "Method not allowed",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Method not allowed",
                        "detail": "The method POST is not allowed for path /products"
                    }
                }
            },
        },
        "500": {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Internal server error",
                        "detail": "Exception message"
                    }
                }
            },
        },
    }

    # Gắn thêm response vào từng path-method
    for path in openapi_schema["paths"].values():
        for method in path.values():
            responses = method.setdefault("responses", {})
            for code, response in error_responses.items():
                responses.setdefault(code, response)

    app.openapi_schema = openapi_schema
    return app.openapi_schema
