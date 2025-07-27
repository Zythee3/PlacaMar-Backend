from django.db import models
from django.contrib.auth.models import AbstractUser

PAISES_CHOICES = [
    ('Argentina', 'Argentina'),
    ('Bolívia', 'Bolívia'),
    ('Brasil', 'Brasil'),
    ('Chile', 'Chile'),
    ('Colômbia', 'Colômbia'),
    ('Costa Rica', 'Costa Rica'),
    ('Cuba', 'Cuba'),
    ('República Dominicana', 'República Dominicana'),
    ('Equador', 'Equador'),
    ('El Salvador', 'El Salvador'),
    ('Guatemala', 'Guatemala'),
    ('Honduras', 'Honduras'),
    ('México', 'México'),
    ('Nicarágua', 'Nicarágua'),
    ('Panamá', 'Panamá'),
    ('Paraguai', 'Paraguai'),
    ('Peru', 'Peru'),
    ('Porto Rico', 'Porto Rico'),
    ('Uruguai', 'Uruguai'),
    ('Venezuela', 'Venezuela'),
    ('Estados Unidos', 'Estados Unidos'),
    ('Canadá', 'Canadá'),
    ('Portugal', 'Portugal'),
    ('Espanha', 'Espanha'),
    ('França', 'França'),
    ('Alemanha', 'Alemanha'),
    ('Reino Unido', 'Reino Unido'),
    ('Itália', 'Itália'),
    ('Japão', 'Japão'),
    ('China', 'China'),
    ('Austrália', 'Austrália'),
    ('Outro', 'Outro'),
]

class Usuario(AbstractUser):
    tipo_perfil = models.CharField(max_length=50, default='Turista')
    idade = models.IntegerField(null=True, blank=True)
    pais_origem = models.CharField(max_length=255, choices=PAISES_CHOICES, default='Brasil')
    estado_origem = models.CharField(max_length=255, null=True, blank=True)
    cidade_origem = models.CharField(max_length=255, null=True, blank=True)
    sexo = models.CharField(max_length=10, null=True, blank=True)
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