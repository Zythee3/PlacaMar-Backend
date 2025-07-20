# PlacaMar-Backend

## Tecnologia usada:  Django com PostgreSQL e PostGIS para suporte a dados geográficos

## Logica do Banco de dados
### 👤 Usuário (turista ou morador):
    Pode acessar diretamente via QR Code ou pela plataforma web/app.
    Quando acessa, visualiza as zonas disponíveis.

Ao escolher uma zona, ele pode:

    Ver os locais/pontos de interesse daquela zona.
    Ver os conteúdos educativos do local.
    Acessar placas físicas com QR Code.
    Navegar por roteiros.
    Interagir (favoritar, comentar, dar feedback).
    Realizar compras no marketplace.

### 🧑‍💼 Gestor Ambiental:
    Não vê dados de usuários, conteúdos, nem marketplace.

Só acessa relatórios agregados, como:

    Quantas pessoas acessaram zonas.
    Fluxo por zona e por local.
    Alertas de acessos em zonas restritas.

### 🏪 Parceiros B2B (Pousadas, Restaurantes, etc.):
    Podem oferecer produtos no marketplace.
    Seus dados não são acessíveis por gestores.
    Atuam em conjunto com comunidades locais.



## 1. Visão Geral e Reestruturação do Banco de Dados

*   **Gestão de Usuários**: Diferentes tipos de usuários (Admin, Turista, Gestor Ambiental, Parceiro B2B).
*   **Zonas Geográficas e Pontos de Interesse**: Definição de áreas e locais específicos.
*   **Placas QR Code**: Integração com placas físicas para acesso a informações.
*   **Conteúdo Educativo**: Associação de conteúdo a pontos de interesse e zonas.
*   **Marketplace**: Funcionalidades para comunidades e parceiros B2B oferecerem serviços/produtos.
*   **Relatórios e Analytics**: Coleta de dados de acesso, localização, feedbacks e perfis de turistas.
*   **Suporte Geoespacial**: Utilização de PostGIS para campos de geometria.

## 2. Migração de Banco de Dados: SQLite para PostgreSQL/PostGIS

