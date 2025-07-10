from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def usuarios_view(request):
    # Exemplo simples: lista de usuários fictícios
    usuarios = [
        {"id": 1, "nome": "João"},
        {"id": 2, "nome": "Maria"},
        {"id": 3, "nome": "Ana"},
    ]
    return Response({"usuarios": usuarios})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    # Exemplo de dados para dashboard
    dados = {
        "total_usuarios": 100,
        "novos_cadastros": 5,
        "atividade": "Tudo funcionando!"
    }
    return Response({"dashboard": dados})
