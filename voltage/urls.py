from rest_framework_nested import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'voltages', views.VoltageViewSet)

urlpatterns = [
    path('', views.VoltageCreate.as_view()),
]