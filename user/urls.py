from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_view, name='logout'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('adduserdtls/<str:username>/',views.customer_form,name='customer_dtls'),
    path('merchant_signup/<str:username>/',views.merchant_form),
    path('merchant_profile/<str:username>/',views.merchant_profile,name='merchant_profile'),
    path('delete_item/<int:product_id>/', views.delete_item, name='delete_item')
]