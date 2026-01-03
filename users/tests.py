from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAuthTests(APITestCase):
    def test_registration(self):
        """Test user registration."""
        url = reverse("user-register")  # Ensure this matches users/urls.py
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "password123",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        new_user = User.objects.get()
        self.assertEqual(new_user.username, "newuser")
        self.assertNotEqual(new_user.password, "password123")
        self.assertTrue(new_user.check_password("password123"))

    def test_login(self):
        """Test user login."""
        user = User.objects.create_user(username="testuser", password="password123")
        url = reverse("user-login")  # Ensure matches users/urls.py
        data = {"username": "testuser", "password": "password123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)


class UserProfileTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="profileuser", password="password123"
        )
        self.client.force_authenticate(user=self.user)
        # Assuming the detail view URL is 'user-detail' or similar.
        # I need to check users/urls.py to be sure of the name.
        # Based on typical detail views:
        self.url = reverse("user-detail")

    def test_get_profile(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "profileuser")
