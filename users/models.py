from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    products_created = models.ManyToManyField(
        "products.Product", related_name="creators", blank=True
    )

    def __str__(self):
        return self.username
