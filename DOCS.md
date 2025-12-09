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


# ---

## Week 2: User Implementation & Authentication

### 1. Configuration Changes
* **Authentication Setup:** Added `'rest_framework.authtoken'` to `INSTALLED_APPS` to enable Token-based Authentication.
* **Middleware Fix:** Corrected the typo in `MIDDLEWARE` from `CsrFViewMiddleware` to the correct `CsrfViewMiddleware`.

### 2. User Serializers (`users/serializers.py`)
* **Registration:** `UserRegistrationSerializer` uses `create_user` method to handle password hashing, ensuring security.
* **Login:** `UserLoginSerializer` uses `authenticate()` for credential verification and raises a validation error on failure.
* **Profile:** `UserSerializer` is read/write for `username` and `email`, used for the `/me/` endpoint.

### 3. User Views & Endpoints (`users/views.py`)
* **Registration (`UserRegisterView`):** Uses `generics.CreateAPIView`. Allows any user access (`permissions.AllowAny`).
* **Login (`UserLoginView`):** Uses `APIView`. On successful authentication, it uses `Token.objects.get_or_create()` to issue a persistent token key.
* **Profile (`UserDetailView`):** Uses `generics.RetrieveUpdateDestroyAPIView`. Requires `permissions.IsAuthenticated` and uses `self.request.user` to scope the queryset, ensuring users only access their own data.

# ---

## Week 3: Product Core (CRUD & Search)

### 1. Product Model Enhancement (`products/models.py`)
* The relationship field `created_by` is a `ForeignKey` to `settings.AUTH_USER_MODEL`. This enforces data integrity by ensuring every product has an associated creator.

### 2. Custom Permissions (`products/permissions.py`)
* **Permission Class:** `IsStaffOrReadOnly` was created to enforce business logic:
    * It checks if the `request.method` is in `permissions.SAFE_METHODS` (GET, HEAD, OPTIONS) to allow public read access.
    * Otherwise, it requires the user to be both authenticated and have `is_staff=True` to proceed with write operations (POST, PUT, DELETE).

### 3. Product Serializer (`products/serializers.py`)
* The serializer includes `created_by_username` as a `ReadOnlyField(source='created_by.username')` for clear data representation without exposing the internal Foreign Key ID.

### 4. Product Views & Endpoints (`products/views.py`)
* **List/Create (`ProductListCreateView`):**
    * Uses `generics.ListCreateAPIView` with `IsStaffOrReadOnly` permissions.
    * The `perform_create` method is overridden to automatically set the `created_by` field to `self.request.user`.
* **Detail/CRUD (`ProductDetailView`):** Uses `generics.RetrieveUpdateDestroyAPIView` with `IsStaffOrReadOnly` permissions.
* **Basic Search (`ProductSearchView`):**
    * Uses `generics.ListAPIView` (publicly accessible).
    * The `get_queryset` method handles filtering:
        * Partial matching on name using `name__icontains`.
        * Exact matching on category using `category__iexact`.

