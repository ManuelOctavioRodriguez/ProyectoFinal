from django import forms
from .models import Articulo

class FormularioArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('titulo', 'subtitulo', 'cuerpo', 'imagen')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
