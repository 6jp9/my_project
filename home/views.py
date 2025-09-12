from django.shortcuts import render
from .forms import ProductForms

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def orders(request):
    return render(request,'user/my_orders.html')
def add_product(request):
    form = ProductForms()
    return render(request,'home/addproductform.html',{'form':form})