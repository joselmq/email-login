from django.contrib.auth import get_user_model
from rest_framework import serializers


class MyUserSerializer(serializers.ModelSerializer):
    """
    Write your own User serializer.
    """
    class Meta:
        model = get_user_model()
        fields = 'email'


class MyUserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = 'email'
