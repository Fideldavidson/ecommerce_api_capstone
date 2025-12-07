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

