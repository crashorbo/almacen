from django import forms
from django.forms import ModelForm

from articulo.models import Articulo, Categoria, Unidad

class CategoriaCreateForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['codigo', 'nombre', 'descripcion']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class UnidadCreateForm(ModelForm):
    class Meta:
        model = Unidad
        fields = ['nombre_completo', 'nombre_corto']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_corto': forms.TextInput(attrs={'class': 'form-control'}),            
        }     
        
        
class ArticuloCreateForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['codigo', 'nombre', 'unidad', 'numero_parte']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad': forms.Select(attrs={'class': 'form-control'}),
            'numero_parte': forms.TextInput(attrs={'class': 'form-control'}),
        }