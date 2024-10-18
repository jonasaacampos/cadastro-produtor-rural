from django import forms
from .models import ProdutorRural, PropriedadeRural

class PropriedadeRuralForm(forms.ModelForm):
    class Meta:
        model = PropriedadeRural
        fields = ['nome', 'cidade', 'estado', 'area_total', 'area_agricultavel', 'area_vegetacao', 'culturas']

class ProdutorRuralForm(forms.ModelForm):
    class Meta:
        model = ProdutorRural
        fields = ['cpf_cnpj', 'nome', 'fazendas']