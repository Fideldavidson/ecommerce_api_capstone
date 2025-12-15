from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView # <-- Import RedirectView

urlpatterns = [
    # Root URL Redirection
    # Redirects the base URL (/) directly to the product list endpoint
    path('', RedirectView.as_view(url='api/products/products/', permanent=False), name='api-root-redirect'),

    path('admin/', admin.site.urls),
    # Include the user authentication endpoints
    path('api/users/', include('users.urls')),
    
    # Include Product API endpoints
    path('api/products/', include('products.urls')),
]
