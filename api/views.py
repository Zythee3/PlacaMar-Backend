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
from usuarios.models import Usuario
from conteudo_educativo.models import ConteudoEducativo # Assumindo que o modelo de usuário está aqui

@csrf_exempt
@require_POST
def registrar_acesso_qr(request):
    try:
        data = json.loads(request.body)
        qr_code_str = data.get('codigo_qr') # Renomeado para qr_code_str

        if not qr_code_str:
            return JsonResponse({'error': 'Código QR não fornecido.'}, status=400)

        try:
            qr_code_obj = QRCode.objects.get(qr_code_value=qr_code_str) # Busca o objeto QRCode pelo qr_code_value
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


def get_conteudo_educativo_details(request, conteudo_id):
    try:
        conteudo_educativo = ConteudoEducativo.objects.get(id=conteudo_id)
        data = {
            'id': conteudo_educativo.id,
            'titulo': conteudo_educativo.titulo,
            'tipo': conteudo_educativo.tipo,
            'conteudo': conteudo_educativo.conteudo,
            'topico': conteudo_educativo.topico,
            'placa_id': conteudo_educativo.placa.id if conteudo_educativo.placa else None,
            'quiz_data': conteudo_educativo.quiz_data
        }
        return JsonResponse(data)
    except ConteudoEducativo.DoesNotExist:
        return JsonResponse({'error': 'Conteúdo Educativo não encontrado.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_quiz_question(request, conteudo_id, question_index):
    try:
        conteudo_educativo = ConteudoEducativo.objects.get(id=conteudo_id)
        quiz_data = conteudo_educativo.quiz_data

        if not quiz_data or 'questions' not in quiz_data:
            return JsonResponse({'error': 'Quiz não encontrado para este conteúdo educativo.'}, status=404)

        questions = quiz_data['questions']
        if not (0 <= question_index < len(questions)):
            return JsonResponse({'error': 'Índice da pergunta inválido.'}, status=400)

        question = questions[question_index]
        return JsonResponse({
            'question_index': question_index,
            'question_text': question['question_text'],
            'options': question['options'],
            'total_questions': len(questions)
        })
    except ConteudoEducativo.DoesNotExist:
        return JsonResponse({'error': 'Conteúdo Educativo não encontrado.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_POST
def submit_quiz_answer(request, conteudo_id, question_index):
    try:
        conteudo_educativo = ConteudoEducativo.objects.get(id=conteudo_id)
        quiz_data = conteudo_educativo.quiz_data

        if not quiz_data or 'questions' not in quiz_data:
            return JsonResponse({'error': 'Quiz não encontrado para este conteúdo educativo.'}, status=404)

        questions = quiz_data['questions']
        if not (0 <= question_index < len(questions)):
            return JsonResponse({'error': 'Índice da pergunta inválido.'}, status=400)

        data = json.loads(request.body)
        user_answer_index = data.get('answer_index')

        if user_answer_index is None:
            return JsonResponse({'error': 'Índice da resposta não fornecido.'}, status=400)

        question = questions[question_index]
        is_correct = (user_answer_index == question['correct_answer_index'])

        next_question_index = question_index + 1
        is_last_question = (next_question_index >= len(questions))

        response_data = {
            'is_correct': is_correct,
            'current_question_index': question_index
        }

        if is_last_question:
            # Aqui você pode adicionar lógica para calcular a pontuação total se desejar
            response_data['message'] = 'Quiz concluído!'
            response_data['final_result'] = 'Você respondeu a todas as perguntas.' # Exemplo de resultado final
        else:
            response_data['next_question_index'] = next_question_index
            response_data['message'] = 'Resposta registrada. Próxima pergunta.'

        return JsonResponse(response_data)
    except ConteudoEducativo.DoesNotExist:
        return JsonResponse({'error': 'Conteúdo Educativo não encontrado.'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Requisição inválida. JSON malformado.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

