from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Usuario

ESTADOS_BRASILEIROS = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
]

ESTADOS_CHOICES_COMPLETA = [('', '---------')] + ESTADOS_BRASILEIROS + [('Outro', 'Outro')]

class UsuarioAdminForm(UserChangeForm):
    estado_origem = forms.ChoiceField(choices=ESTADOS_CHOICES_COMPLETA, required=False)

    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = (
            'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions',
            'tipo_perfil', 'idade', 'pais_origem', 'estado_origem', 'cidade_origem', 'sexo',
        )

    def clean(self):
        cleaned_data = super().clean()
        pais_origem = cleaned_data.get('pais_origem')
        estado_origem = cleaned_data.get('estado_origem')
        cidade_origem = cleaned_data.get('cidade_origem')

        if pais_origem == 'Brasil':
            if not estado_origem or estado_origem == 'Outro':
                self.add_error('estado_origem', 'Este campo é obrigatório e deve ser um estado válido para o Brasil.')
            # Se estado_origem for preenchido, cidade_origem também é obrigatório
            if estado_origem and not cidade_origem:
                self.add_error('cidade_origem', 'Este campo é obrigatório para o Brasil quando o estado é preenchido.')
        else:
            # Se não for Brasil, estado_origem deve ser 'Outro' ou vazio
            if estado_origem and estado_origem != 'Outro':
                self.add_error('estado_origem', 'Para outros países, o estado deve ser \'Outro\' ou vazio.')
            if not estado_origem:
                cleaned_data['estado_origem'] = None
            if not cidade_origem:
                cleaned_data['cidade_origem'] = None

        return cleaned_data

class UsuarioAdminCreationForm(UserCreationForm):
    estado_origem = forms.ChoiceField(choices=ESTADOS_CHOICES_COMPLETA, required=False)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = (
            'username', 'email', 'tipo_perfil', 'idade', 'pais_origem', 'estado_origem', 'cidade_origem', 'sexo',
        )

    def clean(self):
        cleaned_data = super().clean()
        pais_origem = cleaned_data.get('pais_origem')
        estado_origem = cleaned_data.get('estado_origem')
        cidade_origem = cleaned_data.get('cidade_origem')

        if pais_origem == 'Brasil':
            if not estado_origem or estado_origem == 'Outro':
                self.add_error('estado_origem', 'Este campo é obrigatório e deve ser um estado válido para o Brasil.')
            if estado_origem and not cidade_origem:
                self.add_error('cidade_origem', 'Este campo é obrigatório para o Brasil quando o estado é preenchido.')
        else:
            if estado_origem and estado_origem != 'Outro':
                self.add_error('estado_origem', 'Para outros países, o estado deve ser \'Outro\' ou vazio.')
            if not estado_origem:
                cleaned_data['estado_origem'] = None
            if not cidade_origem:
                cleaned_data['cidade_origem'] = None

        return cleaned_data
