from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cartapi.views import OrderView, OrderItemView, ProductView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'orders', OrderView, 'order')
router.register(r'order_items', OrderItemView, 'order_item')
router.register(r'products', ProductView, 'product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
