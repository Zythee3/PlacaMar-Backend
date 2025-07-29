import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Subzona Praia de Tamandaré')

placas_data = [
    {
        'nome_placa': 'A.S. 3.6.1. TAMANDARÉ PESCA 1 - ESTACIONAMENTO',
        'descricao': 'Área destinada apenas ao estacionamento de embarcações de pesca.',
        'latitude': -8.74825833,
        'longitude': -35.08699444,
    },
    {
        'nome_placa': 'A.S. 3.6.2. JANGADEIROS TAMANDARÉ 1 - ESTACIONAMENTO',
        'descricao': 'Área destinada apenas ao estacionamento de embarcações de pesca e das Jangadas utilizadas na atividade turística náutica.',
        'latitude': -8.749950,
        'longitude': -35.08899444,
    },
    {
        'nome_placa': 'A.S. 3.6.3 JANGADEIROS TAMANDARÉ 2 - ESTACIONAMENTO',
        'descricao': 'Área destinada apenas ao estacionamento de embarcações de pesca e das Jangadas utilizadas na atividade turística náutica.',
        'latitude': -8.75564167,
        'longitude': -35.09317222,
    },
    {
        'nome_placa': 'A.S. 3.6.4. TAMANDARÉ PESCA 2 - ESTACIONAMENTO',
        'descricao': 'Área destinada apenas ao estacionamento de embarcações de pesca.',
        'latitude': -8.75861389,
        'longitude': -35.09625556,
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
        localidade_x='', # Default
        num_embarcacoes_desembarque=None, # Default
        max_pessoas_catamara=None, # Default
        max_pessoas_miudas=None, # Default
        atividades_autorizadas='', # Default
    )
    print(f"Placa '{data['nome_placa']}' cadastrada com QR Code: {qr_code_obj.code}")

print("Todas as placas foram cadastradas com sucesso!")
