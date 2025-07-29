import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Subzona Rio Formoso')

placas_data = [
    {
        'nome_placa': 'A.S. 2.2.1 PEDRA DA MARGAÍDA/PIPIRÍ - ZONA DE PRESERVAÇÃO DA VIDA ESTUARINA (ZPVE) DO SANTUÁRIO DO MERO',
        'descricao': 'Área destinada à conservação estuarina in situ, produção e exportação de biomassa para a pesca local, desenvolvimento de pesquisa e educação ambiental. Proíbe-se atividade náutica (turismo, lazer, transporte e pesca), exceto em situação de pesquisa devidamente aprovada pelas instituições competentes',
        'latitude': -8.671900,
        'longitude': -35.122797,
    },
    {
        'nome_placa': 'A.S. 2.2.2 NOVA HOLANDA- ZONA DE PRESERVAÇÃO DA VIDA ESTUARINA (ZPVE) DO SANTUÁRIO DO MERO',
        'descricao': 'Área destinada à conservação estuarina in situ, produção e exportação de biomassa para a pesca local, desenvolvimento de pesquisa e educação ambiental. Proíbe-se atividade náutica (turismo, lazer, transporte e pesca), exceto em situação de pesquisa devidamente aprovada pelas instituições competentes',
        'latitude': -8.683519,
        'longitude': -35.113183,
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
