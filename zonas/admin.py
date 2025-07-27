from django.contrib import admin
from .models import Zona, PontoDeInteresse, Placa, Atividade, PlacaAtividade, QRCode

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'restrita')
    search_fields = ('nome',)

@admin.register(PontoDeInteresse)
class PontoDeInteresseAdmin(admin.ModelAdmin):
    list_display = ('nome', 'zona', 'tipo')
    list_filter = ('zona', 'tipo')
    search_fields = ('nome', 'descricao')

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at')
    search_fields = ('code',)

@admin.register(Placa)
class PlacaAdmin(admin.ModelAdmin):
    list_display = ('qr_code', 'zona', 'ponto_interesse')
    list_filter = ('zona', 'ponto_interesse')
    search_fields = ('descricao',)
    raw_id_fields = ('qr_code',)

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(PlacaAtividade)
class PlacaAtividadeAdmin(admin.ModelAdmin):
    list_display = ('placa', 'atividade')
    list_filter = ('placa', 'atividade')