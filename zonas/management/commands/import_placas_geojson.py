import os
import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from zonas.models import Zona, Placa

class Command(BaseCommand):
    help = 'Importa dados de placas de um arquivo GeoJSON para o banco de dados.'

    def handle(self, *args, **options):
        geojson_path = os.path.join('placasjson', 'placas.geojson')

        if not os.path.exists(geojson_path):
            self.stderr.write(self.style.ERROR(f'Arquivo GeoJSON não encontrado em: {geojson_path}'))
            return

        with open(geojson_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.stdout.write(self.style.SUCCESS('Iniciando importação de placas...'))

        for feature in data['features']:
            properties = feature['properties']
            geometry = feature['geometry']

            # Extrair nome da zona
            zona_nome = properties.get('zona')
            if not zona_nome:
                self.stderr.write(self.style.WARNING(f'Placa sem nome de zona, pulando: {properties.get("nome_placa", "N/A")}'))
                continue

            # Obter ou criar a Zona
            zona, created = Zona.objects.get_or_create(nome=zona_nome)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Zona "{zona_nome}" criada.'))

            # Extrair coordenadas
            longitude, latitude = geometry['coordinates']
            location = Point(longitude, latitude, srid=4326) # SRID 4326 para WGS84

            # Mapear campos do GeoJSON para o modelo Placa
            # Note: O modelo Placa em zonas/models.py tem campos diferentes do modelo antigo.
            # Estou mapeando para os campos do modelo Placa em zonas/models.py
            # Se houver campos no GeoJSON que não se encaixam, eles serão ignorados ou precisarão de tratamento.

            # O campo 'codigo_qr' no modelo Placa (zonas/models.py) é unique=True.
            # Vou usar 'nome_placa' do GeoJSON como 'codigo_qr' para evitar duplicatas e ter um identificador.
            # Se 'nome_placa' não for único no GeoJSON, isso causará um erro.
            codigo_qr = properties.get('nome_placa', f'Placa-{properties.get("nº", "N/A")}')

            # Criar ou atualizar a Placa
            placa_data = {
                'zona': zona,
                'descricao': properties.get('descricao_(conteudo)'),
                'atividades_autorizadas': properties.get('atividades permitidas'), # JSONField, pode precisar de parse mais complexo
                'latitude': latitude,
                'longitude': longitude,
                # 'ponto_interesse': ... (não mapeado diretamente do GeoJSON, pode ser adicionado depois)
            }

            try:
                placa, created = Placa.objects.update_or_create(
                    codigo_qr=codigo_qr,
                    defaults=placa_data
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Placa "{placa.codigo_qr}" criada.'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Placa "{placa.codigo_qr}" atualizada.'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Erro ao processar placa "{codigo_qr}": {e}'))

        self.stdout.write(self.style.SUCCESS('Importação de placas concluída.'))
