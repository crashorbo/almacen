from django import forms
from django.forms import ModelForm

from articulo.models import Articulo, Categoria, Unidad

class CategoriaCreateForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['codigo', 'nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }


class UnidadCreateForm(ModelForm):
    class Meta:
        model = Unidad
        fields = ['nombre_completo', 'nombre_corto']        
        
        
class ArticuloCreateForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['codigo', 'nombre', 'unidad', 'numero_parte']