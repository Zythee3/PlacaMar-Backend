from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Area

class AreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Area
        geo_field = "geom"
        fields = ("id", "name")
