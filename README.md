# Make Life Easier API

This is a FastAPI project that manages products (such as supplements and cosmetics) with expiry dates.

## 📦 Features

- Full CRUD API for products
- SQLite database support
- Pagination, sorting, and filtering
- Soft delete with `enabled` field
- API documentation with Swagger UI

- [Products API doc](https://github.com/CoaCao/make-life-easier-api/blob/main/docs/products.md)
- [Categories API doc](https://github.com/CoaCao/make-life-easier-api/blob/main/docs/categories.md)
- [Feature API doc](https://github.com/CoaCao/make-life-easier-api/blob/main/docs/feature.md)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/make-life-easier-api.git
cd make-life-easier-api
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate.bat  # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
uvicorn src.main:app --reload
```

Visit http://127.0.0.1:8000/docs, http://127.0.0.1:8000/redoc for the interactive API documentation.

## 🐳 Run with Docker

### 1. Build Docker Image

```bash
docker build -t make-life-easier-api .
```

### 2. Run the Container

```bash
docker run -p 8000:8000 make-life-easier-api
```

Then visit: http://localhost:8000/docs, http://localhost:8000/redoc

## 🗃️ Initialize Sample Data

```bash
python src/core/init_data.py
```

This will create the SQLite DB and insert sample product records.

Application id: c86967de-617e-46ba-bf00-ad8fd1771d25
Object id: f75403f2-bebe-42e2-9154-b8f9ccfe04c1
Tenant id: 5486b9d7-3cba-42c0-8d35-e750477d9a37
Value:  dU98Q~~GKnnCdFAcUQ4x7pWh2yUxF77OG0

Secret Google
-------------------
tp7uluUbAXPZI-1fNlypOPK7fNxD

client_id
---------------
2596818084-8bdl7h5i4b1945b4uji3b6daas6u714d
