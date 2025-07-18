from django.core.management.base import BaseCommand
import pandas as pd
import json

class Command(BaseCommand):
    help = 'Converte XLSX para GeoJSON'

    def handle(self, *args, **kwargs):
        df = pd.read_excel('/home/guest/Documentos/Plataforma-PlacaMar/PlacaMar-Backend/api/placas/data/Zatan_v3 (1).xlsx')

        features = []
        for _, row in df.iterrows():
            features.append({
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
            })

        geojson = {
            "type": "FeatureCollection",
            "features": features,
        }

        with open("placas.geojson", "w", encoding="utf-8") as f:
            json.dump(geojson, f, ensure_ascii=False, indent=2)

        self.stdout.write(self.style.SUCCESS('placas.geojson gerado com sucesso'))
