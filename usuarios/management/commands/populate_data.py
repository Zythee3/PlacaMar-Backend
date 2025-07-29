
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib.gis.geos import Point

from usuarios.models import Usuario, PAISES_CHOICES
from relatorios.models import AcessoQR, HistoricoAcessoZona, LogAcessoZonaRestrita, PerfilTuristaAnalytics
from zonas.models import QRCode, Zona, Placa # Importar Placa do app zonas
from api.models import Estado, Cidade # Assumindo que Estado e Cidade estão em api.models

class Command(BaseCommand):
    help = 'Popula o banco de dados com 2000 turistas, acessos QR Code e acessos a áreas restritas.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando a população de dados...'))

        # Limpar dados existentes (opcional, para testes)
        # Usuario.objects.filter(tipo_perfil='Turista').delete()
        # AcessoQR.objects.all().delete()
        # HistoricoAcessoZona.objects.all().delete()
        # LogAcessoZonaRestrita.objects.all().delete()
        # PerfilTuristaAnalytics.objects.all().delete()

        # Obter ou criar algumas Zonas e QRCodes para simulação
        zonas = list(Zona.objects.all())
        if not zonas:
            self.stdout.write(self.style.ERROR('Nenhuma Zona encontrada. Por favor, crie zonas antes de executar este script.'))
            return

        qrcodes = list(QRCode.objects.all())
        if not qrcodes:
            self.stdout.write(self.style.ERROR('Nenhum QRCode encontrado. Por favor, crie QRCodes antes de executar este script.'))
            return
        
        placas = list(Placa.objects.all())
        if not placas:
            self.stdout.write(self.style.ERROR('Nenhuma Placa encontrada. Por favor, crie Placas antes de executar este script.'))
            return


        # Dados para geração de turistas
        paises = [choice[0] for choice in PAISES_CHOICES]
        estados_br = list(Estado.objects.all())
        cidades_br = list(Cidade.objects.all())

        if not estados_br or not cidades_br:
            self.stdout.write(self.style.ERROR('Nenhum Estado ou Cidade encontrado. Por favor, crie Estados e Cidades antes de executar este script.'))
            return


        # Gerar 2000 turistas
        self.stdout.write(self.style.SUCCESS('Gerando 2000 turistas...'))
        for i in range(2000):
            username = f'turista_{i+1}'
            password = make_password('senha123') # Senha padrão para todos os turistas
            email = f'turista{i+1}@example.com'
            
            pais_origem = random.choice(paises)
            estado_origem = None
            cidade_origem = None

            if pais_origem == 'Brasil':
                if estados_br:
                    estado_origem = random.choice(estados_br)
                    # Filtrar cidades pelo estado selecionado
                    cidades_do_estado = Cidade.objects.filter(estado=estado_origem)
                    if cidades_do_estado:
                        cidade_origem = random.choice(cidades_do_estado)
            
            usuario = Usuario.objects.create(
                username=username,
                password=password,
                email=email,
                tipo_perfil='Turista',
                idade=random.randint(18, 70),
                pais_origem=pais_origem,
                estado_origem=estado_origem,
                cidade_origem=cidade_origem,
                sexo=random.choice(['Masculino', 'Feminino', 'Outro']),
            )
            
            # Criar PerfilTuristaAnalytics para cada usuário
            PerfilTuristaAnalytics.objects.create(
                usuario=usuario,
                origem_cidade=cidade_origem.nome if cidade_origem else None,
                origem_pais=pais_origem,
                interesses_declarados=random.choice([
                    {'praia': True, 'historia': False},
                    {'praia': False, 'historia': True},
                    {'praia': True, 'historia': True},
                    {'praia': False, 'historia': False}
                ]),
                total_acessos_qr=0,
                zonas_mais_visitadas={}
            )

            # Simular acessos (alguns com QR, alguns sem, alguns em área restrita)
            num_acessos = random.randint(1, 5)
            for _ in range(num_acessos):
                acesso_via_qr = random.choice([True, False])
                zona_acessada = random.choice(zonas)
                
                if acesso_via_qr and qrcodes:
                    qr_code_usado = random.choice(qrcodes)
                    AcessoQR.objects.create(
                        qr_code=qr_code_usado,
                        usuario=usuario,
                        latitude_dispositivo=random.uniform(-8.5, -7.5),
                        longitude_dispositivo=random.uniform(-35.0, -34.0),
                        info_dispositivo=random.choice(['Android', 'iOS', 'Web'])
                    )
                
                HistoricoAcessoZona.objects.create(
                    usuario=usuario,
                    zona=zona_acessada,
                    via_qrcode=acesso_via_qr
                )

                if zona_acessada.restrita and random.random() < 0.3: # 30% de chance de entrar em área restrita
                    LogAcessoZonaRestrita.objects.create(
                        usuario=usuario,
                        zona=zona_acessada,
                        coordenada_entrada=Point(random.uniform(-35.0, -34.0), random.uniform(-8.5, -7.5))
                    )

        self.stdout.write(self.style.SUCCESS('População de dados concluída com sucesso!'))
