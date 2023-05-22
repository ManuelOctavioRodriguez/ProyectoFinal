from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Articulo
from .forms import FormularioArticulo
from django.contrib.auth.decorators import login_required

def home(request):
    articulos = Articulo.objects.all()
    return render(request, 'Blog/blog.html', {'articulos': articulos})

def acerca_de(request):
    return render(request, 'Blog/acerca_de.html')

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'Blog/lista_articulos.html', {'articulos': articulos})

def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'Blog/detalle_articulo.html', {'articulo': articulo})

@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = FormularioArticulo(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user.perfil
            articulo.save()
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        form = FormularioArticulo()
    return render(request, 'Blog/crear_articulo.html', {'form': form})

@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.user != articulo.autor.user:
        return redirect('detalle_articulo', pk=articulo.pk)

    if request.method == 'POST':
        formulario = FormularioArticulo(request.POST, instance=articulo)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        formulario = FormularioArticulo(instance=articulo)

    contexto = {
        'formulario': formulario,
        'articulo': articulo
    }
    return render(request, 'Blog/editar_articulo.html', contexto)

@login_required
def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.user != articulo.autor.user:
        return redirect('detalle_articulo', pk=articulo.pk)

    if request.method == 'POST':
        articulo.delete()
        return redirect('lista_articulos')

    contexto = {
        'articulo': articulo
    }
    return render(request, 'Blog/eliminar_articulo.html', contexto)
