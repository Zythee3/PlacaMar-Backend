from rest_framework import serializers
from .models import Admin
from django.contrib.auth.password_validation import validate_password

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'username', 'email']

class AdminCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = Admin
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = Admin.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

from .models import HistoricoLocalizacao
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class HistoricoLocalizacaoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = HistoricoLocalizacao
        geo_field = "ponto"
        fields = ['id', 'ponto', 'timestamp']
