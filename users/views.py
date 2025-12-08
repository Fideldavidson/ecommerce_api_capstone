from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .serializers import (
    UserRegistrationSerializer, 
    UserLoginSerializer, 
    UserSerializer
)

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    """
    API endpoint that allows for user registration.
    POST /api/users/register/
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)


class UserLoginView(APIView):
    """
    API endpoint that allows users to log in and receive an authentication token.
    POST /api/users/login/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Get or create the auth token for the user
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email
        }, status=status.HTTP_200_OK)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows authenticated users to retrieve, update, or delete 
    their own profile information.
    GET, PUT, PATCH, DELETE /api/users/me/
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        # Ensure the user can only manage their own profile
        return self.request.user

    def delete(self, request, *args, **kwargs):
        # We need to manually delete the user instance
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
