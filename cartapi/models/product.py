from django.db import models
from. user import User

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)
    image_url = models.CharField(max_length=1000, default=1)
