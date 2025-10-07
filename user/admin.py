from django.contrib import admin
from .models import Customers,Merchants
# Register your models here.
class Customer_admin(admin.ModelAdmin):
    list_display = ['user','customer_id','username','first_name','last_name','email','phone','address','created_at']
admin.site.register(Customers,Customer_admin)

class Merchant_admin(admin.ModelAdmin):
    list_display = ['merchant_id','user','username','business_name','email','phone','address','created_at','total_revenue']
admin.site.register(Merchants,Merchant_admin)
