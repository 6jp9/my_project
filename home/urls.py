from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/',views.orders,name='orders'),
    path('addproduct/<str:username>/',views.add_product),
    path('product/<int:product_id>',views.product_dtls,name='product'),
    path('buyitem/<int:cart_id>',views.buy_item,name='buy_item'),
    path('terms_and_conditions/',views.TandC_view,name='terms&conditions'),
]