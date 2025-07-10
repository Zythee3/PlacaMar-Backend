import json
from django.http import JsonResponse
from pathlib import Path
from django.conf import settings

def geojson_placas_view(request):
    geojson_path = Path(settings.BASE_DIR) / 'dados' / 'placas.geojson'
    try:
        with open(geojson_path, encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data)
    except FileNotFoundError:
        return JsonResponse({'erro': 'Arquivo placas.geojson não encontrado.'}, status=404)
