from django.shortcuts import render, redirect, get_object_or_404
from home.models import Products
from .models import Cart
from user.models import Customers
from django.contrib.auth.decorators import login_required
# Create your views here.

def cart(request):
    return render(request,'cartapp/cart.html')

@login_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        product = get_object_or_404(Products, product_id=product_id)
        # Use request.user.username to match the CharField in Customers
        customer = get_object_or_404(Customers, username=request.user.username)
        Cart.objects.create(
            customer=customer,
            product=product,
            quantity=quantity,
            status="pending"
        )
    return redirect("cart")

