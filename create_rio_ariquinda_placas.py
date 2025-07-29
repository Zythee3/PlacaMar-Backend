import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Subzona Rio Ariquindá')

placas_data = [
    {
        'nome_placa': 'A.S. 2.1.1 MANGUEIRA - EMBARQUE / DESEMBARQUE DE EMBARCAÇÃO DE TURISMO DE BASE COMUNITÁRIA E PESCA ARTESANAL',
        'descricao': 'Área destinada ao embarque, desembarque e fundeio de embarcações ligadas ao turismo de base comunitária e à pesca artesanal. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.69603611,
        'longitude': -35.10459444,
    },
    {
        'nome_placa': 'A.S. 2.1.2 AMARAGI - EMBARQUE / DESEMBARQUE E FUNDEIO DE EMBARCAÇÃO DE TURISMO DE BASE COMUNITÁRIA E PESCA ARTESANAL',
        'descricao': 'Área destinada ao embarque, desembarque e fundeio de embarcações ligadas ao turismo de base comunitária e à pesca artesanal. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.69878889,
        'longitude': -35.10509444,
    },
    {
        'nome_placa': 'A.S. 2.1.3 PORTO DA FOLHA - APOIO À PESCA ARTESANAL',
        'descricao': 'Área destinada ao embarque, desembarque e fundeio de embarcações ligadas à pesca artesanal. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.70885278,
        'longitude': -35.10415278,
    },
    {
        'nome_placa': 'A.S. 2.1.4 TOCA DE BAIXO - ZONA DE PRESERVAÇÃO DA VIDA ESTUARINA (ZPVE) DO SANTUÁRIO DO MERO',
        'descricao': 'Área destinada à conservação estuarina in situ, produção e exportação de biomassa para a pesca local, desenvolvimento de pesquisa e educação ambiental. Proíbe-se atividade náutica (turismo, lazer, transporte e pesca), exceto em situação de pesquisa devidamente aprovada pelas instituições competentes.',
        'latitude': -8.70968056,
        'longitude': -35.09775833,
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
