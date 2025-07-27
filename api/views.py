import json
from django.http import JsonResponse
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from .models import Estado, Cidade

PAISES_CHOICES = [
    'Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Costa Rica', 'Cuba',
    'República Dominicana', 'Equador', 'El Salvador', 'Guatemala', 'Honduras',
    'México', 'Nicarágua', 'Panamá', 'Paraguai', 'Peru', 'Porto Rico', 'Uruguai',
    'Venezuela', 'Estados Unidos', 'Canadá', 'Portugal', 'Espanha', 'França',
    'Alemanha', 'Reino Unido', 'Itália', 'Japão', 'China', 'Austrália', 'Outro',
]

SEXO_CHOICES = [
    'Masculino', 'Feminino', 'Outro'
]


def home(request):
    return render(request, 'home.html')

def geojson_placas_view(request):
    geojson_path = Path(settings.BASE_DIR) / 'placasjson' / 'placas.geojson'
    try:
        with open(geojson_path, encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data)
    except FileNotFoundError:
        return JsonResponse({'erro': 'Arquivo placas.geojson não encontrado.'}, status=404)

def get_choices_view(request):
    estados_brasileiros_data = []
    for estado in Estado.objects.all().order_by('nome'):
        estados_brasileiros_data.append({'value': estado.uf, 'text': estado.nome})

    cidades_por_estado_data = {}
    for estado in Estado.objects.all():
        cidades_por_estado_data[estado.uf] = [cidade.nome for cidade in estado.cidades.all().order_by('nome')]

    choices = {
        'paises': PAISES_CHOICES,
        'estados_brasileiros': estados_brasileiros_data,
        'cidades_por_estado': cidades_por_estado_data,
        'sexo': SEXO_CHOICES,
    }
    return JsonResponse(choices)

def get_cidades_por_estado_view(request, estado_id):
    try:
        estado = Estado.objects.get(id=estado_id)
        cidades = [{'id': cidade.id, 'nome': cidade.nome} for cidade in estado.cidades.all().order_by('nome')]
        return JsonResponse({'cidades': cidades})
    except Estado.DoesNotExist:
        return JsonResponse({'error': 'Estado não encontrado.'}, status=404)
