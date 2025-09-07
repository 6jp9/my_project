from django.shortcuts import render

# Create your views here.
def profile(request):
    return render (request,'user/profile.html')
def signup(request):
    return render(request,'user/signup.html')
def logout_view(request):
    return render(request,'user/custom_logout.html')
