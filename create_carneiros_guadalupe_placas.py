import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Subzona Carneiros/ Guadalupe - Foz Rio Formoso')

placas_data = [
    {
        'nome_placa': 'A.S. 2.4.1 PRAINHA - BRINQUEDOS NÁUTICOS',
        'descricao': 'Área destinada ao uso de atividades náuticas de lazer não motorizadas, como caiaque e Stand Up Paddle, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.68946667,
        'longitude': -35.09678611,
    },
    {
        'nome_placa': 'A.S. 2.4.2 PRAINHA -BANHISTAS',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.68957778,
        'longitude': -35.09609722,
    },
    {
        'nome_placa': 'A.S. 2.4.3 PRAINHA - EMBARQUE / DESEMBARQUE DE EMBARCAÇÃO DE TURISMO',
        'descricao': 'Área destinada às embarcações de turismo náutico, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.689825,
        'longitude': -35.09541111,
    },
    {
        'nome_placa': 'A.S. 2.4.4 IGREJINHA - BANHISTAS 1',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.69307778,
        'longitude': -35.08986944,
    },
    {
        'nome_placa': 'A.S. 2.4.5 IGREJINHA - EMBARQUE/DESEMBARQUE DE EMBARCAÇÃO DE TURISMO',
        'descricao': 'Área destinada às embarcações de turismo náutico, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.69454167,
        'longitude': -35.08861111,
    },
    {
        'nome_placa': 'A.S. 2.4.6 IGREJINHA - BANHISTAS 2',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.69521111,
        'longitude': -35.08795,
    },
    {
        'nome_placa': 'A.S. 2.4.7 RESTAURANTE 1-BANHISTAS',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.69740278,
        'longitude': -35.08468611,
    },
    {
        'nome_placa': 'A.S. 2.4.8 RESTAURANTE 1 -EMBARQUE / DESEMBARQUE DE EMBARCAÇÃO DE TURISMO',
        'descricao': 'Área destinada às embarcações de turismo náutico, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.69852778,
        'longitude': -35.08318611,
    },
    {
        'nome_placa': 'A.S. 2.4.9 RESTAURANTE 1 - BRINQUEDOS NÁUTICOS',
        'descricao': 'Área destinada ao uso preferencial da prática de atividades náuticas de lazer não motorizadas, como caiaque e Stand Up Paddle, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.69944167,
        'longitude': -35.08260556,
    },
    {
        'nome_placa': 'A.S. 2.4.10 PONTAL DE CARNEIROS - EMBARQUE / DESEMBARQUE DE EMBARCAÇÃO DE TURISMO',
        'descricao': 'Área destinada às embarcações de turismo náutico, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.70099722,
        'longitude': -35.08040556,
    },
    {
        'nome_placa': 'A.S. 2.4.11 PONTAL DE CARNEIROS - BRINQUEDOS NÁUTICOS',
        'descricao': 'Área destinada ao uso atividades náuticas de lazer não motorizadas, como caiaque e Stand Up Paddle, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente',
        'latitude': -8.701400,
        'longitude': -35.07930833,
    },
    {
        'nome_placa': 'A.S. 2.4.12 PONTAL DE CARNEIROS - BANHISTAS',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.70178333,
        'longitude': -35.07902778,
    },
    {
        'nome_placa': 'A.S. 2.4.13 ARGILA - EMBARQUE / DESEMBARQUE DE EMBARCAÇÃO DE TURISMO DO TIPO CATAMARÃ',
        'descricao': 'Área pública destinada preferencialmente ao embarque/desembarque de passageiros das embarcações de turismo náutico do tipo catamarã, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente. É permitida a permanência da embarcação na Área Seletiva no máximo por 20 minutos.',
        'latitude': -8.68581944,
        'longitude': -35.09282778,
    },
    {
        'nome_placa': 'A.S. 2.4.14 ARGILA - BANHISTA 1',
        'descricao': 'Área pública destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.68564167,
        'longitude': -35.09256389,
    },
    {
        'nome_placa': 'A.S. 2.4.15 ARGILA - EMBARQUE / DESEMBARQUE DE EMBARCAÇÃO DE TURISMO MIÚDA',
        'descricao': 'Área pública destinada preferencialmente ao embarque/desembarque de passageiros das embarcações de turismo náutico do tipo miúda, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente. É permitida a permanência da embarcação na Área Seletiva no máximo por 20 minutos.',
        'latitude': -8.68591389,
        'longitude': -35.09220278,
    },
    {
        'nome_placa': 'A.S. 2.4.16 ARGILA - FUNDEIO DE EMBARCAÇÕES EXCLUSIVA PARA TRABALHADORES LOCAIS',
        'descricao': 'Área pública destinada ao fundeio de embarcações miúdas ligadas ao transporte dos trabalhadores locais.',
        'latitude': -8.686000,
        'longitude': -35.09206667,
    },
    {
        'nome_placa': 'A.S. 2.4.17 ARGILA- EMBARQUE / DESEMBARQUE DE EMBARCAÇÃO DE TURISMO MIÚDA',
        'descricao': 'Área pública destinada preferencialmente ao embarque/desembarque de passageiros das embarcações de turismo náutico do tipo miúda, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente. É permitida a permanência da embarcação na Área Seletiva no máximo por 20 minutos.',
        'latitude': -8.68618611,
        'longitude': -35.09181111,
    },
    {
        'nome_placa': 'A.S. 2.4.18 ARGILA - BANHISTA 2',
        'descricao': 'Área pública destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.686350,
        'longitude': -35.09157778,
    },
    {
        'nome_placa': 'A.S. 2.4.19 ARGILA- EMBARQUE / DESEMBARQUE DE EMBARCAÇÃO DO TIPO CATAMARÃ',
        'descricao': 'Área pública destinada preferencialmente ao embarque/desembarque de passageiros das embarcações de turismo náutico do tipo catamarã, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente. É permitida a permanência da embarcação na Área Seletiva no máximo por 20 minutos.',
        'latitude': -8.686475,
        'longitude': -35.09105556,
    },
    {
        'nome_placa': 'A.S. 2.4.20 GUADALUPE - EMBARQUE / DESEMBARQUE',
        'descricao': 'Área pública destinada ao embarque/desembarque de passageiros, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente. É permitida a permanência da embarcação na Área Seletiva no máximo por 20 minutos. Contempla um píer flutuante conectado a sua margem, defrontante com a garagem náutica, com 5.0 m de comprimento e numa largura máxima de 1.50m, em direção ao estuário.',
        'latitude': -8.68493889,
        'longitude': -35.095475,
    },
    {
        'nome_placa': 'A.S. 2.4.21 PÍER MARIASSÚ - EMBARQUE/DESEMBARQUE',
        'descricao': 'Área pública destinada ao embarque e desembarque.',
        'latitude': -8.68440833,
        'longitude': -35.10199167,
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
