from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Placa
from .serializers import PlacaSerializer

class PlacaListView(APIView):
    def get(self, request):
        placas = Placa.objects.all()
        serializer = PlacaSerializer(placas, many=True)
        return Response(serializer.data)
