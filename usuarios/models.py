from django.contrib.auth.models import AbstractUser
from django.db import models

class Secretaria(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    is_secretaria = models.BooleanField(default=False)
    secretaria = models.ForeignKey(
        Secretaria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuarios'
    )
    def __str__(self):
        return self.username
