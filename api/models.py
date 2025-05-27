from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Outros campos do seu modelo
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Adicionando o related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_set',  # Adicionando o related_name
        blank=True
    )
