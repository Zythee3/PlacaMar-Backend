import json
from django.contrib.gis.geos import Point
from zonas.models import Placa, Subzona, Zona

features = []

for placa in Placa.objects.all():
    properties = {
        "nome_placa": placa.nome_placa,
        "descricao": placa.descricao,
        "localidade_x": placa.localidade_x,
        "acesso_restrito": placa.acesso_restrito,
        "num_embarcacoes_desembarque": placa.num_embarcacoes_desembarque,
        "max_pessoas_catamara": placa.max_pessoas_catamara,
        "max_pessoas_miudas": placa.max_pessoas_miudas,
        "atividades_autorizadas": placa.atividades_autorizadas,
        "latitude": float(placa.latitude) if placa.latitude is not None else None,
        "longitude": float(placa.longitude) if placa.longitude is not None else None,
    }

    if placa.subzona:
        properties["subzona"] = placa.subzona.nome
        if placa.subzona.zona:
            properties["zona"] = placa.subzona.zona.nome

    # Remover chaves com valores None para um GeoJSON mais limpo
    properties = {k: v for k, v in properties.items() if v is not None}

    geometry = None
    if placa.latitude is not None and placa.longitude is not None:
        geometry = {
            "type": "Point",
            "coordinates": [float(placa.longitude), float(placa.latitude)],
        }

    feature = {
        "type": "Feature",
        "geometry": geometry,
        "properties": properties,
    }
    features.append(feature)

geojson_data = {
    "type": "FeatureCollection",
    "features": features,
}

output_path = '/app/placasjson/placas.geojson'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(geojson_data, f, ensure_ascii=False, indent=2)

print(f"GeoJSON gerado com sucesso em {output_path}")
