from django import forms
from banca_valores.models import Banca_valor

class BancaForm(forms.ModelForm):
 
    class Meta:
        model = Banca_valor
        fields = [
            "valor_inicial" 
        ]


