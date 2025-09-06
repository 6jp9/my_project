from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def orders(request):
    return render(request,'user/my_orders.html')
