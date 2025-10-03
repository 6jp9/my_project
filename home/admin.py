from django.contrib import admin
from . import models
# Register your models here.
class Products_Admin(admin.ModelAdmin):
    list_display = ['product_id','name','price', 'stock', 'merchant_id','image', 'created_at']
admin.site.register(models.Products,Products_Admin)

class Orders_Admin(admin.ModelAdmin):
    list_display = ['order_id','customer_id','merchant_id','product_id','quantity','price','status','created_at']
admin.site.register(models.Orders,Orders_Admin)
