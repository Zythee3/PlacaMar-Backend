import logging
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status

from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioCreateSerializer

logger = logging.getLogger(__name__)

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para listar (GET) usuários. Apenas leitura.
    """

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset()


class UsuarioCreateView(APIView):
    """
    Endpoint para cadastro de novos usuários.
    Permite acesso público (sem autenticação).
    """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UsuarioCreateSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning(f"Erro de validação no cadastro: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = serializer.save()
        except Exception as e:
            logger.error(f"Erro ao salvar usuário: {e}", exc_info=True)
            return Response(
                {"detail": "Erro interno ao criar usuário."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        output_serializer = UsuarioSerializer(user)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)