from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import UsuarioAdminForm, UsuarioAdminCreationForm

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    form = UsuarioAdminForm
    add_form = UsuarioAdminCreationForm
    model = Usuario
    list_display = ('username', 'email', 'tipo_perfil', 'is_staff', 'is_active', 'idade', 'pais_origem', 'estado_origem', 'cidade_origem', 'sexo')
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('tipo_perfil', 'idade', 'pais_origem', 'estado_origem', 'cidade_origem', 'sexo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('tipo_perfil', 'idade', 'pais_origem', 'estado_origem', 'cidade_origem', 'sexo')}),
    )

    class Media:
        js = (
            'admin/js/usuario_admin_dynamic_fields.js',
        )