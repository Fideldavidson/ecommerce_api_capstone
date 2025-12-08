from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # This field ensures the username of the creator is returned, not just the user ID
    created_by_username = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'category', 
            'stock_quantity', 'image_url', 'created_at', 'updated_at',
            'created_by_username' # Read-only field
        )
        read_only_fields = ('created_at', 'updated_at', 'created_by_username')
