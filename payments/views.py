import stripe
from django.shortcuts import render,get_object_or_404,redirect
from Payment_Gateway import settings
from cartapp.models import Cart
from user.models import Customers,Merchants
from home.models import Products,Orders
from .models import Payments
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.utils import timezone
from decimal import Decimal
# Create your views here.

# DOMAIN = "http://127.0.0.1:8000/"
DOMAIN = "https://phagolytic-intramolecular-evelin.ngrok-free.dev/"
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request,cart_id):
    cart = get_object_or_404(Cart,cart_id=cart_id)
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
         
        metadata={"cart_id": str(cart.cart_id)},
        mode='payment',
        success_url=DOMAIN + f'success/?cart_id={cart_id}',
        cancel_url=DOMAIN + f'cancel/?cart_id={cart_id}',
       
    )
    return redirect(checkout_session.url, code=303)

def payment_success(request):
    session_id = request.GET.get('session_id')
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)
        cart_id = session.metadata.get('cart_id')
        cart = Cart.objects.get(cart_id=cart_id)
        
    return render(request, 'payments/payment_success.html')

def payment_cancel(request):
    cart_id = request.GET.get('cart_id')
    return render(request, 'payments/payment_cancel.html',{'cart_id':cart_id})

@csrf_exempt
def stripe_webhook(request):
    if request.method != 'POST':
       return HttpResponse("OK")  # ignore GET requests

    event = None
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        cart_id = session['metadata']['cart_id']
        cart = get_object_or_404(Cart,cart_id=cart_id)
        merchant = cart.product.merchant
        order = Orders.objects.create(
            customer = cart.customer,
            merchant = merchant,
            product = cart.product,
            quantity = cart.quantity,
            price = cart.price
        )
        
        print("✅ Order updated!!")

        stripe_fee = round(cart.price * 0.029 + 3, 2)
        platform_fee = round(cart.price*0.1,2)
        merchant_amount = cart.price - stripe_fee - platform_fee
        payment_intent_id = session['payment_intent']
        Payments.objects.create(
            payment_id = payment_intent_id,
            order = order,
            merchant = merchant,
            total_amount = cart.price,
            stripe_cut = stripe_fee,
            platform_cut = platform_fee,
            merchant_amount = merchant_amount,
        )

        print("✅ Payments updated!!")
        product = cart.product
        product.stock -= cart.quantity
        product.save()
        cart.delete()
        print('✅ Cart and product updated')
        merchant.total_revenue += Decimal(merchant_amount)
        merchant.save()
        print("✅ merchant revenue updated!!")



    elif event['type'] == 'checkout.session.async_payment_failed':
        session = event['data']['object']
    else:
        print('Unhandled event type {}'.format(event['type']))
    return HttpResponse(status=200)

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe



@csrf_exempt
def refund_payment(request, payment_id):
    if request.method == "POST":
        payment = get_object_or_404(Payments, payment_id=payment_id)
        
        # Create refund on Stripe
        refund = stripe.Refund.create(payment_intent=payment.payment_id)

            # Update order database
        payment.order.status = "Canceled"
        payment.order.save()
        payment.is_refunded = True
        payment.refund_id = refund.id
        payment.refund_amount = refund.amount / 100  # convert cents to dollars
        payment.refund_date = timezone.now()
        payment.save()

        # Update merchant revenue
        merchant = payment.merchant
        merchant.total_revenue -= Decimal(refund.amount) / 100
        merchant.save()

        print(f"✅ Refund processed successfully for {payment.payment_id}")
        return render(request,'payments/payment_cancel.html', {"refund_id": refund.id})
    return render(request,'payments/payment_cancel.html',{'refund_id':refund.id})
