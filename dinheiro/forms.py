from dataclasses import fields

from django import forms

from dinheiro.models import Dinheiro


class DinheiroForm(forms.ModelForm):

    class Meta:
        model = Dinheiro
        fields = [
            'banca_nome', 'banca_valor'
        ]
