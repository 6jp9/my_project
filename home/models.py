from django.db import models
from user import models as um

# Create your models here.

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(um.Merchants, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'
