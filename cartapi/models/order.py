from django.db import models
from .user import User
from .payment_type import PaymentType

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete = models.CASCADE, related_name='orders')
    date = models.DateField(null=True)
    shipped = models.BooleanField(default=False)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, related_name='order_payments', null=True)
    is_open = models.BooleanField(default=True)
