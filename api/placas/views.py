import os
import json
from django.http import JsonResponse
from django.conf import settings

def lista_placas(request):
    geojson_path = os.path.join(settings.BASE_DIR, "placas.geojson")

    if not os.path.exists(geojson_path):
        return JsonResponse({"erro": "Arquivo placas.geojson não encontrado."}, status=404)

    with open(geojson_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return JsonResponse(data, safe=False)
