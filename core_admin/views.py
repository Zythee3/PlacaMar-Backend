import logging
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status

from .models import Admin
from .serializers import AdminSerializer, AdminCreateSerializer

logger = logging.getLogger(__name__)

class AdminViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para listar (GET) administradores. Apenas leitura.
    """

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset()


class AdminCreateView(APIView):
    """
    Endpoint para cadastro de novos administradores.
    Permite acesso público (sem autenticação).
    """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AdminCreateSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning(f"Erro de validação no cadastro: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = serializer.save()
        except Exception as e:
            logger.error(f"Erro ao salvar administrador: {e}", exc_info=True)
            return Response(
                {"detail": "Erro interno ao criar administrador."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        output_serializer = AdminSerializer(user)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

from .models import HistoricoLocalizacao
from .serializers import HistoricoLocalizacaoSerializer
from django.contrib.gis.geos import Point

class RegistrarLocalizacaoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = HistoricoLocalizacaoSerializer(data=request.data)
        if serializer.is_valid():
            # Pega latitude e longitude do corpo da requisição
            lat = request.data.get('lat')
            lon = request.data.get('lon')
            if lat is not None and lon is not None:
                ponto = Point(float(lon), float(lat), srid=4326)
                HistoricoLocalizacao.objects.create(usuario=request.user, ponto=ponto)
                return Response({"detail": "Localização registrada com sucesso."}, status=status.HTTP_201_CREATED)
            return Response({"detail": "Latitude e Longitude são obrigatórias."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeuRoteiroView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        historico = HistoricoLocalizacao.objects.filter(usuario=request.user)
        serializer = HistoricoLocalizacaoSerializer(historico, many=True)
        return Response(serializer.data)