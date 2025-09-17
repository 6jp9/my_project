from django.db import models
from user import models as em
from home import models as hm

# Create your models here.

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(em.Customers, on_delete=models.CASCADE, related_name='carts', blank=True, null=True)
    product = models.ForeignKey(hm.Products, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

