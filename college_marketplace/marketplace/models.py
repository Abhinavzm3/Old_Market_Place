from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

default_user_id = 1
class Product(models.Model):
    
    CATEGORY_CHOICES = [
        ('books', 'Books and Copy'),
        ('accessories', 'Accessories'),
        ('electronics', 'Electronics'),
        ('essentials', 'Daily Essentials'),
        ('stationery', 'Stationery'),
        ('sports', 'Sports'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=default_user_id)

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    whatsapp_number = models.BigIntegerField()
    image = models.ImageField(upload_to='static/products/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    


    def __str__(self):
        return self.name
