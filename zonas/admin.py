from django.contrib import admin
from .models import Zona, PontoDeInteresse, Placa, Atividade, PlacaAtividade

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'restrita')
    search_fields = ('nome',)

@admin.register(PontoDeInteresse)
class PontoDeInteresseAdmin(admin.ModelAdmin):
    list_display = ('nome', 'zona', 'tipo')
    list_filter = ('zona', 'tipo')
    search_fields = ('nome', 'descricao')

@admin.register(Placa)
class PlacaAdmin(admin.ModelAdmin):
    list_display = ('codigo_qr', 'zona', 'ponto_interesse')
    list_filter = ('zona', 'ponto_interesse')
    search_fields = ('codigo_qr', 'descricao')

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(PlacaAtividade)
class PlacaAtividadeAdmin(admin.ModelAdmin):
    list_display = ('placa', 'atividade')
    list_filter = ('placa', 'atividade')