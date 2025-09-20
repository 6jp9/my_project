from django.db import models
from user import models as em
from home import models as hm
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(em.Customers, on_delete=models.CASCADE, related_name='carts', blank=True, null=True)
    product = models.ForeignKey(hm.Products, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0,max_length=10, validators=[MinValueValidator(0)])    
    status = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.product} ({self.quantity})"
    def update_price(self):
        if self.product:
            self.price = self.product.price * self.quantity

