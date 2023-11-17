from django.db import models

class Voltage(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    voltage = models.CharField(max_length=255)
