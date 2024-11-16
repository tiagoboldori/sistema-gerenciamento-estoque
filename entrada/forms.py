from django import forms
from .models import Entradas

class EntradasForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields =  ['produto','preco','quantidade']
