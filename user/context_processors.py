from .models import Merchants

def merchant_context(request):
    is_merchant = False
    if request.user.is_authenticated:
        is_merchant = Merchants.objects.filter(username=request.user.username).exists()
    return {
        "is_merchant": is_merchant
    }
