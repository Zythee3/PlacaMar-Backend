from rest_framework import serializers
from .models import Placa

class PlacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placa
        fields = '__all__'
