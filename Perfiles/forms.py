from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class FormularioRegistro(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    avatar = forms.ImageField(label='Avatar', required=False)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea, required=False)
    class Meta:
       model = User
       fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2', 'avatar', 'descripcion']
       
class FormularioPerfil(forms.ModelForm):
    avatar = forms.ImageField(label='Avatar', required=False)
    class Meta:
        model = Perfil
        fields = ('avatar', 'nombre', 'descripcion')
        
class FormularioActualizacion(forms.ModelForm):
    avatar = forms.ImageField(label='Avatar', required=False)
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'descripcion']
