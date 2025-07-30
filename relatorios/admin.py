from django.contrib import admin
from .models import (
    GestorAmbiental,
    UsuarioGestor,
    RelatorioGestao,
    AcessoQR,
    HistoricoAcessoZona,
    HistoricoLocalizacao,
    LogAcessoZonaRestrita,
    Feedback,
    UsuarioPontoFavorito,
    BoletimBalneabilidade,
    InteracaoIA,
    PerfilTuristaAnalytics,
)

@admin.register(GestorAmbiental)
class GestorAmbientalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'estado', 'status_contrato')
    list_filter = ('tipo', 'estado', 'status_contrato')
    search_fields = ('nome',)

@admin.register(UsuarioGestor)
class UsuarioGestorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'gestor_ambiental', 'cargo')
    list_filter = ('gestor_ambiental', 'cargo')
    raw_id_fields = ('usuario', 'gestor_ambiental')

@admin.register(RelatorioGestao)
class RelatorioGestaoAdmin(admin.ModelAdmin):
    list_display = ('gestor_ambiental', 'tipo_relatorio', 'data_geracao')
    list_filter = ('tipo_relatorio', 'data_geracao')
    raw_id_fields = ('gestor_ambiental',)

@admin.register(AcessoQR)
class AcessoQRAdmin(admin.ModelAdmin):
    list_display = ('qr_code', 'usuario', 'timestamp_acesso')
    list_filter = ('qr_code', 'usuario')
    raw_id_fields = ('qr_code', 'usuario')

@admin.register(HistoricoAcessoZona)
class HistoricoAcessoZonaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'zona', 'timestamp', 'via_qrcode')
    list_filter = ('zona', 'via_qrcode')
    raw_id_fields = ('usuario', 'zona')

@admin.register(HistoricoLocalizacao)
class HistoricoLocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'timestamp_localizacao')
    raw_id_fields = ('usuario',)

@admin.register(LogAcessoZonaRestrita)
class LogAcessoZonaRestritaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'zona', 'timestamp_entrada', 'notificacao_enviada')
    list_filter = ('zona', 'notificacao_enviada')
    raw_id_fields = ('usuario', 'zona')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'ponto_interesse', 'tipo_feedback', 'status', 'criado_em')
    list_filter = ('tipo_feedback', 'status')
    search_fields = ('mensagem',)
    raw_id_fields = ('usuario', 'ponto_interesse')

@admin.register(UsuarioPontoFavorito)
class UsuarioPontoFavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'ponto_interesse')
    raw_id_fields = ('usuario', 'ponto_interesse')

@admin.register(BoletimBalneabilidade)
class BoletimBalneabilidadeAdmin(admin.ModelAdmin):
    list_display = ('ponto_interesse', 'data_emissao', 'status', 'fonte')
    list_filter = ('status', 'fonte')
    raw_id_fields = ('ponto_interesse',)

@admin.register(InteracaoIA)
class InteracaoIAAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'timestamp_interacao', 'avaliacao_utilidade')
    list_filter = ('avaliacao_utilidade',)
    search_fields = ('pergunta', 'resposta_gerada')
    raw_id_fields = ('usuario',)

@admin.register(PerfilTuristaAnalytics)
class PerfilTuristaAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'origem_cidade', 'origem_pais', 'total_acessos_qr')
    list_filter = ('origem_pais',)
    search_fields = ('usuario__username', 'origem_cidade')
    raw_id_fields = ('usuario',)