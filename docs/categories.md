<h1 id="make-life-easier-api">Make Life Easier API v1.0</h1>

<h1 id="make-life-easier-api-categories">Categories</h1>

## Get all categories

<a id="opIdget_all_categories__get"></a>

`GET /categories/`

<h3 id="get_all_categories__get-parameters">Parameters</h3>

| Name | In    | Type | Required | Description |
|------|-------|------|----------|-------------|
| name | query | any  | false    | none        |

<h3 id="get_all_categories__get-responses">Responses</h3>

| Status | Meaning                                                 | Description         | Schema                                              |
|--------|---------------------------------------------------------|---------------------|-----------------------------------------------------|
| 200    | OK | Successful Response | [CategoryListResponse](#schemacategorylistresponse) |
| 422    | Unprocessable Entity                                    | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror)   |

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

> Example responses

```json
{
  "total": 5,
  "items": [
    {
      "id": 1,
      "name": "Food",
      "created_date": "2025-06-11"
    },
    {
      "id": 2,
      "name": "Drink",
      "created_date": "2025-06-11"
    },
    {
      "id": 3,
      "name": "Drug",
      "created_date": "2025-06-11"
    },
    {
      "id": 4,
      "name": "Cosmetic",
      "created_date": "2025-06-11"
    },
    {
      "id": 5,
      "name": "Supplement",
      "created_date": "2025-06-11"
    }
  ]
}
```

## Add category

<a id="opIdadd_category_categories__post"></a>

`POST /categories/`

*Add Category*

> Body parameter

```json
{
  "name": "string"
}
```

<h3 id="add_category_categories__post-parameters">Parameters</h3>

| Name | In   | Type                              | Required | Description |
|------|------|-----------------------------------|----------|-------------|
| body | body | [CategoryAdd](#schemacategoryadd) | true     | none        |

<h3 id="add_category_categories__post-responses">Responses</h3>

| Status | Meaning                                                 | Description         | Schema                                            |
|--------|---------------------------------------------------------|---------------------|---------------------------------------------------|
| 200    | OK | Successful Response | [CategoryResponse](#schemacategoryresponse)       |
| 422    | Unprocessable Entity                                    | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "created_date": "2019-08-24"
}
```

> Example responses

```json
{
  "id": 2,
  "name": "Supplement",
  "created_date": "2025-06-15"
}
```

## Get category by category_id

<a id="opIdget_category_categories__category_id__get"></a>

`GET /categories/{category_id}`


<h3 id="get_category_categories__category_id__get-parameters">Parameters</h3>

| Name        | In   | Type    | Required | Description |
|-------------|------|---------|----------|-------------|
| category_id | path | integer | true     | none        |

<h3 id="get_category_categories__category_id__get-responses">Responses</h3>

| Status | Meaning                                                 | Description         | Schema                                            |
|--------|---------------------------------------------------------|---------------------|---------------------------------------------------|
| 200    | OK | Successful Response | [CategoryResponse](#schemacategoryresponse)       |
| 422    | Unprocessable Entity                                    | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |


> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "created_date": "2019-08-24"
}
```

> Example responses
```json
{
  "id": 1,
  "name": "Supplement",
  "created_date": "2019-08-24"
}
```


## Edit category

<a id="opIdedit_category_categories__category_id__put"></a>

`PUT /categories/{category_id}`


> Body parameter

```json
{
  "name": "string"
}
```

<h3 id="edit_category_categories__category_id__put-parameters">Parameters</h3>

| Name        | In   | Type                                | Required | Description |
|-------------|------|-------------------------------------|----------|-------------|
| category_id | path | integer                             | true     | none        |
| body        | body | [CategoryEdit](#schemacategoryedit) | true     | none        |

<h3 id="edit_category_categories__category_id__put-responses">Responses</h3>

| Status | Meaning                                                 | Description         | Schema                                            |
|--------|---------------------------------------------------------|---------------------|---------------------------------------------------|
| 200    | OK | Successful Response | [CategoryResponse](#schemacategoryresponse)       |
| 422    | Unprocessable Entity                                    | Validation Error    | [HTTPValidationError](#schemahttpvalidationerror) |

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "created_date": "2019-08-24"
}
```

> Example responses
```json
{
  "name": "string"
}
```

## Delete category

<a id="opIdremove_category_categories__category_id__delete"></a>

`DELETE /categories/{category_id}`

<h3 id="remove_category_categories__category_id__delete-parameters">Parameters</h3>

| Name        | In   | Type    | Required | Description |
|-------------|------|---------|----------|-------------|
| category_id | path | integer | true     | none        |



<h3 id="remove_category_categories__category_id__delete-responses">Responses</h3>

| Status | Meaning                                                 | Description         | Schema                                            |
|--------|---------------------------------------------------------|---------------------|---------------------------------------------------|
| 200    | OK | Successful Response | Inline                                            |

> 200 Response

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

| Name | Type   | Required | Restrictions | Description |
|------|--------|----------|--------------|-------------|
| name | string | true     | none         | none        |

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

| Name | Type   | Required | Restrictions | Description |
|------|--------|----------|--------------|-------------|
| name | string | true     | none         | none        |

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

| Name  | Type                                          | Required | Restrictions | Description |
|-------|-----------------------------------------------|----------|--------------|-------------|
| total | integer                                       | true     | none         | none        |
| items | [[CategoryResponse](#schemacategoryresponse)] | true     | none         | none        |

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

| Name         | Type         | Required | Restrictions | Description |
|--------------|--------------|----------|--------------|-------------|
| id           | integer      | true     | none         | none        |
| name         | string       | true     | none         | none        |
| created_date | string(date) | true     | none         | none        |

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