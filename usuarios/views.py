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
    Usuários do tipo secretaria veem apenas os usuários vinculados à sua secretaria.
    """

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_secretaria and user.secretaria:
            return Usuario.objects.filter(secretaria=user.secretaria)
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


class SecretariaDashboardView(APIView):
    """
    Endpoint para dashboard de secretarias.
    Somente usuários do tipo secretaria autenticados podem acessar.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if not user.is_secretaria:
            return Response({"erro": "Acesso negado."}, status=status.HTTP_403_FORBIDDEN)

        if not user.secretaria:
            return Response({"erro": "Usuário sem secretaria vinculada."}, status=status.HTTP_403_FORBIDDEN)

        # Implementar lógica real para filtrar dados conforme a secretaria do usuário
        dados_filtrados = {
            "msg": f"Dados restritos à secretaria {user.secretaria.nome} - região {user.secretaria.regiao}"
        }

        return Response(dados_filtrados, status=status.HTTP_200_OK)
