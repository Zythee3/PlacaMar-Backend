
import json
import os
from django.core.management.base import BaseCommand
from api.areas.models import AreaPermitida
from django.contrib.gis.geos import Polygon

class Command(BaseCommand):
    help = 'Importa as áreas do arquivo areas.geojson para o banco de dados'

    def handle(self, *args, **kwargs):
        caminho = os.path.join('api', 'placas', 'data', 'areas.geojson')

        with open(caminho, 'r', encoding='utf-8') as f:
            geojson = json.load(f)

        AreaPermitida.objects.all().delete()
        count = 0

        for feature in geojson['features']:
            props = feature['properties']
            geom = feature['geometry']

            if geom['type'] == 'Polygon':
                coords = geom['coordinates'][0]
                polygon = Polygon(coords)

                AreaPermitida.objects.create(
                    nome=props.get('name', 'Sem nome'),
                    geom=polygon
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f'{count} áreas importadas com sucesso.'))
