from rest_framework import generics
from .models import Area
from .serializers import AreaSerializer
from rest_framework.permissions import AllowAny

class AreaList(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [AllowAny]  # permite acesso público
