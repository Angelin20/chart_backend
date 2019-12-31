from rest_framework import generics
from . import models
from . import serializers

class ChartList(generics.ListCreateAPIView):
    queryset = models.Chart.objects.all().order_by('-created_at', '-updated_at')
    serializer_class = serializers.ChartSerializer

class ChartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chart.objects.all()
    serializer_class = serializers.ChartSerializer
