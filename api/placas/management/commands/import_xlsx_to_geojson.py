from django.core.management.base import BaseCommand
import os
import pandas as pd
import json
from django.conf import settings

class Command(BaseCommand):
    help = 'Converte uma planilha Excel em um arquivo GeoJSON'

    def handle(self, *args, **kwargs):
        excel_path = os.path.join(settings.BASE_DIR, 'GeoJSON', 'planilha_placas_v2.xlsx')
        output_geojson = os.path.join(settings.BASE_DIR, 'GeoJSON', 'placas.geojson')

        try:
            df = pd.read_excel(excel_path)

            features = []
            for _, row in df.iterrows():
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [row["longitude"], row["latitude"]],
                    },
                    "properties": {
                        "subzona": row["subzona"],
                        "localidade": row["localidade_x"],
                        "embarcacoes": row["embarcacoes"],
                        "usuarios": row["usuarios"],
                        "nome_placa": row["nome_placa"],
                        "cor": row["cor"],
                        "descricao": row["descricao"],
                    },
                }
                features.append(feature)

            geojson = {
                "type": "FeatureCollection",
                "features": features,
            }

            with open(output_geojson, "w", encoding="utf-8") as f:
                json.dump(geojson, f, ensure_ascii=False, indent=2)

            self.stdout.write(self.style.SUCCESS(f"GeoJSON gerado em: {output_geojson}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro: {e}"))
