from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the user authentication endpoints
    path('api/users/', include('users.urls')),
    
    # Placeholder for Product API endpoints (Week 3)
    path('api/', include('products.urls')),
]
