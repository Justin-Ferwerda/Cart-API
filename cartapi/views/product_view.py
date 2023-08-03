from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.db.models import Count
from cartapi.models import Product, Order
from cartapi.serializers import ProductSerializer

class ProductView(ViewSet):

    def list(self, request):
        """returns a list of all products currently in user's cart"""
