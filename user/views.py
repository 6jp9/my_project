from django.shortcuts import render,redirect
from .forms import SignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Customers
from django.utils.timezone import now

# Create your views here.
def profile(request):
    return render (request,'user/profile.html')

############################################################

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password']) 
#             user.save()
#             return HttpResponseRedirect('/accountslogin')
#     else:
#         form = SignupForm()
#     return render(request, 'user/signup.html', {'form': form})
# def logout_view(request):
#     return render(request,'user/custom_logout.html')


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


            #inserting the similar user records into customer table as well
            Customers.objects.create(
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            created_at=now()
            )


            # Clear session data
            del request.session['signup_data']
            del request.session['otp']

            return redirect('/accountslogin')
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
                subject='Shop-Kart Email Verification',
                message = f"Hello {form.cleaned_data['username']},\nYour OTP for verification is {otp}.",
                from_email='jayaprakash1405401@gmail.com',
                recipient_list=[form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('verify_otp')
    else:
        form = SignupForm()
        
    return render(request, 'user/signup.html', {'form': form})

def logout_view(request):
    return render(request,'user/custom_logout.html')

