from django import forms
from django.contrib.auth.forms import UserCreationForm
from api.placas.models import Placa


class PlacaForm(forms.ModelForm):
    class Meta:
        model = Placa
        fields = [
            'nome',
            'latitude',
            'longitude',
            'subzona',
            'localidade',
            'embarcacoes',
            'usuarios',
            'cor',
            'descricao',
        ]
