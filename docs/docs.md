<!-- Generator: Widdershins v4.0.1 -->

<h1 id="make-life-easier-api">Make Life Easier API v1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Make Life Easier API

<h1 id="make-life-easier-api-products">Products</h1>

## get_products_products__get

<a id="opIdget_products_products__get"></a>

> Code samples

`GET /products/`

*Get Products*

<h3 id="get_products_products__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|skip|query|integer|false|none|
|limit|query|integer|false|none|
|sort_by|query|string|false|none|
|sort_order|query|string|false|none|
|name|query|any|false|none|
|days_to_expire|query|any|false|none|
|category_id|query|any|false|none|

> Example responses

> 200 Response

```json
{
  "total_available": 0,
  "total_return": 0,
  "items": [
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

<h3 id="get_products_products__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ProductListResponse](#schemaproductlistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## add_product_products__post

<a id="opIdadd_product_products__post"></a>

> Code samples

`POST /products/`

*Add Product*

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

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ProductAdd](#schemaproductadd)|true|none|

> Example responses

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

<h3 id="add_product_products__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ProductResponse](#schemaproductresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## get_product_products__product_id__get

<a id="opIdget_product_products__product_id__get"></a>

> Code samples

`GET /products/{product_id}`

*Get Product*

<h3 id="get_product_products__product_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|none|

> Example responses

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

<h3 id="get_product_products__product_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ProductResponse](#schemaproductresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## edit_product_products__product_id__put

<a id="opIdedit_product_products__product_id__put"></a>

> Code samples

`PUT /products/{product_id}`

*Edit Product*

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

<h3 id="edit_product_products__product_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|none|
|body|body|[ProductEdit](#schemaproductedit)|true|none|

> Example responses

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

<h3 id="edit_product_products__product_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ProductResponse](#schemaproductresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## remove_product_products__product_id__delete

<a id="opIdremove_product_products__product_id__delete"></a>

> Code samples

`DELETE /products/{product_id}`

*Remove Product*

<h3 id="remove_product_products__product_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="remove_product_products__product_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="remove_product_products__product_id__delete-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="make-life-easier-api-categories">Categories</h1>

## get_all_categories__get

<a id="opIdget_all_categories__get"></a>

> Code samples

`GET /categories/`

*Get All*

<h3 id="get_all_categories__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|query|any|false|none|

> Example responses

> 200 Response

```json
{
  "total": 0,
  "items": [
    {
      "id": 0,
      "name": "string",
      "created_date": "2019-08-24"
    }
  ]
}
```

<h3 id="get_all_categories__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[CategoryListResponse](#schemacategorylistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## add_category_categories__post

<a id="opIdadd_category_categories__post"></a>

> Code samples

`POST /categories/`

*Add Category*

> Body parameter

```json
{
  "name": "string"
}
```

<h3 id="add_category_categories__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CategoryAdd](#schemacategoryadd)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "created_date": "2019-08-24"
}
```

<h3 id="add_category_categories__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[CategoryResponse](#schemacategoryresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## get_category_categories__category_id__get

<a id="opIdget_category_categories__category_id__get"></a>

> Code samples

`GET /categories/{category_id}`

*Get Category*

<h3 id="get_category_categories__category_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|category_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "created_date": "2019-08-24"
}
```

<h3 id="get_category_categories__category_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[CategoryResponse](#schemacategoryresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## edit_category_categories__category_id__put

<a id="opIdedit_category_categories__category_id__put"></a>

> Code samples

`PUT /categories/{category_id}`

*Edit Category*

> Body parameter

```json
{
  "name": "string"
}
```

<h3 id="edit_category_categories__category_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|category_id|path|integer|true|none|
|body|body|[CategoryEdit](#schemacategoryedit)|true|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "created_date": "2019-08-24"
}
```

<h3 id="edit_category_categories__category_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[CategoryResponse](#schemacategoryresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## remove_category_categories__category_id__delete

<a id="opIdremove_category_categories__category_id__delete"></a>

> Code samples

`DELETE /categories/{category_id}`

*Remove Category*

<h3 id="remove_category_categories__category_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|category_id|path|integer|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="remove_category_categories__category_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="remove_category_categories__category_id__delete-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="make-life-easier-api-feature">Feature</h1>

## get_spending_features_categories_spending_get

<a id="opIdget_spending_features_categories_spending_get"></a>

> Code samples

`GET /features/categories/spending`

*Get Spending*

<h3 id="get_spending_features_categories_spending_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|category_id|query|any|false|Filter by category ID|
|from_date|query|any|false|Start date|
|to_date|query|any|false|End date|

> Example responses

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

