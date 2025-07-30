import os
import json
import uuid
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from zonas.models import Zona, Subzona, Placa, Atividade, PlacaAtividade, QRCode

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

            # Extrair nome da subzona e da zona
            subzona_nome = properties.get('subzona')
            zona_nome = properties.get('zona')

            if not subzona_nome or not zona_nome:
                self.stderr.write(self.style.WARNING(f'Placa sem nome de subzona ou zona, pulando: {properties.get("nome_placa", "N/A")}'))
                continue

            # Obter ou criar a Zona
            zona, created_zona = Zona.objects.get_or_create(nome=zona_nome)
            if created_zona:
                self.stdout.write(self.style.SUCCESS(f'Zona "{zona_nome}" criada.'))

            # Obter ou criar a Subzona
            subzona, created_subzona = Subzona.objects.get_or_create(zona=zona, nome=subzona_nome)
            if created_subzona:
                self.stdout.write(self.style.SUCCESS(f'Subzona "{subzona_nome}" (Zona: {zona_nome}) criada.'))

            # Obter ou criar o QRCode
            qr_code_uuid_str = properties.get('qr_code_uuid')
            if qr_code_uuid_str:
                qr_code_obj, qr_created = QRCode.objects.get_or_create(code=qr_code_uuid_str)
            else:
                # Se não houver UUID no GeoJSON, gerar um novo
                qr_code_obj, qr_created = QRCode.objects.get_or_create(code=str(uuid.uuid4()))

            if qr_created:
                self.stdout.write(self.style.SUCCESS(f'QRCode "{qr_code_obj.code}" criado.'))

            # Extrair coordenadas
            latitude = properties.get('latitude')
            longitude = properties.get('longitude')

            if latitude is None or longitude is None:
                self.stderr.write(self.style.WARNING(f'Placa "{properties.get("nome_placa", "N/A")}" sem latitude ou longitude, pulando.'))
                continue

            placa_data = {
                'subzona': subzona,
                'nome_placa': properties.get('nome_placa'),
                'descricao': properties.get('descricao'),
                'localidade_x': properties.get('localidade_x'),
                'acesso_restrito': properties.get('acesso_restrito', False), # Default False
                'num_embarcacoes_desembarque': properties.get('num_embarcacoes_desembarque'),
                'max_pessoas_catamara': properties.get('max_pessoas_catamara'),
                'max_pessoas_miudas': properties.get('max_pessoas_miudas'),
                'atividades_autorizadas': properties.get('atividades_autorizadas'),
                'latitude': latitude,
                'longitude': longitude,
            }

            try:
                placa, created = Placa.objects.update_or_create(
                    qr_code=qr_code_obj,
                    defaults=placa_data
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Placa "{placa.nome_placa}" criada com QR Code: {qr_code_obj.code}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Placa "{placa.nome_placa}" atualizada com QR Code: {qr_code_obj.code}'))

                # Processar atividades
                atividades_str = properties.get('atividades_autorizadas')
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
                self.stderr.write(self.style.ERROR(f'Erro ao processar placa "{properties.get("nome_placa", "N/A")}": {e}'))

        self.stdout.write(self.style.SUCCESS('Importação de placas e atividades concluída.'))
