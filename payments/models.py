from django.db import models
from home.models import Orders
from user.models import Merchants

# Create your models here.
class Payments(models.Model):
    payment_id = models.CharField(max_length=100, primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='payments', blank=True, null=True)
    merchant = models.ForeignKey(Merchants, on_delete=models.CASCADE, related_name='merchant_payment', blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stripe_cut = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    platform_cut = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    merchant_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
