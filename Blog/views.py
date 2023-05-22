from django.shortcuts import render, get_object_or_404, redirect
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
        form = FormularioArticulo(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        form = FormularioArticulo()
    return render(request, 'Blog/crear_articulo.html', {'form': form})

@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        form = FormularioArticulo(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        form = FormularioArticulo(instance=articulo)
    return render(request, 'Blog/editar_articulo.html', {'form': form, 'articulo': articulo})

@login_required
def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    articulo.delete()
    return redirect('lista_articulos')
