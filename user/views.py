from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignupForm,CustomerDetailsForm,MerchantDetailsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Customers,Merchants
from django.utils.timezone import now
from home.models import Products
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):
    customer = None
    if request.user.is_authenticated:
        try:
            customer = Customers.objects.get(email=request.user.email)
        except Customers.DoesNotExist:
            customer = None
    return render(request, "user/profile.html", {"customer": customer})

def merchant_profile(request,username):
    merchant = Merchants.objects.get(username=username)
    products = Products.objects.filter(merchant_id = merchant.merchant_id)
    return render(request,'user/merchant_profile.html',{'merchant':merchant,'products':products})

def merchant_product_dtls(request,product_id):
    product = Products.objects.get(product_id=product_id)
    return render(request,'user/merchant_product.html',{'product':product})

#############################################################

def verify_otp(request):
    data = request.session.get('signup_data')
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        real_otp = request.session.get('otp')

        if entered_otp == real_otp:
            # Create and save the user
            user = User(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            user.set_password(data['password'])  # To Hash the user text password
            user.save()


            #Inserting the user records into customer table as well
            Customers.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            created_at=now()
            )

            # Clear session data
            del request.session['signup_data']
            del request.session['otp']

            return redirect('/accounts/login')
        else:
            return render(request, 'user/otpverify.html', {'error': 'Invalid OTP'})
    
    email = data['email']
    return render(request, 'user/otpverify.html',{'email': email})


from django.core.mail import send_mail
from random import randint

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():

            # Store user data in session temporarily
            request.session['signup_data'] = form.cleaned_data
            otp = str(randint(100000, 999999))
            request.session['otp'] = otp

            # Send OTP to email
            send_mail(
                subject='Shop@JP Email Verification',
                message = f"Hello {form.cleaned_data['username']},\n\nYour One-Time Password (OTP) for verification is:\n\n {otp} \n\nPlease use this OTP to complete your verification process.\n\nImportant Notes:\n\t-This OTP is valid for 10 minutes only.\n\t-Do not share this OTP with anyone.\n\nIf you did not request this, please ignore this email.\n\nThank you for using Shop@JP!\nWe’re committed to keeping your account secure.\n\nBest regards,\nThe Shop@JP Team",
                from_email='shopkart.jp@gmail.com',
                recipient_list=[form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('verify_otp')
    else:
        form = SignupForm()
        
    return render(request, 'user/signup.html', {'form': form})

def logout_view(request):
    return render(request,'user/custom_logout.html')


##################################################################

def customer_form(request,username):
    temp = Customers.objects.get(username=username)
    form = CustomerDetailsForm(instance=temp)
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST,instance=temp)
        if form.is_valid():
            form.save()
        next_url = request.POST.get('next', '/')
        return redirect(next_url)
    return render(request,'user/add_dtls.html',{'form':form})

def merchant_form(request,username):
    temp = Customers.objects.get(username=username)
    if request.method == 'POST':
        form = MerchantDetailsForm(request.POST)
        if form.is_valid():
            merchant = form.save(commit=False)
            merchant.user=temp.user
            merchant.username = temp.username
            merchant.email = temp.email
            merchant.created_at = now()
            merchant.save()
        return redirect('/')
    else:
        form = MerchantDetailsForm()
    return render(request,'user/signup.html',{'form':form})


def delete_item(request,product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Products,product_id=product_id)
        product.delete()
        return redirect(reverse('merchant_profile',args=[request.user.username]))
    return render('home')