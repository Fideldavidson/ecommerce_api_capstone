from django.urls import path
from .views import (
    ProductListCreateView,
    ProductDetailView,
    ProductSearchView
)

urlpatterns = [
    # CRUD/List Endpoints
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    
    # Search Endpoint (Week 4 Plan, implemented early)
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
]
