from django.contrib import admin
from . import models
# Register your models here.
class Products_Admin(admin.ModelAdmin):
    list_display = ['product_id','name', 'price', 'stock', 'merchant']
admin.site.register(models.Products,Products_Admin)