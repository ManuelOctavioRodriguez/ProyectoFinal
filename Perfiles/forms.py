from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Campo obligatorio. Ingresa una dirección de correo válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class FormularioPerfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('avatar', 'nombre', 'descripcion')
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }