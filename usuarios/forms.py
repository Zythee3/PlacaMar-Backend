from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Usuario
from api.models import Estado, Cidade
from api.views import SEXO_CHOICES

class UsuarioAdminForm(UserChangeForm):
    estado_origem = forms.ModelChoiceField(queryset=Estado.objects.all(), required=False, empty_label="---------")
    cidade_origem = forms.ModelChoiceField(queryset=Cidade.objects.none(), required=False, empty_label="---------")
    sexo = forms.ChoiceField(choices=[('', '---------')] + [(sexo, sexo) for sexo in SEXO_CHOICES], required=False)

    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = (
            'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions',
            'tipo_perfil', 'idade', 'pais_origem', 'estado_origem', 'cidade_origem', 'sexo',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'estado_origem' in self.initial:
            try:
                estado_id = self.initial['estado_origem']
                self.fields['cidade_origem'].queryset = Cidade.objects.filter(estado_id=estado_id).order_by('nome')
            except (TypeError, ValueError):
                pass
        elif self.instance.pk and self.instance.estado_origem:
            self.fields['cidade_origem'].queryset = self.instance.estado_origem.cidades.order_by('nome')

    def clean(self):
        cleaned_data = super().clean()
        pais_origem = cleaned_data.get('pais_origem')
        estado_origem = cleaned_data.get('estado_origem')
        cidade_origem = cleaned_data.get('cidade_origem')

        if pais_origem == 'Brasil':
            if not estado_origem:
                self.add_error('estado_origem', 'Este campo é obrigatório para o Brasil.')
            if estado_origem and not cidade_origem:
                self.add_error('cidade_origem', 'Este campo é obrigatório para o Brasil quando o estado é preenchido.')
        else:
            # Para outros países, estado_origem e cidade_origem devem ser nulos
            cleaned_data['estado_origem'] = None
            cleaned_data['cidade_origem'] = None

        return cleaned_data

class UsuarioAdminCreationForm(UserCreationForm):
    estado_origem = forms.ModelChoiceField(queryset=Estado.objects.all(), required=False, empty_label="---------")
    cidade_origem = forms.ModelChoiceField(queryset=Cidade.objects.none(), required=False, empty_label="---------")
    sexo = forms.ChoiceField(choices=[('', '---------')] + [(sexo, sexo) for sexo in SEXO_CHOICES], required=False)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = (
            'username', 'email', 'tipo_perfil', 'idade', 'pais_origem', 'estado_origem', 'cidade_origem', 'sexo',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'estado_origem' in self.initial:
            try:
                estado_id = self.initial['estado_origem']
                self.fields['cidade_origem'].queryset = Cidade.objects.filter(estado_id=estado_id).order_by('nome')
            except (TypeError, ValueError):
                pass
        elif self.instance.pk and self.instance.estado_origem:
            self.fields['cidade_origem'].queryset = self.instance.estado_origem.cidades.order_by('nome')

    def clean(self):
        cleaned_data = super().clean()
        pais_origem = cleaned_data.get('pais_origem')
        estado_origem = cleaned_data.get('estado_origem')
        cidade_origem = cleaned_data.get('cidade_origem')

        if pais_origem == 'Brasil':
            if not estado_origem:
                self.add_error('estado_origem', 'Este campo é obrigatório para o Brasil.')
            if estado_origem and not cidade_origem:
                self.add_error('cidade_origem', 'Este campo é obrigatório para o Brasil quando o estado é preenchido.')
        else:
            cleaned_data['estado_origem'] = None
            cleaned_data['cidade_origem'] = None

        return cleaned_data
