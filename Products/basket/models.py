from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from MyBestProducts.models import Product

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} ({self.count})"