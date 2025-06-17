<h1 id="make-life-easier-api-feature">Feature</h1>

## Total purchased

<a id="opIdtotal_purchased_features_products_purchased_get"></a>

`GET /features/products/purchased`

<h3 id="total_purchased_features_products_purchased_get-parameters">Parameters</h3>

| Name      | In    | Type | Required | Description             |
|-----------|-------|------|----------|-------------------------|
| from_date | query | any  | true     | Start date (yyyy-mm-dd) |
| to_date   | query | any  | true     | End date (yyyy-mm-dd)   |

<h3 id="total_purchased_features_products_purchased_get-responses">Responses</h3>

| Status | Meaning | Description         | Schema                                  |
|--------|---------|---------------------|-----------------------------------------|
| 200    | OK      | Successful Response | [TotalPurchased](#schematotalpurchased) |

> 200 Response

```json
{
  "total_purchased": "string"
}
```

> Example responses

```json
{
  "total_purchased": "1522.50"
}
```

## Get purchased on categories

<a id="opIdget_purchased_features_categories_purchased_get"></a>

> Code samples

`GET /features/categories/purchased`

<h3 id="get_purchased_features_categories_purchased_get-parameters">Parameters</h3>

| Name        | In    | Type | Required | Description             |
|-------------|-------|------|----------|-------------------------|
| category_id | query | any  | false    | Filter by category ID   |
| from_date   | query | any  | true     | Start date (yyyy-mm-dd) |
| to_date     | query | any  | true     | End date (yyyy-mm-dd)   |

<h3 id="get_purchased_features_categories_purchased_get-responses">Responses</h3>

| Status | Meaning              | Description         | Schema                                            |
|--------|----------------------|---------------------|---------------------------------------------------|
| 200    | OK                   | Successful Response | Inline                                            |
| 422    | Unprocessable Entity | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |

> 200 Response

```json
[
  {
    "category_id": 0,
    "category_name": "string",
    "total_purchased": "string"
  }
]
```

> Example responses

```json
[
  {
    "category_id": 1,
    "category_name": "Food",
    "total_purchased": "266.74"
  },
  {
    "category_id": 2,
    "category_name": "Drink",
    "total_purchased": "503.17"
  },
  {
    "category_id": 3,
    "category_name": "Drug",
    "total_purchased": "259.45"
  },
  {
    "category_id": 4,
    "category_name": "Cosmetic",
    "total_purchased": "277.69"
  }
]
```
