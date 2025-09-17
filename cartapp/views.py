from django.shortcuts import render, redirect, get_object_or_404
from home.models import Products
from .models import Cart
from user.models import Customers
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
import requests

# Create your views here.

def cart(request):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customers, username=request.user.username)
        cart_items = Cart.objects.filter(customer_id = customer.customer_id).select_related('product')
        return render(request,'cartapp/cart.html',{'cart_items': cart_items})
    return render(request,'cartapp/cart.html')


def add_to_cart(request, product_id):
    if request.method == "POST":
        customer = get_object_or_404(Customers, username=request.user.username)
        product = get_object_or_404(Products, product_id=product_id)
        # Use request.user.username to match the CharField in Customers
        Cart.objects.create(
            customer=customer,
            product=product,
            created_at = now()
        )
    return redirect("cart")


def delete_from_cart(request, cart_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, cart_id=cart_id, customer__username=request.user.username)
        cart_item.delete()
    return redirect("cart")

