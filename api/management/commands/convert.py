import pandas as pd
import json
import os

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Converte a planilha Excel em um arquivo GeoJSON'

    def add_arguments(self, parser):
        parser.add_argument(
            '--arquivo',
            type=str,
            default='/home/guest/Documentos/Plataforma-PlacaMar/PlacaMar-Backend/api/placas/data/Zatan_Tamandare.xlsx',
            help='Caminho para o arquivo Excel com os dados das placas',
        )
        parser.add_argument(
            '--saida',
            type=str,
            default='/home/guest/Documentos/Plataforma-PlacaMar/PlacaMar-Backend/placas.geojson',
            help='Caminho de saída do arquivo GeoJSON',
        )

    def handle(self, *args, **options):
        caminho_excel = options['arquivo']
        caminho_saida = options['saida']

        if not os.path.exists(caminho_excel):
            self.stderr.write(f"Arquivo não encontrado: {caminho_excel}")
            return

        # Lê a planilha
        df = pd.read_excel(caminho_excel)

        # Normaliza os nomes das colunas
        df.columns = df.columns.str.strip().str.lower()

        # Exibe as colunas para depuração
        print("Colunas encontradas:", df.columns.tolist())

        if 'latitude' not in df.columns or 'longitude' not in df.columns:
            self.stderr.write("Colunas obrigatórias 'latitude' e 'longitude' não encontradas no arquivo Excel.")
            return

        features = []

        for _, row in df.iterrows():
            try:
                latitude = float(row['latitude'])
                longitude = float(row['longitude'])
            except (ValueError, TypeError):
                continue  # Pula se não conseguir converter

            properties = row.drop(['latitude', 'longitude']).to_dict()

            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [longitude, latitude],
                },
                "properties": properties,
            }
            features.append(feature)

        geojson = {
            "type": "FeatureCollection",
            "features": features,
        }

        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

        with open(caminho_saida, 'w', encoding='utf-8') as f:
            json.dump(geojson, f, ensure_ascii=False, indent=2)

        self.stdout.write(self.style.SUCCESS(f"GeoJSON salvo com sucesso em: {caminho_saida}"))
