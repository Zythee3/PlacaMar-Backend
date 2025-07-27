from django.core.management.base import BaseCommand
from api.models import Estado, Cidade
from api.views import ESTADOS_BRASILEIROS, CIDADES_POR_ESTADO

class Command(BaseCommand):
    help = 'Popula o banco de dados com estados e cidades do Brasil.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando a população de estados e cidades...'))

        # Popula Estados
        for estado_data in ESTADOS_BRASILEIROS:
            estado, created = Estado.objects.get_or_create(
                uf=estado_data['value'],
                defaults={'nome': estado_data['text']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Estado {estado.nome} ({estado.uf}) criado.'))
            else:
                self.stdout.write(self.style.WARNING(f'Estado {estado.nome} ({estado.uf}) já existe.'))

        # Popula Cidades
        for uf, cidades_list in CIDADES_POR_ESTADO.items():
            try:
                estado = Estado.objects.get(uf=uf)
                for cidade_nome in cidades_list:
                    cidade, created = Cidade.objects.get_or_create(
                        estado=estado,
                        nome=cidade_nome
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Cidade {cidade.nome} em {estado.uf} criada.'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Cidade {cidade.nome} em {estado.uf} já existe.'))
            except Estado.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Estado com UF {uf} não encontrado para popular cidades.'))

        self.stdout.write(self.style.SUCCESS('População de estados e cidades concluída.'))
