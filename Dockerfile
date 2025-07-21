# Usar uma imagem oficial do Python como base
FROM python:3.10-slim

# Definir variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependências do sistema
# build-essential e libpq-dev são necessários para o psycopg2
# gdal-bin e libgdal-dev são para as funcionalidades do PostGIS/GEOS
RUN apt-get update \
  && apt-get -y install build-essential libpq-dev gdal-bin libgdal-dev \
  && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências e instalar
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código do projeto para o diretório de trabalho
COPY . /app/

# A porta que o container vai expor
EXPOSE 8000

# O comando padrão para iniciar a aplicação (usando 0.0.0.0 para ser acessível fora do container)
COPY wait-for-it.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-it.sh

CMD ["wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
