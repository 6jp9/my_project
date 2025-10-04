from django.db import models
from user.models import Merchants,Customers

# Create your models here.


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(Merchants, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    merchant = models.ForeignKey(Merchants, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True,default='Ordered')
    created_at = models.DateTimeField(auto_now_add=True)
