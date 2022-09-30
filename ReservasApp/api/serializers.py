from rest_framework import serializers
from ReservasApp.models import Reserva

#Para convertir a JSON mis consultas
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
