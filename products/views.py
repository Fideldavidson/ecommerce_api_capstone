from rest_framework import generics, permissions, filters
from django.db.models import Q # For complex queries like OR/AND
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffOrReadOnly

class ProductFilterMixin:
    """Mixin to handle advanced filtering logic (Price Range, Stock)"""
    def get_queryset(self):
        queryset = Product.objects.all()
        params = self.request.query_params

        # --- 1. Price Range Filtering ---
        min_price = params.get('min_price')
        max_price = params.get('max_price')

        if min_price:
            try:
                queryset = queryset.filter(price__gte=float(min_price))
            except ValueError:
                # Handled by DRF or front-end validation, but robust
                pass
        
        if max_price:
            try:
                queryset = queryset.filter(price__lte=float(max_price))
            except ValueError:
                pass

        # --- 2. Stock Availability Filtering ---
        stock_status = params.get('stock_status')
        if stock_status:
            if stock_status.lower() == 'in_stock':
                queryset = queryset.filter(stock_quantity__gt=0)
            elif stock_status.lower() == 'out_of_stock':
                queryset = queryset.filter(stock_quantity=0)
        
        return queryset


class ProductListCreateView(ProductFilterMixin, generics.ListCreateAPIView):
    """
    GET /api/products/products/  -> List products with Pagination/Filtering (public)
    POST /api/products/products/ -> Create a new product (staff/admin only)
    """
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly] 
    
    # The queryset is now handled by ProductFilterMixin's get_queryset method

    def perform_create(self, serializer):
        # Automatically set the creator
        serializer.save(created_by=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/products/products/<id>/    -> Retrieve single product (public)
    PUT/PATCH /api/products/products/<id>/ -> Update product (staff/admin only)
    DELETE /api/products/products/<id>/  -> Delete product (staff/admin only)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]
    lookup_field = 'id'


class ProductSearchView(generics.ListAPIView):
    """
    GET /api/products/products/search/?name=...&category=...
    Endpoint for searching products by name or category, now integrated with Pagination.
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)
        
        # If no search params, return nothing (or all? User didn't specify, but search usually requires query)
        # Assuming return all if no query, or handle logic.
        # But for 'search' endpoint, usually if no params, we might return all or none.
        # Given lines 80-92, it was intending to return filtered list.
        
        if not name and not category:
            return queryset # Return all if no params

        search_filter = Q()
        has_filter = False

        if name:
            search_filter |= Q(name__icontains=name)
            has_filter = True
        
        if category:
            search_filter |= Q(category__iexact=category)
            has_filter = True
            
        return queryset.filter(search_filter).distinct()
