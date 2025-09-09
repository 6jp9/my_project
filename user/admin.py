from django.contrib import admin
from .models import Customers
# Register your models here.
class Customer_admin(admin.ModelAdmin):
    list_display = ['customer_id','username','first_name','last_name','email','phone','address','created_at']
admin.site.register(Customers,Customer_admin)