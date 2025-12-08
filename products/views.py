from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffOrReadOnly

class ProductListCreateView(generics.ListCreateAPIView):
    """
    GET /api/products/  -> List all products (public)
    POST /api/products/ -> Create a new product (staff/admin only)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Custom permission: Staff users can write (POST), anyone can read (GET)
    permission_classes = [IsStaffOrReadOnly] 
    
    # Override perform_create to automatically set the creator
    def perform_create(self, serializer):
        # The 'created_by' field is set to the currently authenticated user
        serializer.save(created_by=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/products/<id>/    -> Retrieve single product (public)
    PUT/PATCH /api/products/<id>/ -> Update product (staff/admin only)
    DELETE /api/products/<id>/  -> Delete product (staff/admin only)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]
    lookup_field = 'id' # Use 'id' for clean URLs


class ProductSearchView(generics.ListAPIView):
    """
    GET /api/products/search/?name=...&category=...
    Endpoint for searching products by name or category.
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny] # Publicly accessible

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)
        
        # Search by partial match (icontains)
        if name:
            queryset = queryset.filter(name__icontains=name)
        
        # Search by exact category match
        if category:
            queryset = queryset.filter(category__iexact=category)
            
        return queryset.distinct()
