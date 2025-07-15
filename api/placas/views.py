from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Placa
from .serializers import PlacaSerializer

class PlacaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Placa.objects.all()
    serializer_class = PlacaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
