import json
from django.core.management.base import BaseCommand
from api.placas.models import Placa

class Command(BaseCommand):
    help = 'Importa os dados do arquivo GeoJSON para o banco de dados'

    def handle(self, *args, **kwargs):
        file_path = '/home/guest/Documentos/Plataforma-PlacaMar Backend/GeoJSON/Projeto-de-Geolocalizacao-ZATAN-Equipe-InovaRepe-Desafio-7/placas_placM.geojson'
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for feature in data['features']:
            props = feature['properties']
            coords = feature['geometry']['coordinates']

            Placa.objects.create(
                nome_placa=props.get('nome_placa', ''),
                subzona=props.get('subzona', ''),
                localidade=props.get('localidade', ''),
                embarcacoes=props.get('embarcacoes', 0),
                usuarios=props.get('usuarios', 0),
                cor=props.get('cor', '#000000'),
                descricao=props.get('descricao', ''),
                longitude=coords[0],
                latitude=coords[1]
            )
        
        self.stdout.write(self.style.SUCCESS('Importação concluída com sucesso.'))
