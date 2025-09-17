# Register your models here.
from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'customer', 'product', 'created_at')

admin.site.register(Cart, CartAdmin)