

<h1 id="make-life-easier-api-feature">Feature</h1>

## Total spending

<a id="opIdtotal_spending_features_products_spending_get"></a>

`GET /features/products/spending`


<h3 id="total_spending_features_products_spending_get-parameters">Parameters</h3>

| Name      | In    | Type   | Required | Description |
|-----------|-------|--------|----------|-------------|
| from_date | query | string | true     | Start date  |
| to_date   | query | string    | true    | End date    |

<h3 id="total_spending_features_products_spending_get-responses">Responses</h3>

| Status | Meaning              | Description         | Schema                                            |
|--------|----------------------|---------------------|---------------------------------------------------|
| 200    | OK                   | Successful Response | [TotalSpending](#schematotalspending)             |


> 200 Response

```json
{
  "total_spent": "string"
}
```

> Example responses
```json
{
  "total_spent": "1522.50"
}
```

## Get spending on categories

<a id="opIdget_spending_features_categories_spending_get"></a>

> Code samples

`GET /features/categories/spending`


<h3 id="get_spending_features_categories_spending_get-parameters">Parameters</h3>

|Name|In| Type   | Required |Description|
|---|---|--------|----------|---|
|category_id|query| int    | false    |Filter by category ID|
|from_date|query| string | true     |Start date|
|to_date|query| string    | true    |End date|

<h3 id="get_spending_features_categories_spending_get-responses">Responses</h3>

|Status| Meaning                                                                  |Description|Schema|
|---|--------------------------------------------------------------------------|---|---|
|200| OK                                                                       |Successful Response|Inline|
|422| Unprocessable Entity |Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|


> 200 Response

```json
[
  {
    "category_id": 0,
    "category_name": "string",
    "total_spent": "string"
  }
]
```

> Example responses
```json
[
    {
        "category_id": 1,
        "category_name": "Food",
        "total_spent": "266.74"
    },
    {
        "category_id": 2,
        "category_name": "Drink",
        "total_spent": "503.17"
    },
    {
        "category_id": 3,
        "category_name": "Drug",
        "total_spent": "259.45"
    },
    {
        "category_id": 4,
        "category_name": "Cosmetic",
        "total_spent": "277.69"
    }
]
```
