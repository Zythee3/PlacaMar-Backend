from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.password_validation import validate_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'tipo_perfil', 'criado_em']
        read_only_fields = ['criado_em']

class UsuarioCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'tipo_perfil']

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            tipo_perfil=validated_data.get('tipo_perfil', 'Turista')
        )
        return user