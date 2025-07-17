from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    tipo_perfil = models.CharField(max_length=50, default='Turista')
    # O campo email já é herdado de AbstractUser e é único por padrão
    # O campo senha_hash é gerenciado pelo Django (password)
    criado_em = models.DateTimeField(auto_now_add=True)

    # Adicionar related_name para evitar conflitos com AbstractUser
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions ' 
            'granted to each of their groups.'
        ),
        related_name="usuario_set",
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="usuario_set",
        related_query_name="usuario",
    )

    def __str__(self):
        return self.username