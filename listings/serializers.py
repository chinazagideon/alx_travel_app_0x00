# listings/serializers.py
"""
Serializers for the listings app
"""
from rest_framework import serializers
from .models import Listing
from users.serializers import UserDetailSerializer
from addresses.serializers import AddressDetailSerializer

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the listing
    """
    class Meta:
        model = Listing
        fields = '__all__'  

class ListingDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the listing detail
    """
    owner = UserDetailSerializer(read_only=True)
    address = AddressDetailSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = '__all__'
        depth = 1