from django.core.management.base import BaseCommand
from django.contrib.gis.gdal import DataSource
from api.areas.models import Area

class Command(BaseCommand):
    help = 'Importa áreas protegidas a partir do GeoJSON'

    def handle(self, *args, **kwargs):
        ds = DataSource('api/areas/data/Areas.geojson')
        layer = ds[0]

        for feat in layer:
            geom = feat.geom.geos
            name = feat.get('name')
            Area.objects.create(name=name, geom=geom)

        self.stdout.write(self.style.SUCCESS('Áreas importadas com sucesso!'))
