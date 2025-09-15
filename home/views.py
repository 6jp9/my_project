from django.shortcuts import render,redirect
from .forms import ProductForms
from user.models import Merchants
from .models import Products
import requests
# Create your views here.
def home(request):
    Product = Products.objects.all()
    url = f"https://fakestoreapi.com/products/"
    response = requests.get(url)
    api_product = response.json()
    return render(request,'home/home.html',{'product':Product,'api':api_product})
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

def product_dtls(request,product_id):
    product = Products.objects.get(product_id=product_id)
    return render(request,'home/product.html',{'product':product})

def api_product_dtls(request,id):
    url = f'https://fakestoreapi.com/products/{id}'
    response = requests.get(url)
    item = response.json()
    return render(request,'home/product.html',{'item':item})