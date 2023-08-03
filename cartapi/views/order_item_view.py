from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from cartapi.models import OrderItem, Product, Order, User

class OrderItemView(ViewSet):

    def create(self, request):
        """POST request for order_item or 'cart item' for user's cart
        Two conditions for this method: a user already has an open order, or a user does not have an open order and one must be created"""

    def destroy(self, request, pk):
        """DELETE request to remove item from cart
        handles two conditions: removing a single item from cart, and removing all instances of product from cart
        pk=product id"""
