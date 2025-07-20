from django.contrib.auth.models import AbstractUser
from django.db import models

class Admin(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions ' 
            'granted to each of their groups.'
        ),
        related_name="admin_set",
        related_query_name="admin",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="admin_set",
        related_query_name="admin",
    )

    def __str__(self):
        return self.username

from django.contrib.gis.db import models as gis_models

class HistoricoLocalizacao(models.Model):
    usuario = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='historico_localizacao')
    ponto = gis_models.PointField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
