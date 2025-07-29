import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Subzona Praia da Gamela/Aver o Mar')

placas_data = [
    {
        'nome_placa': 'A.S. 3.1.1 AVER O MAR - ESTACIONAMENTO DE BARCOS DE PESCA',
        'descricao': 'Área destinada apenas ao estacionamento de embarcações de pesca.',
        'latitude': -8.66918333,
        'longitude': -35.07120556,
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
