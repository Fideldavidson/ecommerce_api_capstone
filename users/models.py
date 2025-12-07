from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # The existing fields (username, email, password) are handled by AbstractUser.
    # We can add custom fields here if needed, but the required ones are included.
    
    # Adding related name for clarity, though AbstractUser handles relationships well.
    products_created = models.ManyToManyField(
        'products.Product', 
        related_name='creators', 
        blank=True
    )
    
    def __str__(self):
        return self.username
