from rest_framework import serializers
from .models import Usuario, Secretaria
from django.contrib.auth.password_validation import validate_password

class SecretariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretaria
        fields = ['id', 'nome', 'regiao']

class UsuarioSerializer(serializers.ModelSerializer):
    secretaria = SecretariaSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'is_secretaria', 'secretaria']

class UsuarioCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    secretaria_id = serializers.PrimaryKeyRelatedField(
        queryset=Secretaria.objects.all(),
        source='secretaria',
        write_only=True,
        required=False
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'is_secretaria', 'secretaria_id']

    def create(self, validated_data):
        secretaria = validated_data.pop('secretaria', None)
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_secretaria=validated_data.get('is_secretaria', False),
            secretaria=secretaria if secretaria else None  # garante None se for vazio
        )
        return user

