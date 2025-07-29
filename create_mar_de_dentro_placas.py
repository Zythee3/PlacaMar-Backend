import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Subzona Mar de Dentro')

placas_data = [
    {
        'nome_placa': 'AS 1.2.1. GAMELA/AVER O MAR - BANHISTA',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.67023333,
        'longitude': -35.07115,
    },
    {
        'nome_placa': 'A.S. 1.2.2 GAMELA/AVER O MAR - EMBARQUE/DESEMBARQUE.',
        'descricao': 'Área pública destinada ao embarque/desembarque de passageiros, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente. É permitida a permanência da embarcação na Área Seletiva no máximo por 20 minutos.',
        'latitude': -8.67132778,
        'longitude': -35.07128611,
    },
    {
        'nome_placa': 'A.S. 1.2.3 GAMELA/AVER O MAR - EMBARQUE/DESEMBARQUE DE EMBARCAÇÃO DE TURISMO.',
        'descricao': 'Área pública destinada preferencialmente ao embarque/desembarque de passageiros das embarcações de turismo náutico, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente. É permitida a permanência da embarcação na Área Seletiva no máximo por 20 minutos.',
        'latitude': -8.66926944,
        'longitude': -35.07092778,
    },
    {
        'nome_placa': 'A.S. 1.2.4. TEJUCUSSÚ PROTEÇÃO DO BANCO DE AREIA.',
        'descricao': 'Área que contribui para a manutenção dos terraços marinhos e falésias, paisagem costeira única no Estado de Pernambuco. Por isso, proíbe-se retirada e mobilização de sedimento, abertura de canal, além de comercialização de comida e bebida e festa náutica no local.',
        'latitude': -8.68926389,
        'longitude': -35.08061389,
    },
    {
        'nome_placa': 'A.S. 1.2.5. BANANABOAT - QUIOSQUE DO FUSCA - EMBARQUE/DESEMBARQUE',
        'descricao': 'Área destinada ao embarque e desembarque das atividades náuticas de lazer rebocada, como bananaboat e discoboat, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.73438611,
        'longitude': -35.08875278,
    },
    {
        'nome_placa': 'A.S. 1.2.6. BANANABOAT - CAMPAS',
        'descricao': 'Área destinada à prática das atividades náuticas de lazer rebocada, como bananaboat e discoboat, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.72794722,
        'longitude': -35.08827222,
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
