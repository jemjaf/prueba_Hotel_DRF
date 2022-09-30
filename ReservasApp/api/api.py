from rest_framework.response import Response
from rest_framework.views import APIView
from ReservasApp.models import Reserva
from .serializers import ReservaSerializer

class ReservaAPIView(APIView):

    def get(self,request):
        #Traemos todas las reservas
        reservas = Reserva.objects.all()
        #Convertimos de Django a JSON
        reservas_serializer = ReservaSerializer(reservas , many = True)
        return Response(reservas_serializer.data, )