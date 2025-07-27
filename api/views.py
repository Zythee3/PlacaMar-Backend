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

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from zonas.models import Placa, QRCode # Adicionado QRCode
from relatorios.models import AcessoQR
from usuarios.models import Usuario # Assumindo que o modelo de usuário está aqui

@csrf_exempt
@require_POST
def registrar_acesso_qr(request):
    try:
        data = json.loads(request.body)
        qr_code_str = data.get('codigo_qr') # Renomeado para qr_code_str

        if not qr_code_str:
            return JsonResponse({'error': 'Código QR não fornecido.'}, status=400)

        try:
            qr_code_obj = QRCode.objects.get(code=qr_code_str) # Busca o objeto QRCode
        except QRCode.DoesNotExist:
            return JsonResponse({'error': 'QR Code não encontrado.'}, status=404)

        usuario = None
        if request.user.is_authenticated:
            try:
                usuario = Usuario.objects.get(id=request.user.id)
            except Usuario.DoesNotExist:
                pass

        AcessoQR.objects.create(
            qr_code=qr_code_obj, # Usa o objeto QRCode
            usuario=usuario,
            via_qrcode=True
        )
        return JsonResponse({'message': 'Acesso QR registrado com sucesso.'}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Requisição inválida. JSON malformado.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

