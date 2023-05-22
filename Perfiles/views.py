from django.shortcuts import render, redirect
from .forms import FormularioRegistro, FormularioPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('perfil')
    else:
        form = FormularioRegistro()
    return render(request, 'Perfiles/registro.html', {'form': form})

@login_required
def perfil(request):
    if request.method == 'POST':
        form = FormularioPerfil(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = FormularioPerfil(instance=request.user.perfil)
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
    return redirect('inicio')
