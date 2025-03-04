# E-commerce API with FastAPI and MongoDB

This project is a modular e-commerce API built using FastAPI and MongoDB. The application includes features for user registration, authentication, product management, and order management. The project follows a clean and modular architecture, making it easy to maintain and scale.

## 🚀 Features

- User Registration & Authentication
- Product Listing, Creation, and Management
- Order Creation & Status Management
- JWT Authentication
- MongoDB Integration with Motor

---

# 📁 Project Structure

```
ecommerce-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── order.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── order.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── order.py
│   └── utils/
│       ├── __init__.py
│       ├── auth.py
│       └── db_helpers.py
├── requirements.txt
└── README.md
```

---

## 📂 Directory Breakdown

### 1. **app/**

The core application directory that contains all the code for the FastAPI application.

#### 2. **main.py**

- The entry point for the FastAPI application.
- Initializes the app and includes the routers for different modules.

#### 3. **config.py**

- Contains application configurations, such as database connection strings, JWT secrets, and other global settings.

#### 4. **database.py**

- Manages the connection to the MongoDB database using Motor.
- Exposes collections (`user_collection`, `product_collection`, `order_collection`) for easy access in the application.

---

### 📁 **models/**

Contains Pydantic models representing the data structure of users, products, and orders.

- **user.py:** Defines the `UserModel` with fields for `username`, `email`, and `password`.
- **product.py:** Defines the `ProductModel` with fields for `name`, `description`, `price`, and `stock`.
- **order.py:** Defines the `OrderModel` with fields for `user_id`, `product_ids`, `total_price`, and `status`.

---

### 📁 **schemas/**

Holds Pydantic schemas for request validation and serialization.

- **user.py:** Schemas for `CreateUserSchema` and `LoginSchema`.
- **product.py:** Schemas for `CreateProductSchema`.
- **order.py:** Schemas for `CreateOrderSchema`.

---

### 📁 **routes/**

Defines the API endpoints for users, products, and orders.

- **user.py:** Endpoints for registration (`/register`) and authentication (`/login`).
- **product.py:** Endpoints for product creation, listing, and management.
- **order.py:** Endpoints for creating and managing orders.

---

### 📁 **utils/**

Contains utility functions and helper methods.

- **auth.py:** Provides methods for JWT token generation and authentication.
- **db_helpers.py:** Helper functions for MongoDB document serialization and conversion.

---

### **requirements.txt**

- Lists all Python dependencies for the project. Install them with:

```bash
pip install -r requirements.txt
```

---

# 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ecommerce-fastapi
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

### 5. Access the API

- The API will be accessible at: `http://127.0.0.1:8000`
- Swagger documentation: `http://127.0.0.1:8000/docs`

---

# 📋 Example API Endpoints

### 1. **Register a User**

```bash
POST http://127.0.0.1:8000/users/register
```

Request Body:

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "mypassword"
}
```

### 2. **Login a User**

```bash
POST http://127.0.0.1:8000/users/login
```

Request Body:

```json
{
  "username": "john",
  "password": "mypassword"
}
```

### 3. **Create a Product**

```bash
POST http://127.0.0.1:8000/products
```

Request Body:

```json
{
  "name": "Laptop",
  "description": "High-end laptop",
  "price": 1200.5,
  "stock": 10
}
```

---

# 📚 Additional Information

- FastAPI Documentation: [FastAPI](https://fastapi.tiangolo.com)
- MongoDB Documentation: [MongoDB](https://www.mongodb.com)
