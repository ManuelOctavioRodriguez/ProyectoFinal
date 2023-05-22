from django import forms
from .models import Articulo

class FormularioArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('titulo', 'subtitulo', 'cuerpo', 'imagen')