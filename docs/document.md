<!-- Generator: Widdershins v4.0.1 -->

<h1 id="make-life-easier-api">Make Life Easier API v1.0</h1>

<h1 id="make-life-easier-api-products">Products</h1>

## Search Products

<a id="opIdget_products__get"></a>

### `GET /products/`

<h3 id="get_products_products__get-parameters">Parameters</h3>

| Name           | In    | Type         | Required | Description                       |
|----------------|-------|--------------|----------|-----------------------------------|
| skip           | query | integer      | false    | none                              |
| limit          | query | integer      | false    | none                              |
| sort_by        | query | string       | false    | name \| expiry_date \| added_date |
| sort_order     | query | string       | false    | asc \| desc                       |
| name           | query | string(date) | false    | none                              |
| days_to_expire | query | string(date) | false    | none                              |

<h3 id="get_products_products__get-responses">Responses</h3>

| Status | Meaning              | Description         | Schema                                            |
|--------|----------------------|---------------------|---------------------------------------------------|
| 200    | OK                   | Successful Response | [ProductListResponse](#schemaproductlistresponse) |
| 422    | Unprocessable Entity | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |

> 200 Response

```json
{
  "total": 0,
  "items": [
    {
      "id": 0,
      "name": "string",
      "image_url": "string",
      "expiry_date": "2019-08-24",
      "added_date": "2019-08-24"
    }
  ]
}
```

> Example responses

```json
{
  "total": 3,
  "items": [
    {
      "id": 25,
      "name": "Vitamin C 1000",
      "image_url": "https://example.com/images/vitamin1.jpg",
      "expiry_date": "2025-07-10",
      "added_date": "2025-06-05"
    },
    {
      "id": 26,
      "name": "Vitamin E 100",
      "image_url": "https://example.com/images/vitamin2.jpg",
      "expiry_date": "2025-07-10",
      "added_date": "2025-06-05"
    },
    {
      "id": 27,
      "name": "Vitamin E 100",
      "image_url": "https://example.com/images/vitamin3.jpg",
      "expiry_date": "2025-07-10",
      "added_date": "2025-06-05"
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
  "image_url": "string",
  "expiry_date": "2019-08-24"
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
  "image_url": "string",
  "expiry_date": "2019-08-24",
  "added_date": "2019-08-24"
}
```

> Example responses

```json
{
  "id": 30,
  "name": "Canxi 100",
  "image_url": "https://example.com/images/canxi.jpg",
  "expiry_date": "2026-02-19",
  "added_date": "2025-06-07"
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
  "image_url": "string",
  "expiry_date": "2019-08-24",
  "added_date": "2019-08-24"
}
```

> Example responses

```json
{
  "id": 30,
  "name": "Canxi 100",
  "image_url": "https://example.com/images/canxi.jpg",
  "expiry_date": "2026-02-19",
  "added_date": "2025-06-07"
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
  "image_url": "string",
  "expiry_date": "2019-08-24"
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
  "image_url": "string",
  "expiry_date": "2019-08-24",
  "added_date": "2019-08-24"
}
```

> Example responses

```json
{
  "id": 30,
  "name": "Canxi 100",
  "image_url": "https://example.com/images/canxi.jpg",
  "expiry_date": "2026-02-19",
  "added_date": "2025-06-07"
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
  "message": "Product deleted"
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
  "image_url": "string",
  "expiry_date": "2019-08-24"
}

```

### Properties

| Name        | Type         | Required | Restrictions | Description |
|-------------|--------------|----------|--------------|-------------|
| name        | string       | true     | none         | none        |
| image_url   | string       | true     | none         | none        |
| expiry_date | string(date) | true     | none         | none        |

<h2 id="tocS_ProductEdit">ProductEdit</h2>
<!-- backwards compatibility -->
<a id="schemaproductedit"></a>

```json
{
  "name": "string",
  "image_url": "string",
  "expiry_date": "2019-08-24"
}

```

### Properties

| Name        | Type         | Required | Restrictions | Description |
|-------------|--------------|----------|--------------|-------------|
| name        | string       | true     | none         | none        |
| image_url   | string       | true     | none         | none        |
| expiry_date | string(date) | true     | none         | none        |

<h2 id="tocS_ProductListResponse">ProductListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaproductlistresponse"></a>

```json
{
  "total": 0,
  "items": [
    {
      "id": 0,
      "name": "string",
      "image_url": "string",
      "expiry_date": "2019-08-24",
      "added_date": "2019-08-24"
    }
  ]
}

```

### Properties

| Name  | Type                                        | Required | Restrictions | Description |
|-------|---------------------------------------------|----------|--------------|-------------|
| total | integer                                     | true     | none         | none        |
| items | [[ProductResponse](#schemaproductresponse)] | true     | none         | none        |

<h2 id="tocS_ProductResponse">ProductResponse</h2>
<!-- backwards compatibility -->
<a id="schemaproductresponse"></a>

```json
{
  "id": 0,
  "name": "string",
  "image_url": "string",
  "expiry_date": "2019-08-24",
  "added_date": "2019-08-24"
}

```

### Properties

| Name        | Type         | Required | Restrictions | Description |
|-------------|--------------|----------|--------------|-------------|
| id          | integer      | true     | none         | none        |
| name        | string       | true     | none         | none        |
| image_url   | string       | true     | none         | none        |
| expiry_date | string(date) | true     | none         | none        |
| added_date  | string(date) | true     | none         | none        |

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
