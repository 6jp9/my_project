from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForms
from user.models import Merchants,Customers
from .models import Products,Orders
from cartapp.models import Cart
import requests
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from payments.models import Payments
# Create your views here.
def home(request):
    query = request.GET.get('q', '')
    if query:
        products = Products.objects.filter(name__icontains=query)
    else:
        products = Products.objects.all()
    return render(request, 'home/home.html', {'products': products, 'query': query})

def orders(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            customer = get_object_or_404(Customers, username=request.user.username)
            level = request.GET.get('level', 'All')
            orders = Orders.objects.filter(customer_id=customer.customer_id).select_related('product')
            if level == "Ordered":
                orders = orders.filter(status="Ordered")
            elif level == "Canceled":
                orders = orders.filter(status="Canceled")
            context = {
                'orders': orders,
                'selected_level': level
            }
            return render(request, 'home/my_orders.html', context)
    return render(request, 'home/my_orders.html', {'orders': [], 'selected_level': 'All'})


def order_dtils(request,order_id):
    order = Orders.objects.get(order_id = order_id)
    customer = order.customer
    name = customer.first_name +'-'+ customer.last_name
    address = customer.address
    payment = Payments.objects.get(order_id=order.order_id)
    payment_id = payment.payment_id
    return render(request,'home/order.html',{'order':order,'name':name,'address':address,'payment':payment,'payment_id':payment_id})

@login_required
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
    product = get_object_or_404(Products, product_id=product_id)
    in_cart=  False
    quantity=0
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            customer = Customers.objects.get(username = request.user.username)
            in_cart = Cart.objects.filter(customer=customer,product=product)
            if in_cart.exists():
                quantity = in_cart.first().quantity
                cart_id = in_cart.first().cart_id
        return render(request,'home/product.html',{'product':product,'in_cart':in_cart,'quantity':quantity,'cart_id':cart_id})
    return render(request,'home/product.html',{'product':product})

@login_required
def buy_item(request,cart_id):
    cart = Cart.objects.get(cart_id=cart_id)
    buyer =  Customers.objects.get(customer_id = cart.customer.customer_id)
    item = Products.objects.get(product_id = cart.product.product_id)
    if buyer.address==None or buyer.phone==None:
        return redirect('customer_dtls',username=buyer.username)
    return render(request,'home/buyitem.html',{'item': item,"cart":cart ,'buyer':buyer})


    
def TandC_view(request):
    return render(request,'home/tc.html')


class ProductsCRUD_View(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


def alter_product_dtls_form(request,product_id):
    temp = Products.objects.get(product_id=product_id)
    if request.user.username == temp.merchant.username:
        form = ProductForms(instance=temp)
        if request.method == 'POST':
            form = ProductForms(request.POST,request.FILES,instance=temp)
            if form.is_valid():
                form.save()
            return redirect(f'/merchant_profile/{temp.merchant.username}/')
        return render(request,'home/addproductform.html',{'form':form})
    return HttpResponse('<h2>Access Denied</h2>')

@login_required
def merchant_orders(request,merchant_id):
    merchant = Merchants.objects.get(merchant_id=merchant_id)
    active_payments = Payments.objects.filter(merchant_id=merchant_id, is_refunded=False)
    canceled_payments = Payments.objects.filter(merchant_id=merchant_id, is_refunded=True)
    total_revenue = merchant.total_revenue
    return render(request,'home/merchant_order.html',{'total_revenue':total_revenue,'active_payments':active_payments,'canceled_payments':canceled_payments})

