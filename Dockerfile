# Usar imagem oficial Python 3.10 slim como base
FROM python:3.10-slim

# Evitar criar arquivos .pyc e forçar saída sem buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Atualizar o apt e instalar dependências do sistema necessárias
# build-essential e libpq-dev para compilar psycopg2 (Postgres)
# gdal-bin e libgdal-dev para funcionalidades GIS (PostGIS)
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        libpq-dev \
        gdal-bin \
        libgdal-dev \
        netcat-traditional && \
    rm -rf /var/lib/apt/lists/*

# Copiar o arquivo requirements.txt para dentro do container
COPY requirements.txt /app/

# Instalar as dependências Python listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do projeto para dentro do container
COPY . /app/

# Coletar os arquivos estáticos para produção
RUN python manage.py collectstatic --noinput

# Expor a porta 8000 do container
EXPOSE 8000

# Comando padrão para rodar o servidor via Gunicorn (para produção)
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
