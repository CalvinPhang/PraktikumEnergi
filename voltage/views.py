from rest_framework import viewsets, generics
from . import models, serializers

class VoltageViewSet(viewsets.ModelViewSet):
    queryset = models.Voltage.objects.all()
    serializer_class = serializers.VoltageSerializer
    
class VoltageCreate(generics.CreateAPIView):
    queryset = models.Voltage.objects.all()
    serializer_class = serializers.VoltageSerializer