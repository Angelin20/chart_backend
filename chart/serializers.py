from rest_framework import serializers

from . import models

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chart
        fields = '__all__'