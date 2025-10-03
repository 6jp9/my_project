from django.contrib import admin
from .models import Payments
# Register your models here.

class Payments_Admin(admin.ModelAdmin):
    list_display = ['payment_id','order','merchant','total_amount','stripe_cut','platform_cut','merchant_amount','created_at']
admin.site.register(Payments,Payments_Admin)
