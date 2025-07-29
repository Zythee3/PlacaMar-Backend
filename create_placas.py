import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Subzona Complexo Recifal')

placas_data = [
    {
        'nome_placa': 'A.S. 1.1.4 CAMPAS/HOTEL - SUL - BANHISTAS',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.725956,
        'longitude': -35.091067,
    },
    {
        'nome_placa': 'A.S. 1.1.5. AMENDOEIRA - EMBARQUE/DESEMBARQUE',
        'descricao': 'Área destinada preferencialmente às embarcações de turismo náutico, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.738458,
        'longitude': -35.087200,
    },
    {
        'nome_placa': 'VI. A.S. 1.1.6. MARINA 1 IGREJINHA - APOITAMENTO/ABICAGEM',
        'descricao': 'Área destinada ao apoitamento e abicagem de embarcações.',
        'latitude': -8.742092,
        'longitude': -35.087039,
    },
    {
        'nome_placa': 'VII. A.S. 1.1.7. MARINA 2 IGREJINHA - APOITAMENTO /ABICAGEM',
        'descricao': 'Área destinada ao apoitamento e abicagem de embarcações.',
        'latitude': -8.744803,
        'longitude': -35.086650,
    },
    {
        'nome_placa': 'VIII. A.S. 1.1.8. JANGADEIROS TAMANDARÉ - EMBARQUE/DESEMBARQUE',
        'descricao': 'Área destinada às embarcações de turismo náutico, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.750211,
        'longitude': -35.090767,
    },
    {
        'nome_placa': 'IX. A.S. 1.1.9 QUIOSQUES TAMANDARÉ 1 - BANHISTA',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.750494,
        'longitude': -35.091111,
    },
    {
        'nome_placa': 'X. A.S. 1.1.10 PROJETO PRAIA SEM BARREIRAS',
        'descricao': 'Área destinada ao projeto que integra o programa Turismo Acessível, da Empresa Pernambucana de Turismo (EMPETUR) e tem por objetivo garantir o acesso ao lazer de pessoas com deficiência e/ou mobilidade reduzida.',
        'latitude': -8.750839,
        'longitude': -35.091875,
    },
    {
        'nome_placa': 'XI. A.S. 1.1.11 QUIOSQUES TAMANDARÉ 2 - BANHISTA',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.751183,
        'longitude': -35.091858,
    },
    {
        'nome_placa': 'XII. A.S. 1.1.12. TURISMO DE BASE COMUNITÁRIA - QUIOSQUES TAMANDARÉ - EMBARQUE/DESEMBARQUE',
        'descricao': 'Área destinada às embarcações de turismo náutico, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.752531,
        'longitude': -35.092933,
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
