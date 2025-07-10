# /api/placas/management/commands/import_placas.py

from django.core.management.base import BaseCommand
from api.placas.models import Placa
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Importa placas do arquivo Excel'

    def handle(self, *args, **kwargs):
        path = '/home/guest/Documentos/placamar_data/planilha_placas_v2.xlsx'

        if not os.path.exists(path):
            self.stderr.write(f'Arquivo não encontrado: {path}')
            return

        df = pd.read_excel(path)

        for _, row in df.iterrows():
            placa, created = Placa.objects.get_or_create(
                nome=row['nome_placa'],
                defaults={
                    'latitude': row['latitude'],
                    'longitude': row['longitude'],
                    'subzona': row['subzona'],
                    'localidade': row['localidade_x'],
                    'embarcacoes': row['embarcacoes'],
                    'usuarios': row['usuarios'],
                    'cor': row['cor'],
                    'descricao': row['descricao'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Placa criada: {placa.nome}'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️ Placa já existe: {placa.nome}'))
