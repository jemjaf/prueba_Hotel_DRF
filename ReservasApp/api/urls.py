from django.urls import path
from .api import ReservaAPIView

urlpatterns = [
    path('reserva/', ReservaAPIView.as_view(), name = 'reserva_api ')
]