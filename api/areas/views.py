from rest_framework import generics
from api.areas.models import AreaPermitida
from api.areas.serializers import AreaSerializer
from rest_framework.permissions import AllowAny

class AreaList(generics.ListAPIView):
    queryset = AreaPermitida.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [AllowAny]  # permite acesso público