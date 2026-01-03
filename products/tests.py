from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()


class ProductAPITests(APITestCase):
    def setUp(self):
        # 1. Create a staff user for authorized actions
        self.staff_user = User.objects.create_user(
            username="admin", password="password123", is_staff=True
        )
        # 2. Create a regular user for unauthorized checks
        self.regular_user = User.objects.create_user(
            username="guest", password="password123", is_staff=False
        )

        # 3. Create a sample product for testing
        self.product = Product.objects.create(
            name="UniqueTestMouse",
            price=50.00,
            category="Electronics",
            stock_quantity=10,
            created_by=self.staff_user,
        )

    def test_search_product_by_name(self):
        """Test if the search endpoint returns the correct product."""
        url = reverse("product-search") + "?name=UniqueTestMouse"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if "results" in response.data:
            # Handle pagination
            self.assertEqual(len(response.data["results"]), 1)
            self.assertEqual(response.data["results"][0]["name"], "UniqueTestMouse")
        else:
            # Handle no pagination
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]["name"], "UniqueTestMouse")

    def test_unauthorized_delete_fails(self):
        """Ensure a regular user CANNOT delete a product."""
        self.client.force_authenticate(user=self.regular_user)
        url = reverse("product-detail", kwargs={"id": self.product.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Verify custom error handling structure
        self.assertIn("status_code", response.data)
        self.assertEqual(response.data["status_code"], 403)
        self.assertIn("message", response.data)

        self.assertIn("message", response.data)

    def test_filter_min_price(self):
        """Test filtering products by minimum price."""
        # Create an expensive product
        Product.objects.create(
            name="Expensive Laptop",
            price=1500.00,
            category="Electronics",
            stock_quantity=5,
            created_by=self.staff_user
        )
        # Create a cheap product
        Product.objects.create(
            name="Cheap Cable",
            price=10.00,
            category="Electronics",
            stock_quantity=50,
            created_by=self.staff_user
        )
        
        # Test min_price=100 (should include Laptop, exclude Cable)
        # We need to use 'product-list-create' for filtering if search is usually there, 
        # BUT 'ProductListCreateView' uses 'ProductFilterMixin' which has the filter logic.
        url = reverse("product-list-create") + "?min_price=100"
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # We expect 2 products >= 100? No, UniqueTestMouse is 50. Cheap Cable is 10. Expensive Laptop is 1500.
        # Only Expensive Laptop matches.
        
        if "results" in response.data:
             self.assertEqual(len(response.data["results"]), 1)
             self.assertEqual(response.data["results"][0]["name"], "Expensive Laptop")
        else:
             self.assertEqual(len(response.data), 1)
             self.assertEqual(response.data[0]["name"], "Expensive Laptop")

    def test_create_product(self):
        """Ensure a staff user can create a product."""
        self.client.force_authenticate(user=self.staff_user)
        url = reverse("product-list-create")
        data = {
            "name": "New Product",
            "price": 100.00,
            "category": "Electronics",
            "stock_quantity": 5,
            "description": "A brand new product.",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)  # 1 existing + 1 new
        self.assertTrue(Product.objects.filter(name="New Product").exists())

    def test_update_product(self):
        """Ensure a staff user can update a product."""
        self.client.force_authenticate(user=self.staff_user)
        url = reverse("product-detail", kwargs={"id": self.product.id})
        data = {"price": 75.00}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, 75.00)

    def test_delete_product(self):
        """Ensure a staff user can delete a product."""
        self.client.force_authenticate(user=self.staff_user)
        url = reverse("product-detail", kwargs={"id": self.product.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
