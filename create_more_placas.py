import uuid
from zonas.models import Subzona, Placa, QRCode

subzona = Subzona.objects.get(nome='Subzona Complexo Recifal')

placas_data = [
    {
        'nome_placa': 'A.S. 1.1.13. MARINA 3 - PONTAL MACEIÓ - APOITAMENTO/ABICAGEM',
        'descricao': 'Área destinada ao apoitamento e abicagem de embarcações e ao embarque e desembarque de embarcações de turismo náutico.',
        'latitude': -8.75556111,
        'longitude': -35.09310278,
    },
    {
        'nome_placa': 'A.S. 1.1.14. FORTE DE TAMANDARÉ - EMBARQUE/ DESEMBARQUE',
        'descricao': 'Área destinada às embarcações de turismo náutico, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.75899444,
        'longitude': -35.09604444,
    },
    {
        'nome_placa': 'A.S. 1.1.15. FORTE DE TAMANDARÉ - BANHISTA',
        'descricao': 'Área destinada a banhistas, podendo ser compartilhada com atividades da pesca artesanal, as quais não conflitem por espaço nem ofereçam risco de acidente.',
        'latitude': -8.75916944,
        'longitude': -35.09648889,
    },
    {
        'nome_placa': 'A.S. 1.1.16. PISCINA - PIRAMBU DO NORTE - BANHISTA.',
        'descricao': 'Área de banho destinada ao uso turístico empresarial ou de base comunitária e ao uso recreativo, comportando a pesca artesanal, conforme a vocação local. O uso da piscina pelas atividades náuticas está condicionado aos parâmetros de conservação ambiental definidos pela APA de Guadalupe e pela APA Costa dos Corais, incluindo a capacidade de carga. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.74249167,
        'longitude': -35.08095,
    },
    {
        'nome_placa': 'A.S. 1.1.17. PISCINA - DA VAL 4 - BANHISTA.',
        'descricao': 'Área de banho destinada ao uso turístico empresarial ou de base comunitária e ao uso recreativo, comportando a pesca artesanal, conforme a vocação local. O uso da piscina pelas atividades náuticas está condicionado aos parâmetros de conservação ambiental definidos pela APA de Guadalupe e pela APA Costa dos Corais, incluindo a capacidade de carga. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.74585556,
        'longitude': -35.08378889,
    },
    {
        'nome_placa': 'A.S. 1.1.18. PISCINA - DA VAL 3/MATAFOME- ATIVIDADE DE MERGULHO.',
        'descricao': 'Área preferencialmente para mergulho livre, podendo comportar banhistas nas ocasiões de baixa-mar de sizígia e comportando a pesca artesanal, conforme a vocação local. O uso da piscina pelas atividades náuticas está condicionado aos parâmetros de conservação ambiental definidos pela APA de Guadalupe e pela APA Costa dos Corais, incluindo a capacidade de carga. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.742625,
        'longitude': -35.08091111,
    },
    {
        'nome_placa': 'A.S. 1.1.19. PISCINA - DA VAL 2/PRAINHA- BANHISTA.',
        'descricao': 'Área de banho destinada ao uso turístico empresarial ou de base comunitária e ao uso recreativo, comportando a pesca artesanal, conforme a vocação local. O uso da piscina pelas atividades náuticas está condicionado aos parâmetros de conservação ambiental definidos pela APA de Guadalupe e pela APA Costa dos Corais, incluindo a capacidade de carga. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.74925556,
        'longitude': -35.08495278,
    },
    {
        'nome_placa': 'A.S. 1.1.20. PISCINA - DA VAL 1 - BANHISTA.',
        'descricao': 'Área de banho destinada ao uso turístico de base comunitária, comportando a pesca artesanal, conforme a vocação local. O uso da piscina pelas atividades náuticas está condicionado aos parâmetros de conservação ambiental definidos pela APA de Guadalupe e pela APA Costa dos Corais, incluindo a capacidade de carga. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.75125556,
        'longitude': -35.08516667,
    },
    {
        'nome_placa': 'A.S. 1.1.21. PISCINA - PIRAMBU DO SUL - ATIVIDADE DE MERGULHO.',
        'descricao': 'Área destinada ao uso turístico de base comunitária para mergulho livre, comportando a pesca artesanal, conforme a vocação local. O uso da piscina pelas atividades náuticas está condicionado aos parâmetros de conservação ambiental definidos pela APA de Guadalupe e pela APA Costa dos Corais, incluindo a capacidade de carga. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.75961944,
        'longitude': -35.085675,
    },
    {
        'nome_placa': 'A.S. 1.1.22. TRÊS CABEÇOS - ATIVIDADE DE MERGULHO.',
        'descricao': 'Área destinada ao uso turístico de base comunitária para mergulho livre, comportando a pesca artesanal, conforme a vocação local. O uso da piscina pelas atividades náuticas está condicionado aos parâmetros de conservação ambiental definidos pela APA de Guadalupe e pela APA Costa dos Corais, incluindo a capacidade de carga. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.75899444,
        'longitude': -35.08917778,
    },
    {
        'nome_placa': 'A.S. 1.1.23. PISCINA DO FORTE 1 - BANHISTA.',
        'descricao': 'Área de banho destinada ao uso turístico empresarial ou de base comunitária e ao uso recreativo, comportando a pesca artesanal, conforme a vocação local. O uso da piscina pelas atividades náuticas está condicionado aos parâmetros de conservação ambiental definidos pela APA de Guadalupe e pela APA Costa dos Corais, incluindo a capacidade de carga. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.76082778,
        'longitude': -35.08939722,
    },
    {
        'nome_placa': 'A.S. 1.1.24. PISCINA DO FORTE 2 - ATIVIDADE DE MERGULHO.',
        'descricao': 'Área preferencialmente para mergulho livre, podendo comportar banhistas nas ocasiões de baixa-mar de sizígia e comportando a pesca artesanal, conforme a vocação local. O uso da piscina pelas atividades náuticas está condicionado aos parâmetros de conservação ambiental definidos pela APA de Guadalupe e pela APA Costa dos Corais, incluindo a capacidade de carga. O fundeio das embarcações deverá ser realizado na borda da área seletiva, em local destinado para tal fim.',
        'latitude': -8.76110833,
        'longitude': -35.09148611,
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
