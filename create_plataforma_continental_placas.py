import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Subzona Plataforma Continental')

placas_data = [
    {
        'nome_placa': 'A.S. 4.1 ILHA DE SANTO ALEIXO -Praia',
        'descricao': 'Banhistas compartilhada com pesca artesanal; Permitido 364 Usuários em simultâneo',
        'latitude': -8.280183,
        'longitude': -35.102544,
        'localidade_x': 'Ilha de Santo Aleixo - Praia',
        'atividades_autorizadas': 'Banhistas',
        'num_embarcacoes_desembarque': None,
        'max_pessoas_catamara': None,
        'max_pessoas_miudas': 200,
    },
    {
        'nome_placa': 'A.S. 4.2 ILHA DE SANTO ALEIXO- Piscina',
        'descricao': 'Conservação da Biodiversidade Marinha; Proteção aos Ambientes Recifais  (309 usuários por dia)',
        'latitude': -8.281597,
        'longitude': -35.101340,
        'localidade_x': 'Ilha de Santo Aleixo - Piscina',
        'atividades_autorizadas': 'Banhistas',
        'num_embarcacoes_desembarque': 0,
        'max_pessoas_catamara': 0,
        'max_pessoas_miudas': 0,
    },
    {
        'nome_placa': 'A.S. 4.3 Ilha de Santo Aleixo - Fundeio de embarcações',
        'descricao': 'Conservação da Biodiversidade Marinha; Proteção aos Ambientes Recifais',
        'latitude': -8.280641,
        'longitude': -35.102594,
        'localidade_x': 'Ilha de Santo Aleixo - Fundeio',
        'atividades_autorizadas': 'Fundeio de até 17 embarcações',
        'num_embarcacoes_desembarque': 17,
        'max_pessoas_catamara': 0,
        'max_pessoas_miudas': 0,
    },
    {
        'nome_placa': 'A.S. 4.4 Ilha de Santo Aleixo - Embarque/Desembarque',
        'descricao': 'Conservação da Biodiversidade Marinha; Proteção aos Ambientes Recifais ; E/D embarcações de turismo náutico; pesca artesanal',
        'latitude': -8.281417,
        'longitude': -35.102317,
        'localidade_x': 'Ilha de Santo Aleixo - E/D PLANO DE MANEJO (ESTUDO DE CARGA/SUPORTE E OPERACIONAL DE ATIVIDADES TURISMO NÁUTICO SUSTENTÁVEL',
        'atividades_autorizadas': 'Embarque/Desembarque',
        'num_embarcacoes_desembarque': 2,
        'max_pessoas_catamara': 0,
        'max_pessoas_miudas': 0,
    },
]

for data in placas_data:
    qr_code_obj = QRCode.objects.create(code=str(uuid.uuid4()))
    Placa.objects.create(
        subzona=subzona,
        qr_code=qr_code_obj,
        nome_placa=data['nome_placa'],
        descricao=data['descricao'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        acesso_restrito=False, # Default
        localidade_x=data['localidade_x'],
        num_embarcacoes_desembarque=data['num_embarcacoes_desembarque'],
        max_pessoas_catamara=data['max_pessoas_catamara'],
        max_pessoas_miudas=data['max_pessoas_miudas'],
        atividades_autorizadas=data['atividades_autorizadas'],
    )
    print(f"Placa '{data['nome_placa']}' cadastrada com QR Code: {qr_code_obj.code}")

print("Todas as placas foram cadastradas com sucesso!")