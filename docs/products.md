<!-- Generator: Widdershins v4.0.1 -->

<h1 id="make-life-easier-api">Make Life Easier API v1.0</h1>

<h1 id="make-life-easier-api-products">Products</h1>

## Search Products

<a id="opIdget_products__get"></a>

### `GET /products/`

<h3 id="get_products_products__get-parameters">Parameters</h3>

| Name           | In    | Type    | Required | Description                       |
|----------------|-------|---------|----------|-----------------------------------|
| skip           | query | integer | false    | none                              |
| limit          | query | integer | false    | none                              |
| sort_by        | query | string  | false    | name \| expiry_date \| added_date |
| sort_order     | query | string  | false    | asc \| desc                       |
| category_id    | query | integer | false    | none                              |
| name           | query | string  | false    | none                              |
| days_to_expire | query | any     | false    | none                              |

<h3 id="get_products_products__get-responses">Responses</h3>

| Status | Meaning              | Description         | Schema                                            |
|--------|----------------------|---------------------|---------------------------------------------------|
| 200    | OK                   | Successful Response | [ProductListResponse](#schemaproductlistresponse) |
| 422    | Unprocessable Entity | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |

> 200 Response

```json
{
  "total_available": 0,
  "total_return": 0,
  "results": [
    {
      "id": 0,
      "name": "string",
      "category_id": 0,
      "category_name": "string",
      "image_url": "string",
      "price": "string",
      "expiration_date": "2019-08-24",
      "purchased_date": "2019-08-24"
    }
  ]
}
```

> Example responses

```json
{
  "total_available": 9,
  "total_return": 3,
  "results": [
    {
      "id": 2,
      "name": "Product 2",
      "category_id": 2,
      "category_name": "Drink",
      "image_url": "https://example.com/images/product_2.jpg",
      "price": "11.45",
      "expiration_date": "2025-10-13",
      "purchased_date": "2025-06-09"
    },
    {
      "id": 7,
      "name": "Product 7",
      "category_id": 2,
      "category_name": "Drink",
      "image_url": "https://example.com/images/product_7.jpg",
      "price": "79.14",
      "expiration_date": "2026-01-31",
      "purchased_date": "2025-06-08"
    },
    {
      "id": 12,
      "name": "Product 12",
      "category_id": 2,
      "category_name": "Drink",
      "image_url": "https://example.com/images/product_12.jpg",
      "price": "91.36",
      "expiration_date": "2026-01-01",
      "purchased_date": "2025-05-26"
    }
  ]
}
```

## Add Product

<a id="opIdadd_product__post"></a>

### `POST /products/`

> Body parameter

```json
{
  "name": "string",
  "category_id": 0,
  "image_url": "string",
  "price": 0,
  "expiration_date": "2019-08-24"
}
```

<h3 id="add_product_products__post-parameters">Parameters</h3>

| Name | In   | Type                            | Required | Description |
|------|------|---------------------------------|----------|-------------|
| body | body | [ProductAdd](#schemaproductadd) | true     | none        |

<h3 id="add_product_products__post-responses">Responses</h3>

| Status | Meaning              | Description         | Schema                                            |
|--------|----------------------|---------------------|---------------------------------------------------|
| 200    | OK                   | Successful Response | [ProductResponse](#schemaproductresponse)         |
| 422    | Unprocessable Entity | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "category_id": 0,
  "category_name": "string",
  "image_url": "string",
  "price": "string",
  "expiration_date": "2019-08-24",
  "purchased_date": "2019-08-24"
}
```

> Example responses

```json
{
  "id": 28,
  "name": "Chicken Snack",
  "category_id": 4,
  "category_name": "Cosmetic",
  "image_url": "https://example.com/images/ChickenSnack.jpg",
  "price": "5.20",
  "expiration_date": "2025-08-18",
  "purchased_date": "2025-06-11"
}
```

## Get Product By Id

<a id="opIdget_product_products__product_id__get"></a>

### `GET /products/{product_id}`

<h3 id="get_product_products__product_id__get-parameters">Parameters</h3>

| Name       | In   | Type    | Required | Description |
|------------|------|---------|----------|-------------|
| product_id | path | integer | true     | none        |

<h3 id="get_product_products__product_id__get-responses">Responses</h3>

| Status | Meaning              | Description         | Schema                                            |
|--------|----------------------|---------------------|---------------------------------------------------|
| 200    | OK                   | Successful Response | [ProductResponse](#schemaproductresponse)         |
| 422    | Unprocessable Entity | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "category_id": 0,
  "category_name": "string",
  "image_url": "string",
  "price": "string",
  "expiration_date": "2019-08-24",
  "purchased_date": "2019-08-24"
}
```

> Example responses

```json
{
  "id": 28,
  "name": "Chicken Snack",
  "category_id": 4,
  "category_name": "Cosmetic",
  "image_url": "https://example.com/images/ChickenSnack.jpg",
  "price": "5.20",
  "expiration_date": "2025-08-18",
  "purchased_date": "2025-06-11"
}
```

## Edit Product

<a id="opIdedit_product__put"></a>

### `PUT /products/{product_id}`

<h3 id="edit_product_products__product_id__put-parameters">Parameters</h3>

| Name       | In   | Type                              | Required | Description |
|------------|------|-----------------------------------|----------|-------------|
| product_id | path | integer                           | true     | none        |
| body       | body | [ProductEdit](#schemaproductedit) | true     | none        |

> Body parameter

```json
{
  "name": "string",
  "category_id": 0,
  "image_url": "string",
  "price": 0,
  "expiration_date": "2019-08-24"
}
```

<h3 id="edit_product_products__product_id__put-responses">Responses</h3>

| Status | Meaning              | Description         | Schema                                            |
|--------|----------------------|---------------------|---------------------------------------------------|
| 200    | OK                   | Successful Response | [ProductResponse](#schemaproductresponse)         |
| 422    | Unprocessable Entity | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "category_id": 0,
  "category_name": "string",
  "image_url": "string",
  "price": "string",
  "expiration_date": "2019-08-24",
  "purchased_date": "2019-08-24"
}
```

> Example responses

```json
{
  "id": 34,
  "name": "Chocolate Snack",
  "category_id": 1,
  "category_name": "Food",
  "image_url": "https://example.com/images/Snack.jpg",
  "price": "45.20",
  "expiration_date": "2025-07-18",
  "purchased_date": "2025-06-17"
}
```

## Remove Product

<a id="opIdremove_product__delete"></a>

### `DELETE /products/{product_id}`

<h3 id="remove_product_products__product_id__delete-parameters">Parameters</h3>

| Name       | In   | Type    | Required | Description |
|------------|------|---------|----------|-------------|
| product_id | path | integer | true     | none        |

<h3 id="remove_product_products__product_id__delete-responses">Responses</h3>

| Status | Meaning              | Description         | Schema                                            |
|--------|----------------------|---------------------|---------------------------------------------------|
| 200    | OK                   | Successful Response | Inline                                            |
| 422    | Unprocessable Entity | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |

> 200 Response

```json
{
  "message": "string"
}
```

> Example responses

```json
{
  "message": "Product deleted successfully"
}
```

# Schemas

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

### Properties

| Name   | Type                                        | Required | Restrictions | Description |
|--------|---------------------------------------------|----------|--------------|-------------|
| detail | [[ValidationError](#schemavalidationerror)] | false    | none         | none        |

<h2 id="tocS_ProductAdd">ProductAdd</h2>
<!-- backwards compatibility -->
<a id="schemaproductadd"></a>

```json
{
  "name": "string",
  "category_id": 0,
  "image_url": "string",
  "price": 0,
  "expiration_date": "2019-08-24"
}

```

### Properties

| Name        | Type    | Required | Restrictions | Description |
|-------------|---------|----------|--------------|-------------|
| name        | string  | true     | none         | none        |
| category_id | integer | true     | none         | none        |
| image_url   | string  | true     | none         | none        |
| price       | any     | true     | none         | none        |

<h2 id="tocS_ProductEdit">ProductEdit</h2>
<!-- backwards compatibility -->
<a id="schemaproductedit"></a>

```json
{
  "name": "string",
  "category_id": 0,
  "image_url": "string",
  "price": 0,
  "expiration_date": "2019-08-24"
}

```

### Properties

| Name        | Type    | Required | Restrictions | Description |
|-------------|---------|----------|--------------|-------------|
| name        | string  | true     | none         | none        |
| category_id | integer | true     | none         | none        |
| image_url   | string  | true     | none         | none        |
| price       | any     | true     | none         | none        |

<h2 id="tocS_ProductListResponse">ProductListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaproductlistresponse"></a>

```json
{
  "total_available": 0,
  "total_return": 0,
  "results": [
    {
      "id": 0,
      "name": "string",
      "category_id": 0,
      "category_name": "string",
      "image_url": "string",
      "price": "string",
      "expiration_date": "2019-08-24",
      "purchased_date": "2019-08-24"
    }
  ]
}

```

### Properties

| Name            | Type                                        | Required | Restrictions | Description |
|-----------------|---------------------------------------------|----------|--------------|-------------|
| total_available | integer                                     | true     | none         | none        |
| total_return    | integer                                     | true     | none         | none        |
| results         | [[ProductResponse](#schemaproductresponse)] | true     | none         | none        |

<h2 id="tocS_ProductResponse">ProductResponse</h2>
<!-- backwards compatibility -->
<a id="schemaproductresponse"></a>

```json
{
  "id": 0,
  "name": "string",
  "category_id": 0,
  "category_name": "string",
  "image_url": "string",
  "price": "string",
  "expiration_date": "2019-08-24",
  "purchased_date": "2019-08-24"
}

```

### Properties

| Name            | Type         | Required | Restrictions | Description |
|-----------------|--------------|----------|--------------|-------------|
| id              | integer      | true     | none         | none        |
| name            | string       | true     | none         | none        |
| category_id     | integer      | true     | none         | none        |
| category_name   | string       | true     | none         | none        |
| image_url       | string       | true     | none         | none        |
| price           | string       | true     | none         | none        |
| expiration_date | string(date) | true     | none         | none        |
| purchased_date  | string(date) | true     | none         | none        |

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```
