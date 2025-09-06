from django.db import models
from user import models as em
from home import models as hm

# Create your models here.

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(em.Customers, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(hm.Products, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'

