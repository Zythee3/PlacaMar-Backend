import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Area Proteção Ambiental')

placas_data = [
    {
        'nome_placa': 'APAG GUADALUPE1 - ZATAN',
        'descricao': 'APA DE GUADALUPE - APAG - DECRETO nº 19.635/1997- Área de proteção e conservação dos sistemas naturais essenciais à Biodiversidade - Recursos hídricos, População local, Ecossistemas e Desenvolvimento Sustentável',
        'latitude': -8.380691,
        'longitude': -35.206794,
        'localidade_x': 'APA Guadalupe',
        'atividades_autorizadas': 'Proteção ambiental e biodiversidade',
        'num_embarcacoes_desembarque': 0,
        'max_pessoas_catamara': 0,
        'max_pessoas_miudas': 0,
    },
    {
        'nome_placa': 'APAG GUADALUPE2 - ZATAN',
        'descricao': 'APA DE GUADALUPE - APAG - DECRETO nº 19.635/1997- Área de proteção e conservação dos sistemas naturais essenciais à Biodiversidade - Recursos hídricos, População local, Ecossistemas e Desenvolvimento Sustentável',
        'latitude': -8.378933,
        'longitude': -35.192853,
        'localidade_x': 'APA Guadalupe',
        'atividades_autorizadas': 'Proteção ambiental e biodiversidade',
        'num_embarcacoes_desembarque': 0,
        'max_pessoas_catamara': 0,
        'max_pessoas_miudas': 0,
    },
    {
        'nome_placa': 'APAG GUADALUPE3 - ZATAN',
        'descricao': 'APA DE GUADALUPE - APAG - DECRETO nº 19.635/1997- Área de proteção e conservação dos sistemas naturais essenciais à Biodiversidade - Recursos hídricos, População local, Ecossistemas e Desenvolvimento Sustentável',
        'latitude': -8.408161,
        'longitude': -35.189359,
        'localidade_x': 'APA Guadalupe',
        'atividades_autorizadas': 'Proteção ambiental e biodiversidade',
        'num_embarcacoes_desembarque': 0,
        'max_pessoas_catamara': 0,
        'max_pessoas_miudas': 0,
    },
    {
        'nome_placa': 'APAG GUADALUPE4 - ZATAN',
        'descricao': 'APA DE GUADALUPE - APAG - DECRETO nº 19.635/1997- Área de proteção e conservação dos sistemas naturais essenciais à Biodiversidade - Recursos hídricos, População local, Ecossistemas e Desenvolvimento Sustentável',
        'latitude': -8.405502,
        'longitude': -35.187048,
        'localidade_x': 'APA Guadalupe',
        'atividades_autorizadas': 'Proteção ambiental e biodiversidade',
        'num_embarcacoes_desembarque': 0,
        'max_pessoas_catamara': 0,
        'max_pessoas_miudas': 0,
    },
    {
        'nome_placa': 'APAG GUADALUPE5 - ZATAN',
        'descricao': 'APA DE GUADALUPE - APAG - DECRETO nº 19.635/1997- Área de proteção e conservação dos sistemas naturais essenciais à Biodiversidade - Recursos hídricos, População local, Ecossistemas e Desenvolvimento Sustentável',
        'latitude': -8.402844,
        'longitude': -35.183938,
        'localidade_x': 'APA Guadalupe',
        'atividades_autorizadas': 'Proteção ambiental e biodiversidade',
        'num_embarcacoes_desembarque': 0,
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
