from django import forms
from .models import Saidas

class SaidasForm(forms.ModelForm):
    class Meta:
        model = Saidas
        fields =  ['produto','quantidade']
