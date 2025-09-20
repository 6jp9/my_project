from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path("delete_cart/<int:cart_id>/", views.delete_from_cart, name="delete_from_cart"),
    path('increment/<int:cart_id>/', views.increment_item, name='increment'),
    path('decrement/<int:cart_id>/', views.decrement_item, name = 'decrement'),

]