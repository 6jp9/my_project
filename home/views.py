from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForms
from user.models import Merchants,Customers
from .models import Products
from cartapp.models import Cart
import requests
# Create your views here.
def home(request):
    Product = Products.objects.all()
    return render(request,'home/home.html',{'product':Product})
def orders(request):
    return render(request,'home/my_orders.html')
def add_product(request,username):
    if request.method=='POST':
        merchant = Merchants.objects.get(username=username)
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.merchant_id = merchant.merchant_id
            product.save()
            return redirect(f'/merchant_profile/{merchant.username}/')
    else:
        form = ProductForms()
    return render(request,'home/addproductform.html',{'form':form})

def product_dtls(request,product_id,cart_id=None):
    product = Products.objects.get(product_id=product_id)
    in_cart=  False
    quantity=0
    if request.user.is_authenticated:
        customer = Customers.objects.get(username = request.user.username)
        in_cart = Cart.objects.filter(customer=customer,product=product)
        if in_cart.exists():
            
            quantity = in_cart.first().quantity
            cart_id = in_cart.first().cart_id

    return render(request,'home/product.html',{'product':product,'in_cart':in_cart,'quantity':quantity,'cart_id':cart_id})

def buy_item(request,cart_id):
    cart = Cart.objects.get(cart_id=cart_id)
    buyer =  Customers.objects.get(customer_id = cart.customer.customer_id)
    item = Products.objects.get(product_id = cart.product.product_id)
    if buyer.address==None or buyer.phone==None:
        return redirect('customer_dtls',username=buyer.username)
    return render(request,'home/buyitem.html',{'item': item,"cart":cart ,'buyer':buyer})


    
def TandC_view(request):
    return render(request,'home/tc.html')