from django.shortcuts import render,redirect
from .forms import ProductForms
from user.models import Merchants
from .models import Products
# Create your views here.
def home(request):
    Product = Products.objects.all()
    return render(request,'home/home.html',{'product':Product})
def orders(request):
    return render(request,'user/my_orders.html')
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