from django.urls import path
from .views import (
    UserRegisterView, 
    UserLoginView, 
    UserDetailView
)

urlpatterns = [
    # Registration, Login, and Profile Management Endpoints
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
