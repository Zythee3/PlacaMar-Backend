from django.contrib import admin
from .models import ConteudoEducativo

@admin.register(ConteudoEducativo)
class ConteudoEducativoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'tipo', 'topico', 'placa')
    list_filter = ('tipo', 'topico', 'placa')
    search_fields = ('titulo', 'conteudo')
    fieldsets = (
        (None, {
            'fields': ('titulo', 'tipo', 'conteudo', 'topico', 'placa')
        }),
        ('Dados do Quiz', {
            'fields': ('quiz_data',)
        }),
    )