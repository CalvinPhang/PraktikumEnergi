from rest_framework import serializers
from . import models

class VoltageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Voltage
        fields = '__all__'