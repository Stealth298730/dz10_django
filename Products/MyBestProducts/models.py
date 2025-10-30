from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50,null=True,default=None)
    description = models.CharField(max_length=150,null=True,default=None)
    price = models.IntegerField(null=True,default=None)

    def __str__(self):
        return f"{self.name}:{self.price}"


class MainList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Main: {self.product.name}"

class TopList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Top: {self.product.name}"