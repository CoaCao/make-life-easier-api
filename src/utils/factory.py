from src.schemas.product_schema import ProductResponse


def to_product_response(result) -> ProductResponse:
    product, category_name = result
    return ProductResponse(
        id=product.id,
        name=product.name,
        category_id=product.category_id,
        category_name=category_name,
        image_url=product.image_url,
        price=product.price,
        expiration_date=product.expiration_date,
        purchased_date=product.purchased_date,
    )