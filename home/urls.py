from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api',views.ProductsCRUD_View)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/',views.orders,name='orders'),
    path('addproduct/<str:username>/',views.add_product),
    path('product/<int:product_id>/',views.product_dtls,name='product'),
    path('buyitem/<int:cart_id>/',views.buy_item,name='buy_item'),
    path('terms_and_conditions/',views.TandC_view,name='terms&conditions'),
    path('',include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('order_dtls/<int:order_id>',views.order_dtils,name='order_dtls'),
    path('editproduct/<int:product_id>/',views.alter_product_dtls_form),
    path('order_dashboard/<int:merchant_id>/',views.merchant_orders)
]