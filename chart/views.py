from rest_framework import generics
from . import models
from . import serializers

class ChartList(generics.ListAPIView):
    queryset = models.Chart.objects.all()
    serializer_class = serializers.ChartSerializer

class ChartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chart.objects.all()
    serializer_class = serializers.ChartSerializer
