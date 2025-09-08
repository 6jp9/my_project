from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_view, name='logout'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
]