### 2.1. Instalação e Configuração do PostgreSQL e PostGIS

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib postgis
```

**Criação do Usuário e Banco de Dados PostgreSQL:**

```bash
sudo -u postgres psql
CREATE USER placamar WITH PASSWORD 'placamar';
CREATE DATABASE placamar WITH OWNER placamar;
\c placamar;
CREATE EXTENSION postgis;
\q
```

### 2.2. Configuração do Django para PostgreSQL
1.

    ```
    Django==5.0.6
    djangorestframework==3.15.1
    djangorestframework-simplejwt==5.3.1
    django-cors-headers==4.3.1
    python-decouple==3.8
    psycopg2-binary
    ```
2. 

    ```bash
    pip install -r requirements.txt
    ```

3.  

    As configurações do banco de dados em `backend/settings.py` foram alteradas para apontar para o PostgreSQL, e `django.contrib.gis` foi adicionado a `INSTALLED_APPS`.

    ```python
    # ...
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'django.contrib.gis', 
        'corsheaders',
        'usuarios',
        'api.placas',
        'core_admin',
        'zonas',
        'conteudo_educativo',
        'marketplace',
        'relatorios',
    ]
    # ...
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'placamar',
            'USER': 'placamar',
            'PASSWORD': 'placamar',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    # ...
    ```

## 3. Reestruturação dos Modelos Django
*   **`core_admin`**: Contém o modelo `Admin` (o antigo `Usuario` que representa os administradores da plataforma).
*   **`usuarios`**: Contém o novo modelo `Usuario` (para usuários gerais da plataforma, como turistas, gestores ambientais, etc.).
*   **`zonas`**: Gerencia `Zonas`, `PontosDeInteresse`, `Placas` e `Atividades` relacionadas.
*   **`conteudo_educativo`**: Gerencia `ConteudoEducativo` e suas relações com `PontosDeInteresse` e `Zonas`.
*   **`marketplace`**: Gerencia `ComunidadeLocal`, `ParceiroB2B`, `ProdutosMarketplace`, `TransacaoMarketplace` e `RoteiroTuristico`.
*   **`relatorios`**: Gerencia `GestorAmbiental`, `UsuarioGestor`, `RelatorioGestao`, `AcessoQR`, `HistoricoAcessoZona`, `HistoricoLocalizacao`, `LogAcessoZonaRestrita`, `Feedback`, `UsuarioPontoFavorito`, `BoletimBalneabilidade`, `InteracaoIA` e `PerfilTuristaAnalytics`.

## 4. Processo de Migração do Banco de Dados

1.  **Limpar Migrações Antigas e Banco de Dados SQLite:**
    Todos os arquivos de migração antigos e o arquivo `db.sqlite3` foram removidos para garantir um estado limpo.

    ```bash
    rm -f db.sqlite3
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc" -delete
    ```

2.  **Gerar Novas Migrações:**
    Novas migrações foram geradas para todas as aplicações, refletindo a nova estrutura dos modelos.

    ```bash
    python3 manage.py makemigrations
    ```

3.  **Aplicar Migrações:**
    As migrações foram aplicadas ao banco de dados PostgreSQL.

    ```bash
    python3 manage.py migrate
    ```

## 5. Acesso ao Painel de Administração do Django

Para acessar o painel de administração do Django:

1.  **Criar um Superusuário:**
    Se você ainda não tem um superusuário, crie um executando o seguinte comando no seu terminal:

    ```bash
    python3 manage.py createsuperuser
    ```
    Siga as instruções para definir um nome de usuário e senha.

2.  **Iniciar o Servidor de Desenvolvimento:**
    Inicie o servidor Django. Se a porta 8000 estiver em uso, você pode especificar outra porta (ex: 8001).

    ```bash
    python3 manage.py runserver
    # ou
    python3 manage.py runserver 8001
    ```

3.  **Acessar o Painel de Administração:**
    Abra seu navegador e vá para `http://127.0.0.1:8000/admin/` (ou a porta que você estiver usando). Use as credenciais do superusuário que você criou para fazer login.

Você deverá ver todas as aplicações (`Autenticação e Autorização`, `Core Admin`, `Usuários`, `Zonas`, `Conteúdo Educativo`, `Marketplace`, `Relatórios`) listadas no painel de administração, com seus respectivos modelos disponíveis para gerenciamento.

## 6. Funcionalidade de Rastreamento de Localização

Funcionalidade para rastrear a localização do usuário em tempo real e armazenar seu histórico de movimentação, criando um "roteiro".

### Componentes da Funcionalidade

1.  **Modelo `HistoricoLocalizacao`** (`core_admin/models.py`):
    *   Armazena cada ponto de localização de um usuário.
    *   Campos: `usuario` (ForeignKey para `Admin`), `ponto` (PointField do GeoDjango), `timestamp`.

2.  **Serializador `HistoricoLocalizacaoSerializer`** (`core_admin/serializers.py`):
    *   Converte os dados de localização para o formato GeoJSON para a API.

3.  **Endpoints da API** (`core_admin/urls.py`):
    *   `POST /api/admin/registrar-localizacao/`:
        *   **Ação**: Registra a localização atual do usuário.
        *   **Autenticação**: Requerida (o usuário precisa estar logado).
        *   **Corpo da Requisição**: `{"lat": <latitude>, "lon": <longitude>}`.
    *   `GET /api/admin/meu-roteiro/`:
        *   **Ação**: Retorna a lista de todos os pontos de localização (o roteiro) do usuário logado.
        *   **Autenticação**: Requerida.

### Fluxo de Uso (Frontend)

1.  O frontend deve solicitar permissão ao usuário para acessar a geolocalização do navegador.
2.  Periodicamente (ex: a cada 30 segundos), o frontend obtém as coordenadas (latitude e longitude).
3.  As coordenadas são enviadas via `POST` para o endpoint `/api/admin/registrar-localizacao/`.
4.  Para exibir o mapa com o roteiro, o frontend faz uma requisição `GET` para `/api/admin/meu-roteiro/` e desenha os pontos recebidos em um mapa.