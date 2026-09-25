# FlowAccount Technical Test - Backend

A simple Product Management RESTful API for SME stores, built with **Python (FastAPI)**. This project implements **Clean Architecture** principles to separate concerns, ensuring the code is maintainable, scalable, and easy to test.

## 🏗️ Architecture

The project is structured based on Clean Architecture concepts (Delivery -> Use Cases -> Data Access).

```text
project_root/
├── main.py                  # Application entry point and exception handlers
├── schemas/                 # Data Transfer Objects (DTOs) and Pydantic validation rules
├── repositories/            # Data access layer (In-memory storage for this test)
├── services/                # Core business logic and rules
└── routers/                 # API Endpoints (Controllers)
```

## 🚀 Features Implemented

### Part 1: Core Features
- [x] **Challenge 1:** Create new product with robust Pydantic validation.
- [x] **Challenge 2:** Retrieve all products with an optional category filter.
- [x] **Challenge 3:** Sell product (Stock deduction with business rule validations).

### Part 2: Bonus Features
- [x] **Challenge 4:** Search products by name or SKU (Case-insensitive).
- [x] **Challenge 5:** Bulk update product prices.

## 🛠️ Tech Stack
- **Framework:** FastAPI (Python)
- **Validation:** Pydantic
- **Database:** In-Memory Storage (List/Dictionary)
- **Server:** Uvicorn

## ⚙️ Prerequisites
- Python 3.9 or higher

## 🏃‍♂️ How to Run the Project

1. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn pydantic
   ```

2. **Start the development server:**
   ```bash
   python -m uvicorn main:app --reload
   ```

3. **Access the API Documentation:**
   Open your browser and navigate to the auto-generated Swagger UI to test the endpoints:
   👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📡 API Endpoints Summary

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/products` | Create a new product. |
| `GET` | `/api/products` | Get all products (supports `?category=` filter). |
| `POST` | `/api/products/sell` | Sell a product and deduct stock. |
| `GET` | `/api/products/search` | Search products by keyword (supports `?keyword=`). |
| `PUT` | `/api/products/bulk-price-update` | Update prices for multiple products at once. |

## 💡 Note for Reviewer

- The system handles default FastAPI validation errors (HTTP 422) and transforms them into **HTTP 400 Bad Request** with a custom Thai error array format exactly as required by the specification.
- **In-memory data storage** is used via the Repository pattern. This makes it trivial to swap out with a real database (e.g., PostgreSQL + SQLAlchemy) in the future without modifying the business logic (Service layer).