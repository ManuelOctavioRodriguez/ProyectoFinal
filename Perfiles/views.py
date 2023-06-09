from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import FormularioRegistro, FormularioPerfil, FormularioActualizacion
from .models import Perfil
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView


def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            perfil = Perfil.objects.create(user=user)
            perfil.avatar = form.cleaned_data['avatar']
            perfil.descripcion = form.cleaned_data['descripcion']
            perfil.save()

            login(request, user)
            return redirect('perfil')
        else:
            print("Errores en el formulario:", form.errors)
    else:
        form = FormularioRegistro()
    return render(request, 'Perfiles/registro.html', {'form': form})

@login_required
def perfil(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = FormularioPerfil(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = FormularioPerfil(instance=perfil)
    return render(request, 'Perfiles/perfil.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'Perfiles/iniciar_sesion.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = FormularioActualizacion
    success_url = reverse_lazy('perfil')
    template_name = 'Perfiles/editar_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user