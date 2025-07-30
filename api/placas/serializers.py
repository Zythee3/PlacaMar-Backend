from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Placa

class PlacaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Placa
        geo_field = "location"
        fields = (
            'id',
            'nome_placa',
            'localidade',
            'zona',
            'atividades_permitidas',
            'qtd_placas',
            'descricao',
            'num_embarcacoes',
            'max_pessoas_catamara',
            'max_pessoas_miudas',
        )
