from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import AreaPermitida

class AreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AreaPermitida
        geo_field = "geom"
        fields = ("id", "name")