from rest_framework import serializers
from cartapi.models import User

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = User
        fields = (
                  'name',
                  'email', 
                  )
