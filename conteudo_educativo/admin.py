from django.contrib import admin
from .models import ConteudoEducativo

@admin.register(ConteudoEducativo)
class ConteudoEducativoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'topico', 'ponto_interesse', 'zona')
    list_filter = ('tipo', 'topico', 'ponto_interesse', 'zona')
    search_fields = ('titulo', 'conteudo')