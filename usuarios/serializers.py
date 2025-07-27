from rest_framework import serializers
from .models import Usuario
from api.models import Estado, Cidade
from django.contrib.auth.password_validation import validate_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'tipo_perfil', 'criado_em']
        read_only_fields = ['criado_em']

class UsuarioCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    estado_origem = serializers.PrimaryKeyRelatedField(queryset=Estado.objects.all(), allow_null=True, required=False)
    cidade_origem = serializers.PrimaryKeyRelatedField(queryset=Cidade.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'tipo_perfil', 'idade', 'estado_origem', 'pais_origem', 'cidade_origem', 'sexo']

    def create(self, validated_data):
        estado_origem_data = validated_data.pop('estado_origem', None)
        cidade_origem_data = validated_data.pop('cidade_origem', None)

        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            tipo_perfil=validated_data.get('tipo_perfil', 'Turista'),
            idade=validated_data.get('idade'),
            pais_origem=validated_data.get('pais_origem'),
            sexo=validated_data.get('sexo'),
        )
        user.estado_origem = estado_origem_data
        user.cidade_origem = cidade_origem_data
        user.save()
        return user