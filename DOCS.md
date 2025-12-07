# 📚 Technical Documentation: E-commerce Product API

## Week 1: Project Initialization and Data Modeling

### 1. Technology Stack
* **Core Framework:** Django 4+
* **API:** Django REST Framework (DRF)
* **Language:** Python 3.x
* **Database:** SQLite (Development Default), configured for easy switch to PostgreSQL.
* **Authentication Method (Planned):** Token-Based (using DRF's built-in TokenAuthentication/JWT).

### 2. Database Models (ERD Implementation)

#### **2.1. User Model (`users/models.py`)**
* **Base:** Inherits from `AbstractUser` to leverage Django's existing authentication framework.
* **Key Purpose:** Manages admin/staff accounts responsible for product CRUD operations.
* **Relationships:** Related to `Product` via the Foreign Key on the `Product` model.

#### **2.2. Product Model (`products/models.py`)**
* **Key Purpose:** Stores all e-commerce product inventory data.
* **Attributes:**
    * `name`: `CharField` (Required)
    * `description`: `TextField`
    * `price`: `DecimalField(10, 2)` (Required)
    * `category`: `CharField` (Used for search/filtering)
    * `stock_quantity`: `IntegerField` (Required, Default: 0)
    * `image_url`: `URLField`
* **Relationship (Foreign Key):**
    * `created_by`: `ForeignKey` to `settings.AUTH_USER_MODEL`. This implements the **One-to-Many** relationship: a User creates many Products.

### 3. API Configuration

The core `config/settings.py` file establishes:
* **Custom User Model:** `AUTH_USER_MODEL = 'users.User'`.
* **Default Authentication:** `DEFAULT_AUTHENTICATION_CLASSES` set to include `TokenAuthentication`.
* **Pagination:** `DEFAULT_PAGINATION_CLASS` set to `PageNumberPagination` with a default `PAGE_SIZE: 10`.

