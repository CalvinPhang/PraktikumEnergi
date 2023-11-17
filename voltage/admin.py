from django.contrib import admin
from . import models

@admin.register(models.Voltage)
class VoltageAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp',
        'voltage'
    )
