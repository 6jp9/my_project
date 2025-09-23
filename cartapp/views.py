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
        quantity = int(request.POST.get("quantity", 1))
        cart_item, created = Cart.objects.get_or_create(
            customer=customer,
            product=product,
            defaults={"quantity": quantity, "price": product.price * quantity, "status": "active"}
        )

        if not created:
            cart_item.quantity += quantity
            if cart_item.quantity>product.stock:
                cart_item.quantity=product.stock
            cart_item.update_price()
            cart_item.save()
    return redirect("product",product_id=product_id)


def delete_from_cart(request, cart_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, cart_id=cart_id, customer__username=request.user.username)
        cart_item.delete()
    return redirect("cart")



def increment_item(request, cart_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, cart_id=cart_id)
        product = cart_item.product
        stock = product.stock

        if cart_item.quantity < stock:
            cart_item.quantity += 1
        else:
            cart_item.quantity = stock
        cart_item.update_price()
        cart_item.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
        # return redirect('cart')
    return redirect('login')


def decrement_item(request, cart_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, cart_id=cart_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.update_price()
            cart_item.save()
        else:
            cart_item.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
        # return redirect('cart')
    return redirect('login')