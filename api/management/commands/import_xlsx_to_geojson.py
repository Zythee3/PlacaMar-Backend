from django.core.management.base import BaseCommand
import pandas as pd
import json

class Command(BaseCommand):
    help = 'Converte XLSX para GeoJSON'

    def handle(self, *args, **kwargs):
        df = pd.read_excel('/home/guest/Documentos/Plataforma-PlacaMar/PlacaMar-Backend/api/placas/data/Zatan_Tamandare.xlsx')
        # Renomeia colunas para facilitar acesso no código
        df.rename(columns={
            'localidade_x': 'localidade',
            'Zona': 'zona',
            'Atividades Permitidas': 'atividades_permitidas',
            'Qtd Placas': 'qtd_placas',
            'descricao_(conteudo)': 'descricao',
            'Nº de Embarcações/Desembarque': 'num_embarcacoes',
            'Nº Maximo de pessoas por Embarque/Catamarã': 'max_pessoas_catamara',
            'Nº Maximo de pessoas para Embarque/Miúdas': 'max_pessoas_miudas'
        }, inplace=True)

        features = []
        for _, row in df.iterrows():
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [row["longitude"], row["latitude"]],
                },
                "properties": {
                    "localidade": row["localidade"],
                    "zona": row["zona"],
                    "atividades_permitidas": row["atividades_permitidas"],
                    "qtd_placas": row["qtd_placas"],
                    "nome_placa": row["nome_placa"],
                    "descricao": row["descricao"],
                    "num_embarcacoes": row["num_embarcacoes"],
                    "max_pessoas_catamara": row["max_pessoas_catamara"],
                    "max_pessoas_miudas": row["max_pessoas_miudas"],
                },
            })

        geojson = {
            "type": "FeatureCollection",
            "features": features,
        }

        with open("placas.geojson", "w", encoding="utf-8") as f:
            json.dump(geojson, f, ensure_ascii=False, indent=2)

        self.stdout.write(self.style.SUCCESS('placas.geojson gerado com sucesso'))