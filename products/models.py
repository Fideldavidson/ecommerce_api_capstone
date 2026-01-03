from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL


class Product(models.Model):
    # Product attributes
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock_quantity = models.IntegerField(default=0)
    image_url = models.URLField(max_length=500, blank=True, null=True)

    # Relationship (Foreign Key - One-to-Many)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="products",
        # This is your FK to User.id
    )

    # Tracking fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
