from django.urls import path
from . import views

urlpatterns = [
    path('checkout_session/<int:cart_id>/',views.create_checkout_session,name='checkout_session'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
    path('stripe/webhook',views.stripe_webhook,name='stripe_webhook'),
]