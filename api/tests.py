from django.test import TestCase
from .models import Usuario

class UsuarioModelTest(TestCase):
    def test_criacao_usuario(self):
        user = Usuario.objects.create_user(username="teste", password="senha123", role="turista")
        self.assertEqual(user.username, "teste")
        self.assertEqual(user.role, "turista")
