from rest_framework import generics
from .models import Placa
from .serializers import PlacaSerializer

class PlacaListAPIView(generics.ListAPIView):
    queryset = Placa.objects.all()
    serializer_class = PlacaSerializer
