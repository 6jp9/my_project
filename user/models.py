from django.db import models

# Create your models here.


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'

class Merchants(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    business_name = models.CharField(max_length=150, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchants'
