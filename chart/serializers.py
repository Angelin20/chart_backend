from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from . import models

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chart
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user