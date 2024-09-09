from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.db.models import Count
from cartapi.models import Product, Order
from cartapi.serializers import ProductSerializer

class ProductView(ViewSet):

    def list(self, request):
        """returns a list of all products currently in user's cart"""
        products = Product.objects.all()
        user = request.META['HTTP_AUTHORIZATION']
        if user is not None:
            order=Order.objects.get(buyer=user, is_open=True)
            products = Product.objects.filter(order_products__order=order).annotate(quantity=Count('order_products'))

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
