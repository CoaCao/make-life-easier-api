<!-- Generator: Widdershins v4.0.1 -->

<h1 id="make-life-easier-api">Make Life Easier API v1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Make Life Easier API

<h1 id="make-life-easier-api-products">Products</h1>

## get_products

<a id="opIdget_products_products__get"></a>

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

> Example responses

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



`POST /products/`

*Add Product*

> Body parameter

```json
{
  "name": "string",
  "image_url": "string",
  "expiry_date": "2019-08-24"
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
  "image_url": "string",
  "expiry_date": "2019-08-24",
  "added_date": "2019-08-24"
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
  "image_url": "string",
  "expiry_date": "2019-08-24",
  "added_date": "2019-08-24"
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



`PUT /products/{product_id}`

*Edit Product*

> Body parameter

```json
{
  "name": "string",
  "image_url": "string",
  "expiry_date": "2019-08-24"
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
  "image_url": "string",
  "expiry_date": "2019-08-24",
  "added_date": "2019-08-24"
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

# Schemas

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
  "image_url": "string",
  "expiry_date": "2019-08-24"
}

```

ProductAdd

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|image_url|string|true|none|none|
|expiry_date|string(date)|true|none|none|

<h2 id="tocS_ProductEdit">ProductEdit</h2>
<!-- backwards compatibility -->
<a id="schemaproductedit"></a>
<a id="schema_ProductEdit"></a>
<a id="tocSproductedit"></a>
<a id="tocsproductedit"></a>

```json
{
  "name": "string",
  "image_url": "string",
  "expiry_date": "2019-08-24"
}

```

ProductEdit

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|image_url|string|true|none|none|
|expiry_date|string(date)|true|none|none|

<h2 id="tocS_ProductListResponse">ProductListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaproductlistresponse"></a>
<a id="schema_ProductListResponse"></a>
<a id="tocSproductlistresponse"></a>
<a id="tocsproductlistresponse"></a>

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

ProductListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total|integer|true|none|none|
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
  "image_url": "string",
  "expiry_date": "2019-08-24",
  "added_date": "2019-08-24"
}

```

ProductResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|none|
|name|string|true|none|none|
|image_url|string|true|none|none|
|expiry_date|string(date)|true|none|none|
|added_date|string(date)|true|none|none|

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
