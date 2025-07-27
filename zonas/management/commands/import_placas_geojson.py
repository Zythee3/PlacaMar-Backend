import os
import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from zonas.models import Zona, Placa, Atividade, PlacaAtividade

class Command(BaseCommand):
    help = 'Importa dados de placas de um arquivo GeoJSON para o banco de dados.'

    def handle(self, *args, **options):
        geojson_path = os.path.join('placasjson', 'placas.geojson')

        if not os.path.exists(geojson_path):
            self.stderr.write(self.style.ERROR(f'Arquivo GeoJSON não encontrado em: {geojson_path}'))
            return

        with open(geojson_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.stdout.write(self.style.SUCCESS('Iniciando importação de placas e atividades...'))

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

            codigo_qr = properties.get('nome_placa', f'Placa-{properties.get("nº", "N/A")}')

            placa_data = {
                'zona': zona,
                'descricao': properties.get('descricao_(conteudo)'),
                'atividades_autorizadas': properties.get('atividades permitidas'), # JSONField
                'latitude': latitude,
                'longitude': longitude,
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

                # Processar atividades
                atividades_str = properties.get('atividades permitidas')
                if atividades_str:
                    # Limpar atividades existentes para evitar duplicatas em atualizações
                    PlacaAtividade.objects.filter(placa=placa).delete()

                    atividades_list = [a.strip() for a in atividades_str.split(',') if a.strip()]
                    for atividade_nome in atividades_list:
                        atividade, created_atividade = Atividade.objects.get_or_create(nome=atividade_nome)
                        if created_atividade:
                            self.stdout.write(self.style.SUCCESS(f'Atividade "{atividade_nome}" criada.'))
                        PlacaAtividade.objects.create(placa=placa, atividade=atividade)

            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Erro ao processar placa "{qr_code_str}": {e}'))

        self.stdout.write(self.style.SUCCESS('Importação de placas e atividades concluída.'))