<h3 id="get_spending_features_categories_spending_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_spending_features_categories_spending_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Spending Features Categories Spending Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Get Spending Features Categories Spending Get|[[SpendingByCategory](#schemaspendingbycategory)]|false|none|none|
|» SpendingByCategory|[SpendingByCategory](#schemaspendingbycategory)|false|none|none|
|»» category_id|integer|true|none|none|
|»» category_name|string|true|none|none|
|»» total_spent|string|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## total_spending_features_products_spending_get

<a id="opIdtotal_spending_features_products_spending_get"></a>

> Code samples

`GET /features/products/spending`

*Total Spending*

<h3 id="total_spending_features_products_spending_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|from_date|query|any|false|Start date|
|to_date|query|any|false|End date|

> Example responses

> 200 Response

```json
{
  "total_spent": "string"
}
```

<h3 id="total_spending_features_products_spending_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TotalSpending](#schematotalspending)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_CategoryAdd">CategoryAdd</h2>
<!-- backwards compatibility -->
<a id="schemacategoryadd"></a>
<a id="schema_CategoryAdd"></a>
<a id="tocScategoryadd"></a>
<a id="tocscategoryadd"></a>

```json
{
  "name": "string"
}

```

CategoryAdd

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|

<h2 id="tocS_CategoryEdit">CategoryEdit</h2>
<!-- backwards compatibility -->
<a id="schemacategoryedit"></a>
<a id="schema_CategoryEdit"></a>
<a id="tocScategoryedit"></a>
<a id="tocscategoryedit"></a>

```json
{
  "name": "string"
}

```

CategoryEdit

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|

<h2 id="tocS_CategoryListResponse">CategoryListResponse</h2>
<!-- backwards compatibility -->
<a id="schemacategorylistresponse"></a>
<a id="schema_CategoryListResponse"></a>
<a id="tocScategorylistresponse"></a>
<a id="tocscategorylistresponse"></a>

```json
{
  "total": 0,
  "items": [
    {
      "id": 0,
      "name": "string",
      "created_date": "2019-08-24"
    }
  ]
}

```

CategoryListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total|integer|true|none|none|
|items|[[CategoryResponse](#schemacategoryresponse)]|true|none|none|

<h2 id="tocS_CategoryResponse">CategoryResponse</h2>
<!-- backwards compatibility -->
<a id="schemacategoryresponse"></a>
<a id="schema_CategoryResponse"></a>
<a id="tocScategoryresponse"></a>
<a id="tocscategoryresponse"></a>

```json
{
  "id": 0,
  "name": "string",
  "created_date": "2019-08-24"
}

```

CategoryResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|none|
|name|string|true|none|none|
|created_date|string(date)|true|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

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

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ProductAdd">ProductAdd</h2>
<!-- backwards compatibility -->
<a id="schemaproductadd"></a>
<a id="schema_ProductAdd"></a>
<a id="tocSproductadd"></a>
<a id="tocsproductadd"></a>

```json
{
  "name": "string",
  "category_id": 0,
  "image_url": "string",
  "price": 0,
  "expiration_date": "2019-08-24"
}

```

ProductAdd

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|category_id|integer|true|none|none|
|image_url|string|true|none|none|
|price|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|expiration_date|string(date)|true|none|none|

<h2 id="tocS_ProductEdit">ProductEdit</h2>
<!-- backwards compatibility -->
<a id="schemaproductedit"></a>
<a id="schema_ProductEdit"></a>
<a id="tocSproductedit"></a>
<a id="tocsproductedit"></a>

```json
{
  "name": "string",
  "category_id": 0,
  "image_url": "string",
  "price": 0,
  "expiration_date": "2019-08-24"
}

```

ProductEdit

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|category_id|integer|true|none|none|
|image_url|string|true|none|none|
|price|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|expiration_date|string(date)|true|none|none|

<h2 id="tocS_ProductListResponse">ProductListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaproductlistresponse"></a>
<a id="schema_ProductListResponse"></a>
<a id="tocSproductlistresponse"></a>
<a id="tocsproductlistresponse"></a>

```json
{
  "total_available": 0,
  "total_return": 0,
  "items": [
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

ProductListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total_available|integer|true|none|none|
|total_return|integer|true|none|none|
|items|[[ProductResponse](#schemaproductresponse)]|true|none|none|

<h2 id="tocS_ProductResponse">ProductResponse</h2>
<!-- backwards compatibility -->
<a id="schemaproductresponse"></a>
<a id="schema_ProductResponse"></a>
<a id="tocSproductresponse"></a>
<a id="tocsproductresponse"></a>

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

ProductResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|none|
|name|string|true|none|none|
|category_id|integer|true|none|none|
|category_name|string|true|none|none|
|image_url|string|true|none|none|
|price|string|true|none|none|
|expiration_date|string(date)|true|none|none|
|purchased_date|string(date)|true|none|none|

<h2 id="tocS_SpendingByCategory">SpendingByCategory</h2>
<!-- backwards compatibility -->
<a id="schemaspendingbycategory"></a>
<a id="schema_SpendingByCategory"></a>
<a id="tocSspendingbycategory"></a>
<a id="tocsspendingbycategory"></a>

```json
{
  "category_id": 0,
  "category_name": "string",
  "total_spent": "string"
}

```

SpendingByCategory

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|category_id|integer|true|none|none|
|category_name|string|true|none|none|
|total_spent|string|true|none|none|

<h2 id="tocS_TotalSpending">TotalSpending</h2>
<!-- backwards compatibility -->
<a id="schematotalspending"></a>
<a id="schema_TotalSpending"></a>
<a id="tocStotalspending"></a>
<a id="tocstotalspending"></a>

```json
{
  "total_spent": "string"
}

```

TotalSpending

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total_spent|string|true|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

