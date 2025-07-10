from django.contrib import admin
from placas.models import Placa

@admin.register(Placa)
class PlacaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'subzona', 'localidade', 'latitude', 'longitude']
    search_fields = ['nome', 'localidade', 'descricao']
