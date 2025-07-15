from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # ou AllowAny, conforme a necessidade
from .models import Placa
from .serializers import PlacaSerializer  # Crie este serializer

class PlacaListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        placas = Placa.objects.all()
        serializer = PlacaSerializer(placas, many=True)
        return Response(serializer.data)
