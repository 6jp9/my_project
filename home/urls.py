from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/',views.orders,name='orders'),
    path('addproduct/<str:username>/',views.add_product),
    path('product/<int:product_id>',views.product_dtls),
    path('api_product/<int:id>',views.api_product_dtls),
]