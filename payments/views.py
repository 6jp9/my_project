import stripe
from django.shortcuts import render,get_object_or_404,redirect
from Payment_Gateway import settings
from cartapp import models
from home.models import Products
from django.contrib.auth.decorators import login_required
# Create your views here.

DOMAIN = "http://127.0.0.1:8000/"
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request,cart_id):
    cart = get_object_or_404(models.Cart,cart_id=cart_id)
    checkout_session = stripe.checkout.Session.create(
        # payment_method_types=['card', 'upi', 'netbanking'],
        line_items=[
            {
            'price_data': {
                'currency': 'inr',  # INR for India
                'product_data': {
                    'name': cart.product.name,
                    },
                'unit_amount': int(cart.price/cart.quantity * 100),  # amount in paise
            },
            'quantity': cart.quantity,
            },
        ],
        mode='payment',
        success_url=DOMAIN + f'success/?cart_id={cart_id}',
        cancel_url=DOMAIN + f'cancel/?cart_id={cart_id}',
        metadata={
        "cart_id": str(cart.cart_id),
        }
    )
    return redirect(checkout_session.url, code=303)

def payment_success(request):
    session_id = request.GET.get('session_id')
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)
        cart_id = session.metadata.get('cart_id')
        cart = models.Cart.objects.get(cart_id=cart_id)
        
    return render(request, 'payments/payment_success.html')

def payment_cancel(request):
    cart_id = request.GET.get('cart_id')
    return render(request, 'payments/payment_cancel.html',{'cart_id':cart_id})
