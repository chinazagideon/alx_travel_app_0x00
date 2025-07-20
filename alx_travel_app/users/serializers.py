# users/serializers.py
"""
Serializers for the users app
"""
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at', 'updated_at']

class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the user detail
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at', 'updated_at']