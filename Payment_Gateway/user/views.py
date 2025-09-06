from django.shortcuts import render

# Create your views here.
def profile(request):
    return render (request,'user/profile.html')
def signup(request):
    return render(request,'user/signup.html')
# def login(request):
#     return render(request,'user/signup.html')
