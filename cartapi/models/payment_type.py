from django.db import models

class PaymentType(models.Model):
    name=models.CharField(max_length=50)
