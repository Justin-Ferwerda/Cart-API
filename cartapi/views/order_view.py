from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from cartapi.models import Order, User, PaymentType

class OrderView(ViewSet):

    def update(self, request, pk):
        """PUT request to submit an order.
        When an order is submitted, it is not deleted, but is_open is set to False
        PK = payment_type id"""
