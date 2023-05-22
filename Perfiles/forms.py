from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class FormularioRegistro(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    class Meta:
       model = User
       fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class FormularioPerfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('avatar', 'nombre', 'descripcion')