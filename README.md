# 🛒 E-commerce Product API Capstone Project

## Project Title: E-commerce Product API

This repository contains the backend implementation for an E-commerce Product Management system, built using Django and Django REST Framework (DRF). The API provides robust CRUD operations for product inventory and secure user authentication for store administrators.

---

## 🚀 Week 1: Setup & Foundation

The goal of Week 1 was to establish the project structure, define core database models, and configure the necessary dependencies.

### Key Deliverables:

* **Project Structure:** Initialized Django project (`config`), and two core applications (`users` and `products`).
* **Dependencies:** `Django`, `djangorestframework`, and `psycopg2-binary` (for future PostgreSQL connection) installed.
* **Configuration:** `settings.py` updated to register apps, set up DRF defaults (including `TokenAuthentication` and `Pagination`), and define the custom `AUTH_USER_MODEL = 'users.User'`.
* **Database Models:** Initial models for `User` (custom `AbstractUser`) and `Product` defined with necessary fields and the **One-to-Many** relationship established.
* **Version Control:** Initialized Git repository and pushed the first commit to GitHub.

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:Fideldavidson/ecommerce_api_capstone.git
    cd ecommerce_api_capstone
    ```
2.  **Activate Virtual Environment:**
    ```bash
    source venv/bin/activate
    ```
3.  **Install Dependencies:** (If not done in Week 1)
    ```bash
    pip install -r requirements.txt # (Assuming you create this file later)
    # OR: pip install django djangorestframework
    ```
4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

### Next Steps (Week 2 Focus)

Implement authentication serializers, views, and URL patterns for user registration and login endpoints.

---

## 🔒 Week 2: User Implementation & Authentication

The primary goal of Week 2 was to implement secure token-based user authentication and management endpoints.

### Key Deliverables:

* **Custom User Model Ready:** Confirmed `AUTH_USER_MODEL = 'users.User'` setup in `settings.py`.
* **Authentication Setup:** Integrated `rest_framework.authtoken` and configured `TokenAuthentication` as the default method.
* **User Serializers:** Created `UserRegistrationSerializer`, `UserLoginSerializer`, and `UserSerializer` for data validation and profile representation.
* **Authentication Endpoints:** Implemented the following core API views:
    * **POST `/api/users/register/`**: Creates a new user and hashes the password.
    * **POST `/api/users/login/`**: Authenticates credentials and issues a unique `Token`.
    * **GET/PUT/DELETE `/api/users/me/`**: Allows authenticated users to view, update, or delete their own profile.
* **URL Routing:** Defined and included all user authentication endpoints under the `/api/users/` path.
* **Fixes:** Resolved the `ModuleNotFoundError: No module named 'products.urls'` by creating a placeholder file and the middleware typo in `settings.py`.

---

## 📦 Week 3: Product Core (CRUD & Search)

The focus of Week 3 was building the core E-commerce functionality for managing the product inventory.

### Key Deliverables:

* **Product Serializer:** Created `ProductSerializer` to handle CRUD operations and validate product attributes (Name, Price, Stock Quantity, etc.). Includes a read-only field for the `created_by_username`.
* **Product CRUD Views:** Implemented **Generic Views** for product management:
    * **GET/POST `/api/products/products/`**: List all products (GET) or create a new product (POST).
    * **GET/PUT/DELETE `/api/products/products/<id>/`**: Retrieve, update, or delete a single product.
* **Authorization Logic:** Implemented a custom permission class, **`IsStaffOrReadOnly`**, to enforce the following rule:
    * **Read (GET)** operations are **publicly accessible**.
    * **Write (POST, PUT, DELETE)** operations are restricted to authenticated users with `is_staff = True`.
* **Basic Search Functionality:** Implemented a `ProductSearchView` mapped to **`api/products/products/search/`** allowing search by `name__icontains` or `category__iexact`.
* **Model Integrity:** Ensured the `created_by` Foreign Key is automatically set to the authenticated user during product creation using `perform_create`.

### Next Steps (Week 4 Focus)

Enhance product listing and search endpoints with pagination, advanced filtering options (`price range`, `stock availability`), and implement full error handling.


### 📈 Week 4: Optimization & Enhancement

The focus of Week 4 was optimizing data retrieval for scalability and user experience by implementing advanced filtering and confirming pagination.

| Deliverable | Description | Endpoint |
| :--- | :--- | :--- |
| **Advanced Filtering** | Implemented a **`ProductFilterMixin`** to allow querying products by three new parameters: **Price Range** (`min_price`/ `max_price`), and **Stock Availability** (`in_stock`/`out_of_stock`). | `GET /api/products/products/` |
| **Pagination Confirmation** | Confirmed that DRF's **PageNumberPagination** (set to 10 items per page) is active on all product listing and search endpoints, ensuring high performance for large datasets. | `GET /api/products/products/` |
| **Search Enhancement** | Integrated filtering logic into the list view to allow complex querying (e.g., filtering by stock AND price range). | `GET /api/products/products/search/` |
| **URL Fix** | Updated `config/urls.py` with a `RedirectView` to send root path visitors (`/`) directly to the main API endpoint, resolving the initial 404 error. | `GET /` |

---

## 🛑 Project Status & Next Steps (Week 5 Focus)

All core functional and technical requirements (User Auth, Product CRUD, Search, Filtering, Pagination) are now **functionally complete**.

The remaining phase, **Week 5**, is dedicated to non-functional requirements vital for production quality: **Testing**, **Error Handling**, and **Documentation**.

