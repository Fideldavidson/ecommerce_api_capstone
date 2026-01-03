# 🛒 E-Commerce API Capstone
**Final Submission - Week 5**

A robust, production-ready RESTful API built with Django REST Framework (DRF) for a modern e-commerce platform. This project represents the culmination of 5 weeks of development, focusing on security, scalability, and standardized documentation.

---

## 🚀 Key Features

* **Custom User Architecture**: Implemented a Custom User model to handle role-based access control (Customers vs. Merchants).
* **Secure Authentication**: JWT-based authentication using `djangorestframework-simplejwt`.
* **Product & Inventory**: Full CRUD operations with category filtering and merchant-only permissions.
* **Shopping Cart & Atomic Orders**: A robust ordering system that ensures database integrity during the checkout process.
* **Global Error Handling**: Standardized JSON error responses for a consistent API consumer experience.
* **Live Documentation**: Interactive API testing environment via Swagger and ReDoc.

---

## 🛠️ Tech Stack

* **Framework**: Django 4.2+ & Django REST Framework
* **Authentication**: SimpleJWT (JSON Web Tokens)
* **Documentation**: drf-spectacular (OpenAPI 3.0)
* **Database**: SQLite (Dev) / PostgreSQL (Ready)
* **Testing**: Django TestCase

---

## 📖 API Documentation

Once the server is running, you can explore the endpoints here:

* **Swagger UI**: [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
* **ReDoc**: [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)



---

## 🔧 Installation & Setup

1.  **Clone & Enter**:
    ```bash
    git clone https://github.com/Fideldavidson/ecommerce_api_capstone.git
    cd ecommerce_api_capstone
    ```

2.  **Environment Setup**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Database Initialisation**:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

4.  **Run Server**:
    ```bash
    python manage.py runserver
    ```

---

## 🧪 Testing
The project includes automated tests for Authentication, Product Management, and Ordering logic.
```bash
python manage.py test
```

---

## �� Project Structure
* `users/`: Custom user models and authentication logic.
* `products/`: Product management and category filtering.
* `orders/`: Shopping cart and order processing logic.
* `config/`: Global settings, custom exception handlers, and URL routing.

