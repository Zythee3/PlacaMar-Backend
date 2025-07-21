import os
import json
from django.conf import settings
from django.http import JsonResponse, HttpResponseNotFound

def lista_placas(request):
    geojson_path = os.path.join(settings.BASE_DIR, 'placas.geojson')
    
    if not os.path.isfile(geojson_path):
        return HttpResponseNotFound("Arquivo placas.geojson não encontrado.")
    
    with open(geojson_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return JsonResponse(data, safe=False)
