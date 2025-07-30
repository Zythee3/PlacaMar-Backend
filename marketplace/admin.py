from django.contrib import admin
from .models import ComunidadeLocal, ParceiroB2B, ProdutosMarketplace, TransacaoMarketplace, RoteiroTuristico, RoteiroPontoInteresse

@admin.register(ComunidadeLocal)
class ComunidadeLocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato_email')
    search_fields = ('nome', 'descricao')

@admin.register(ParceiroB2B)
class ParceiroB2BAdmin(admin.ModelAdmin):
    list_display = ('nome_negocio', 'usuario', 'cnpj', 'categoria')
    search_fields = ('nome_negocio', 'cnpj')
    raw_id_fields = ('usuario',)

@admin.register(ProdutosMarketplace)
class ProdutosMarketplaceAdmin(admin.ModelAdmin):
    list_display = ('nome', 'parceiro_b2b', 'comunidade', 'preco', 'ativo')
    list_filter = ('ativo', 'parceiro_b2b', 'comunidade')
    search_fields = ('nome', 'descricao')
    raw_id_fields = ('parceiro_b2b', 'comunidade')

@admin.register(TransacaoMarketplace)
class TransacaoMarketplaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'comprador_usuario', 'data_transacao', 'valor_total', 'status_pagamento')
    list_filter = ('status_pagamento', 'data_transacao')
    search_fields = ('produto__nome', 'comprador_usuario__username')
    raw_id_fields = ('produto', 'comprador_usuario')

@admin.register(RoteiroTuristico)
class RoteiroTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'comunidade', 'tipo')
    list_filter = ('comunidade', 'tipo')
    search_fields = ('nome', 'descricao')
    raw_id_fields = ('comunidade',)

@admin.register(RoteiroPontoInteresse)
class RoteiroPontoInteresseAdmin(admin.ModelAdmin):
    list_display = ('roteiro', 'ponto_interesse', 'ordem')
    list_filter = ('roteiro', 'ponto_interesse')
    raw_id_fields = ('roteiro', 'ponto_interesse')