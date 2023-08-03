from rest_framework import serializers
from cartapi.models import Product
from cartapi.serializers import UserSerializer

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for products"""
    quantity = serializers.IntegerField(default=None)
    seller = UserSerializer()

    class Meta:
        model = Product
        fields = ('id', 
                  'seller',
                  'name',
                  'price',
                  'description',
                  'stock',
                  'image_url',
                  'quantity'
                  )
        depth = 1
