from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Secretaria

@admin.register(Secretaria)
class SecretariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'regiao')

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'is_secretaria', 'secretaria', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_secretaria', 'secretaria')}),
    )
