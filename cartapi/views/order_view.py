from datetime import date
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from cartapi.models import Order, User, PaymentType

class OrderView(ViewSet):

    def update(self, request, pk):
        """PUT request to submit an order.
        When an order is submitted, it is not deleted, but is_open is set to False
        PK = payment_type id"""
        user = User.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        order = Order.objects.get(is_open=True, buyer=user)
        payment_type = PaymentType.objects.get(pk=pk)
        order.is_open=False
        order.payment_type=payment_type
        order.date=date.today()
        order.save()
        return Response({'message': 'Order Closed'}, status=status.HTTP_204_NO_CONTENT)
